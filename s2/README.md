# Selecting one representative per KOS family

The 20 resources admitted in Supplementary S1 were assessed against 16 requests within each family. The assessment dated 13 October 2026 records one assessor’s judgments about named editions and source profiles. The sample contains four unresolved judgments. The readers’ guide gives the five request sets, the evidence behind each selection and the cases where the selection changes. [Supplementary S2](Supplementary_S2_Family_Representatives.docx)

## Reproduce the analysis

From this directory, run the following commands with Python 3.12.14. NumPy 2.3.5 was used for the released run. The script contains the assessment and runs offline once NumPy is available.

```sh
python -m pip install numpy==2.3.5
python select_representatives.py
```

On a local machine the script writes to `family_leader_selection_output/` in the working directory. Set `FAMILY_SELECTION_OUTPUT` to choose another destination. The release run used one OpenBLAS/OpenMP thread, PCG64 with base seed 20261013, and batches of 20,000. The run manifest records the draw counts, scenario names, software versions and input hashes. The self-tests cover panel integrity, evidence coding, tie handling, rankings and the selection rule. [Run manifest](results/manifest.json) · [90 self-tests](results/self_tests.json)

## Trace a candidate

| Question | Released file |
| --- | --- |
| Which candidate, edition and access boundary were assessed? | [20 panel profiles](results/panel.csv) |
| What evidence satisfies each request? | [Protocol and 80 request definitions](results/protocol.json) |
| What did the assessor record for this candidate? | [320 judgments with observations and source identifiers](results/evidence_audit.csv) |
| Where can I inspect the cited documentation or a recorded correction? | [59 reference records](results/sources.json) · [Five amendments](results/quality_review_amendments.json) |
| Which requests contribute to each capability? | [Request codes and count bounds for all 20 candidates](results/capability_scores.csv) |
| Where did each candidate rank for each possible resolution of the evidence? | [42 candidate-by-completion rank distributions](results/rank_acceptability.csv) |
| Which candidate met the decision rule in each family? | [Five baseline selections and guarded leads](results/family_leaders.csv) |
| How sensitive were the selections? | [150 family-by-scenario results, including five baselines](results/sensitivity.csv) · [316 individual evidence reversals](results/evidence_challenges.csv) |

Join records by `candidate_id` and `test_id`. The evidence codes are 1 (supported), 0 (absent within the stated profile) and blank (unresolved). In the capability file the four symbols in each `C*_bits` column correspond to requests a–d, with `?` marking an unresolved judgment. C1 covers knowledge representation, C2 semantic map construction and anchoring, C3 semantic path finding, and C4 knowledge retrieval and reasoning support.

Each baseline capability is its supported fraction out of four equally weighted requests. The simulation samples one million weight vectors per family from Dirichlet(1,1,1,1), scores all candidates under each vector and divides tied positions equally. Every possible 0/1 resolution of that family’s unknowns is evaluated using the same vectors. First-rank shares are reported separately for these completions. The selected candidate’s smallest first-rank share must exceed every rival’s largest share by more than twice the simultaneous Monte Carlo allowance. The guard covers sampling error in those numerical shares. Source judgments and choices of weights are examined separately in the sensitivity files.

In the rank table, `rank_1` through `rank_6` give the fraction of draws at each applicable rank. A completion label such as `2:3c=0` means the third candidate in the family’s panel order took value 0 for C3c. Multiple assignments in a label apply together. `central_w1` through `central_w4` are the mean criterion weights over draws in which the candidate received first-rank credit, weighted by that credit. These fields are blank when the credit is zero. In the sensitivity table, the vectors in `min_first` and `max_first` follow the same panel order. A blank `selected` means the comparison did not separate a representative.

## Release provenance

The public script retains the checked numerical implementation and embeds its 320 evidence records. The script header, assessment description and the titles, locators and document links for two local provenance records (R01 and R02) were edited for public distribution. Those links point to the published counterparts of the original outline and panel record. Their `local:` paths are relative to the released source register. The changes produce a new assessment hash. The original was `898a679a4b14c7165b5c11c1d46da4c15997f22229ba064229404486bb6299f6`. The release hash is in the manifest. Both versions have protocol hash `7bc648d4e078d645a89a8bb168696bc8ba7bb73f4c531de3c2a1002faa64e2f8`.

The original and public scripts were both run in the recorded environment. Their seven CSV files, protocol, amendment record and self-test results matched byte for byte. The full selection and sensitivity summary also matched the archived notebook output.

The source register describes the material consulted by the assessor. Raw source snapshots, executed adapter benchmarks and independent reassessment would require separate evidence. A rerun also generates a complete assessment JSON, CSV request definitions, expanded JSON results and a Markdown summary. The files linked above are the deposited subset.
