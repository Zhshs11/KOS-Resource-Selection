"""Check the S1 source tables against the published screening and panel decisions."""

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlsplit


HERE = Path(__file__).resolve().parent
STAGES = (
    ("recorded_scope", "s1_scope", "S1"),
    ("recorded_english", "s2_english", "S2"),
    ("recorded_access", "s3_public_access", "S3"),
)
FAMILY_FLOW = {
    "F1": (62, 28, 25, 21, 4, 17),
    "F2": (46, 16, 10, 7, 3, 4),
    "F3": (69, 23, 23, 23, 3, 20),
    "F4": (33, 18, 17, 13, 6, 7),
    "F5": (14, 14, 13, 13, 4, 9),
}


def check(condition, message):
    if not condition:
        raise ValueError(message)


def load(path, count):
    with path.open(encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.DictReader(stream, strict=True))
    check(len(rows) == count, f"{path.name} must contain {count} data rows")
    check(all(None not in row and None not in row.values() for row in rows),
          f"{path.name} has an irregular row")
    return rows


def keyed(rows, key):
    records = {row[key]: row for row in rows}
    check("" not in records and len(records) == len(rows), f"Missing or duplicate {key}")
    return records


def public_url(value):
    parts = urlsplit(value)
    check(parts.scheme in ("http", "https") and parts.hostname
          and not parts.username and not parts.password and not any(c.isspace() for c in value),
          f"Expected a public HTTP(S) link: {value!r}")


def main():
    discovery = keyed(load(HERE / "discovery.csv", 224), "resource_id")
    audit = keyed(load(HERE / "screening_evidence.csv", 224), "resource_id")
    screening = keyed(load(HERE.parent / "screening.csv", 224), "resource_id")
    panel = keyed(load(HERE.parent / "panel_selection.csv", 77), "resource_id")
    searches = keyed(load(HERE / "search_log.csv", 95), "search_id")
    publications = keyed(load(HERE / "publications.csv", 38), "publication_id")
    boundaries = keyed(load(HERE / "boundary_decisions.csv", 68), "lead")
    protocol = load(HERE / "method_protocol.csv", 33)
    check(len({(row["stage"], row["activity"]) for row in protocol}) == 33,
          "Duplicate protocol activity")
    check(sum(row["stage"] == "After-filter screening" for row in protocol) == 5,
          "Expected five screening additions to the 28 discovery entries")
    sources = load(HERE / "screening_sources.csv", 324)
    check(discovery.keys() == audit.keys() == screening.keys(), "Resource ID sets differ")

    origins = Counter(row["discovery_origin"] for row in discovery.values())
    check(origins == {"Prepared seed": 10, "Additional outline seed": 4, "Discovery addition": 210},
          "Discovery-origin counts differ")
    cited_searches, cited_publications = [], []
    for rid, row in discovery.items():
        check(row["family_id"] == rid.split("-")[0] == screening[rid]["family_id"],
              f"{rid} family differs across tables")
        public_url(row["source_url"])
        refs = row["search_ids"].split(";")
        check(len(set(refs)) == len(refs) and set(refs) <= searches.keys(),
              f"{rid} has a duplicate or unknown search ID")
        cited_searches.extend(refs)
        refs = row["publication_ids"].split(";") if row["publication_ids"] else []
        check(len(set(refs)) == len(refs) and set(refs) <= publications.keys(),
              f"{rid} has a duplicate or unknown publication ID")
        cited_publications.extend(refs)
    check((len(cited_searches), len(set(cited_searches))) == (341, 92),
          "Candidate-to-search link counts differ")
    check((len(cited_publications), len(set(cited_publications))) == (59, 34),
          "Candidate-to-publication link counts differ")
    for row in publications.values():
        public_url(row["source_url"])
    for row in searches.values():
        check(row["query_or_tracing_operation"] and row["source_urls"], "Incomplete search record")
        for url in row["source_urls"].splitlines():
            public_url(url)
    for lead, row in boundaries.items():
        check(bool(row["evidence_urls"]) == (lead != "FISH / British Museum thesauri"),
              f"{lead} has unexpected evidence coverage")
        for url in row["evidence_urls"].splitlines():
            public_url(url)

    evidence = defaultdict(dict)
    for row in sources:
        rid = row["resource_id"]
        number = int(row["source_number"])
        check(rid in audit and number not in evidence[rid], "Unknown resource or duplicate source number")
        public_url(row["source_url"])
        evidence[rid][number] = row["source_url"]
    check(evidence.keys() == audit.keys(), "Some resources lack numbered source links")

    flow = defaultdict(Counter)
    later_access = Counter()
    advanced = set()
    for rid, row in audit.items():
        family = discovery[rid]["family_id"]
        totals = flow[family]
        totals["discovered"] += 1
        stop = ""
        for raw_field, flow_field, stage in STAGES:
            status = row[raw_field]
            check(status in {"Pass", "Fail", "Unverified", "Not assessed"}, f"{rid} unknown status")
            expected = "Not assessed" if stop else status
            check(screening[rid][flow_field] == expected, f"{rid} sequential {stage} status differs")
            if stop:
                if stage == "S3" and status != "Not assessed":
                    later_access[status] += 1
            elif status == "Pass":
                totals[stage] += 1
            else:
                check(status in {"Fail", "Unverified"}, f"{rid} has an unassessed first stop")
                stop = stage
        check(screening[rid]["first_nonpass"] == stop, f"{rid} first non-pass differs")
        retained = not stop
        check(screening[rid]["screening_outcome"] == ("Advance" if retained else "Not advanced"),
              f"{rid} sequential outcome differs")
        check(row["audit_decision"] == ("Retain" if retained else "Exclude"),
              f"{rid} audit decision differs")
        urls = evidence[rid]
        check(set(urls) == set(range(1, len(urls) + 1)), f"{rid} citation numbering differs")
        check(bool(row["accepted_data_url"]) == retained, f"{rid} accepted route differs")
        if retained:
            check(row["accepted_data_url"] in urls.values(), f"{rid} data route lacks a source link")
            advanced.add(rid)
        for field in ("scope_evidence", "english_evidence", "access_evidence", "access_and_coverage"):
            check(row[field].strip(), f"{rid} lacks {field}")
    check(advanced == panel.keys(), "Panel IDs differ from the 77 eligible IDs")
    check(later_access == {"Pass": 4, "Fail": 2, "Unverified": 2}, "Later access assessments differ")
    for rid, row in panel.items():
        family = discovery[rid]["family_id"]
        check(family == row["family_id"], f"{rid} panel family differs")
        check(row["panel_status"] in {"Selected", "Alternative"}, f"{rid} unknown panel status")
        flow[family][row["panel_status"]] += 1
    check(set(flow) == set(FAMILY_FLOW), "Family set differs")
    for family, expected in FAMILY_FLOW.items():
        counts = flow[family]
        actual = tuple(counts[k] for k in ("discovered", "S1", "S2", "S3", "Selected", "Alternative"))
        check(actual == expected, f"{family} flow differs: {actual}")
    print("S1 verified: 33 protocol entries, 224 candidates, 95 searches, 38 publications and 68 boundary decisions.")
    print("224 -> 99 -> 88 -> 77 eligible -> 20 selected, 57 alternatives. All five families agree.")
    print("324 ordered evidence links, 77 accepted routes and 8 later access assessments checked.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, KeyError, csv.Error) as err:
        sys.exit(f"S1 validation failed: {err}")

