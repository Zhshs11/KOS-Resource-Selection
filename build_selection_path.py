"""Join the S1 screening records to the S2 baseline results by stable resource ID.

Run with no arguments to check the published index, or --write to rebuild it.
All inputs are UTF-8 files within this repository.
"""
import argparse
import csv
from collections import defaultdict
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / 'selection_path.csv'
FIELDS = ('resource_id', 'family_id', 'resource_name', 'broad_scope', 'english_content',
          'public_access', 'first_nonpass', 'eligibility', 'panel_status', 'family_decision',
          'baseline_first_rank_min_pct', 'baseline_first_rank_max_pct')

def rows(path):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))

def index(table, key):
    result = {row[key]: row for row in table}
    if len(result) != len(table):
        raise ValueError(f'Duplicate {key} in an input table')
    return result

def build():
    screening = index(rows(ROOT / 'screening.csv'), 'resource_id')
    panel = index(rows(ROOT / 'panel_selection.csv'), 'resource_id')
    ranks = defaultdict(list)
    for record in rows(ROOT / 's2/results/rank_acceptability.csv'):
        rid = record['candidate_id']
        if panel[rid]['family_id'] != record['family']:
            raise ValueError(f'Family mismatch for {rid}')
        ranks[rid].append(Decimal(record['rank_1']))

    leaders = index(rows(ROOT / 's2/results/family_leaders.csv'), 'family')
    winners = {r['candidate_id'] for r in leaders.values()}
    advanced = {rid for rid,s in screening.items() if s['screening_outcome']=='Advance'}
    selected = {rid for rid,s in panel.items() if s['panel_status']=='Selected'}
    if advanced != set(panel) or selected != set(ranks) or len(winners)!=5 or not winners <= selected:
        raise ValueError('The S1 and S2 cohorts do not join')
    for family, record in leaders.items():
        rid = record['candidate_id']
        if (family != panel[rid]['family_id'] or
                (min(ranks[rid]), max(ranks[rid])) != (Decimal(record['min_first']), Decimal(record['max_first']))):
            raise ValueError(f'The baseline leader file and rank file disagree for {rid}')

    output = []
    for rid, s in screening.items():
        p = panel.get(rid, {})
        rank = ranks.get(rid)
        decision = ('Representative' if rid in winners else 'Assessed') if rank else ''
        out = [rid, s['family_id'], s['resource_name'], s['s1_scope'], s['s2_english'],
               s['s3_public_access'], s['first_nonpass'], s['screening_outcome'],
               p.get('panel_status',''), decision,
               f'{min(rank)*100:.2f}' if rank else '', f'{max(rank)*100:.2f}' if rank else '']
        output.append(dict(zip(FIELDS, out)))
    return output

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='write selection_path.csv')
    args = parser.parse_args()
    result = build()
    if args.write:
        with OUTPUT.open('w', encoding='utf-8', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=FIELDS, lineterminator='\n')
            writer.writeheader()
            writer.writerows(result)
    if rows(OUTPUT) != result:
        raise SystemExit('Index differs from the S1/S2 records. Use --write to regenerate.')
    print(f'Validated {len(result)} resources and their links to the S1 and S2 decisions.')

if __name__ == '__main__':
    main()
