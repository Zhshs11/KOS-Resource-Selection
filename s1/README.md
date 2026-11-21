# Supplementary S1 · Resource screening and comparative selection

These records accompany [Supplementary S1](Supplementary_S1_Resource_Screening.docx). They document the identification of 224 knowledge organization systems (KOSs), the eligibility decisions for all 224 resources, and the selection of 20 candidates from the 77 that met the eligibility criteria. For an individual resource, look up the same `resource_id` in [discovery.csv](discovery.csv), [screening_evidence.csv](screening_evidence.csv) and [screening_sources.csv](screening_sources.csv). The [screening flow](../screening.csv) and [panel decisions](../panel_selection.csv) are in the parent directory.

## Resource identification and family assignment

The study adapted CLeAR from Campos et al. (2020). Cycle I specified the objects, relations, domains and dependencies of interest. The five families below are the study's own grouping. Cycle II combined named-resource and maintainer searches with resource-type terms (such as classification, thesaurus and ontology) and subject terms. Survey tables, public directories and documented reuse or import relationships supplied further leads. The catalog distinguishes citations and mappings from derivation. It records 10 previously prepared seeds, four additional outline seeds (ACM CCS, CLC, Cyc/OpenCyc and WordNet) and 210 additions. [CLeAR paper](https://doi.org/10.1016/j.envsoft.2020.104813)

The catalog required an identifiable system and a source describing its objects and at least one organizational mechanism. A paper, provider's documentation or authoritative catalog could establish the structure. Discovery admitted restricted and historical systems with public structural descriptions. Versions, translations, serializations and pure extractions counted with their parent system. A derived system could receive a distinct entry if it had a distinct organizational purpose. FAST and LCSH therefore have separate IDs, while Wiktionary and its DBnary extraction share an entry. The 68 boundary decisions include excluded leads, scope qualifications and consolidation decisions. Subtracting 68 from a hit count would not reconstruct the catalog.

| Primary family | Assignment rule | Discovered | Scope pass | English pass after scope | All three pass | Selected | Alternative |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| F1 Classification systems | Divides subjects or fields into categories, including faceted and multilevel schemes. | 62 | 28 | 25 | 21 | 4 | 17 |
| F2 Subject headings and controlled vocabularies | Controls terms or concepts for indexing, retrieval or terminology work. | 46 | 16 | 10 | 7 | 3 | 4 |
| F3 Ontologies and formal knowledge bases | Models classes, properties, relations, constraints or axioms. | 69 | 23 | 23 | 23 | 3 | 20 |
| F4 Knowledge graphs and entity authorities | Organizes entities, facts, identities or commonsense concepts through typed relations. | 33 | 18 | 17 | 13 | 6 | 7 |
| F5 Lexical-semantic resources | Organizes lexical meaning through senses, synsets, frames or sememes. | 14 | 14 | 13 | 13 | 4 | 9 |
| Total | One primary family per ID. | 224 | 99 | 88 | 77 | 20 | 57 |

Primary family follows the objects organized. For example, a SKOS serialization alone cannot determine family assignment. YSO belongs to F2 and carries a secondary ontology attribute. Related components may also be combined across releases. The catalog keeps these qualifications in each resource's discovery record.

## Eligibility and candidate-level decisions

1. **Scope.** A system qualified when it covered several domains or supplied a general foundation reusable across disciplines. The screening audit reconsidered the preliminary labels. F2-008 and F2-018 passed after an initial domain-specific label. F3-015, F3-030, F3-053 and F3-054 failed after an initial cross-domain label. The stage removed 125 systems.
2. **English semantic content.** Usable labels, definitions, class captions, senses or equivalent English content had to occur in the resource itself. Among the 99 systems that reached this stage, one failed and ten had insufficient evidence.
3. **Public access.** A free route to usable resource data could be a browser, download or API. Free registration, academic licensing, a documented subset or a historical release could qualify within the recorded coverage. Of the 88 systems that reached this stage, one failed and ten had insufficient evidence. The 77 accepted routes identify the particular data available at screening.

Each criterion has its own recorded status and explanation. `Pass` means the criterion was met, `Fail` means the available evidence showed it was unmet, `Unverified` means the evidence was insufficient, and `Not assessed` means the audit did not assess it. The parent screening table stops each resource at its first non-pass and marks later stages `Not assessed`. The audit also recorded access for eight resources that stopped at English. Four access assessments were Pass, two were Fail and two were Unverified. Those eight assessments do not change the flow. The audit's free-text category “No English data” covers some Unverified records. Use the criterion status for counts.

Among the 77 eligible resources, the panel documented the organizational feature each could illustrate, dependence or overlap with other resources, and the rationale for inclusion or alternative status. It used qualitative judgment and the space allocated within each family. For example, F1-003 (UDC) qualified via its public Summary and was selected for its auxiliaries and combination rules. F1-034 (International Patent Classification) also qualified and remained an alternative because the panel allocated no separate patent classification case. The reasons and outcomes for all 77 are in [panel_selection.csv](../panel_selection.csv).

## Files and fields

CSV files use UTF-8, a header row and standard quoting. Use a CSV reader because a quoted cell can contain line breaks. Resource, publication and search IDs are case-sensitive.

| File and key | Field definitions |
| --- | --- |
| [method_protocol.csv](method_protocol.csv) · 33 · `stage` + `activity` | Covers the 28 discovery protocol entries and the five eligibility-screening additions. `stage`, `activity` and `status` preserve the workbook's labels. `implementation` and `source_or_limit` summarize the documented procedure, reference or qualification for public use. |
| [discovery.csv](discovery.csv) · 224 · `resource_id` | `resource_name` is the catalog's full English name. `family_id` gives the single primary family. `discovery_origin` distinguishes prepared seeds, additional outline seeds and discovery additions. `preliminary_scope`, `subtype` and `subject_domain` are the discovery assessments. `organizational_logic` describes the objects and relations, and `inclusion_basis` explains their relevance. `secondary_attributes`, `related_resources`, `counting_unit` and `boundary_note` preserve cross-family features, dependencies and consolidation limits. `search_ids` and `publication_ids` contain semicolon-separated keys. A blank publication list means the catalog cited the row's primary source directly. `source_type`, `source_title` and `source_url` identify that source. |
| [search_log.csv](search_log.csv) · 95 · `search_id` | `query_or_tracing_operation` records the queries or navigation within a batch. `channel`, `purpose`, `source_urls` (one per line) and `results_and_limits` record the search context and findings. The 224 candidates point to 92 distinct log entries. Three further entries document directory, literature or dependency tracing across candidates. A batch can contain several queries or page visits. |
| [publications.csv](publications.csv) · 38 · `publication_id` | `title`, `authors_or_organization`, `year` and `source_url` identify the document. `role`, `related_resources`, `disposition`, `rationale` and `reading_coverage` describe its use. The log contains 34 included records, two included as methodological literature, one retained lead and one exclusion. |
| [boundary_decisions.csv](boundary_decisions.csv) · 68 · `lead` | `decision` and `rationale` state the treatment of a named lead or group. `related_resources` retains the original names, which can include excluded leads without resource IDs. `evidence_urls` gives the cited link when available. The FISH / British Museum thesauri lead had insufficient evidence and no URL in this field. |
| [screening_evidence.csv](screening_evidence.csv) · 224 · `resource_id` | `recorded_scope`, `recorded_english` and `recorded_access` are the original criterion results. `scope_evidence`, `english_evidence` and `access_evidence` are the criterion-specific explanations. `audit_decision`, `audit_category` and `decision_rationale` are the audit's disposition, reason category and overall explanation. `accepted_data_url` is filled for the 77 retained systems. `access_and_coverage` gives release, access and coverage limits as recorded. |
| [screening_sources.csv](screening_sources.csv) · 324 · `resource_id` + `source_number` | `source_url` is the numbered supporting link on that resource's audit row. The number preserves the within-row order of the bracketed citations in S1 Table S2. The audit groups URLs by resource and gives separate evidence text for each criterion. A URL cannot always be assigned to a single criterion from this record. |
| [screening.csv](../screening.csv) · 224 · `resource_id` | `s1_scope`, `s2_english`, `s3_public_access`, `first_nonpass` and `screening_outcome` reproduce the sequential flow. `decision_basis` summarizes the recorded reason. |
| [panel_selection.csv](../panel_selection.csv) · 77 · `resource_id` | `organizational_contrast`, `relationship_and_boundary` and `panel_reason` justify each `panel_status` (Selected or Alternative). |

## Verification and scope

From the parent directory, run the following commands with Python 3. Both read the published files locally and use the Python standard library.

```sh
python validate_selection.py
python s1/validate_s1.py
```

The checks reproduce the ID joins, family counts, sequential eligibility results, eight later access assessments, accepted-route coverage, numbered evidence links and panel membership. The records preserve the interpreted evidence and the provider URLs recorded at screening. Three URL parameters used for tracking or sharing (`msockid`, `trk` and `usp`) were removed from the S1 data files. The export uses public-facing descriptions of the search interface and of the CLeAR reading record.

The search protocol evolved during discovery. There was no preregistered query sequence, complete hit export, compilation of every rejected result, or exhaustive forward and backward citation search. The logged searches cannot independently generate an identical universe of web results. CLeAR's operational-data analysis, citation/reuse thresholds and Cycle III quality evaluation were outside this discovery exercise. The panel has no recorded numerical weights or tie-breaker. Its counts can be recomputed and its reasons inspected. The archive does not test live data access or establish an optimal panel.

