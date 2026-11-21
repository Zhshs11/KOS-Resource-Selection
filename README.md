# Selection of knowledge organization systems: 224 resources to five family representatives

This repository accompanies the study's selection of **UDC, YSO, SUMO, Wikidata and BabelNet**. Supplementary S1 explains how 224 records yielded a comparison panel of 20 candidates. Supplementary S2 shows how the evidence and rankings for those candidates led to one representative per family.

| Read the supplement | Inspect its records |
|---|---|
| [S1 · Resource discovery and screening (Word)](s1/Supplementary_S1_Resource_Screening.docx) | [Discovery and evidence tables](s1/) · [224 screening decisions](screening.csv) · [77 panel decisions and rationales](panel_selection.csv) |
| [S2 · Within-family assessment (Word)](s2/Supplementary_S2_Family_Representatives.docx) | [320 source judgments](s2/results/evidence_audit.csv) · [Candidate scores](s2/results/capability_scores.csv) · [Baseline rankings](s2/results/rank_acceptability.csv) · [Sensitivity results](s2/results/sensitivity.csv) |

**To follow a single resource**, look up its ID in the [224-row selection index](selection_path.csv). For example, UDC (`F1-003`) passed all three eligibility checks through the English UDC Summary. Its rules for combining subjects and auxiliaries earned it a place on the 20-resource panel. In the subsequent comparison, UDC led the other three classification systems under the baseline preference model. The same ID links its original screening decision, its panel rationale and its family assessment. Blank later-stage fields mean the resource did not reach that stage. The last two columns give the baseline first-rank share in percent, rounded to two decimals.

## How the panel was formed

| Resources carried forward | Decision |
|---|---|
| 224 identified | The adapted CLeAR search started from 10 resources already prepared and four additional resources named in the study outline. Searches and reference tracing added 210. The catalog grouped versions, translations and pure extractions under a common resource and assigned one primary family to each entry. |
| 224 → 99 | The scope check retained resources serving multiple subject domains or providing a general foundation usable across disciplines. |
| 99 → 88 | The English-content check required usable English terms, labels, definitions or equivalent semantic material in the resource. Multilingual resources could qualify. |
| 88 → 77 | The access check required a documented free route to actual content. It could cover a named public subset, a historical release or a free academic route requiring registration. |
| 77 → 20 | The qualitative panel design considered the organizational feature each resource illustrated, relationships between resources, and the cases allocated to each family. The 57 other eligible resources are recorded as alternatives. |

Each stopped resource is counted at its first failed or unverified check. S1 records 125 scope failures. The English and access checks each account for one recorded failure and ten cases with insufficient evidence. Table S3 in the S1 document gives the rationale for every panel decision.

## How the five representatives were selected

For each family, all candidates were evaluated on the same 16 requests, four each for knowledge representation, semantic map construction and anchoring, semantic path finding, and knowledge retrieval and reasoning support. One assessor coded 248 instances of documented support, 68 instances of documented nonsupport in the specified profile, and four unresolved judgments. Each unresolved judgment was considered under both possible completions. The request definitions and source evidence are in the [S2 assessment package](s2/).

The four support counts were divided by four and combined using shared weights from a symmetric Dirichlet(1,1,1,1) distribution. The SMAA-2 baseline used one million weight draws per family and split credit for ties. A candidate was selected only when its lowest first-rank share across evidence completions, after a simulation allowance, still exceeded every rival's highest share plus that allowance. The percentages below are conditional on the recorded source profiles and preference model.

| Family | Candidates | Representative | Baseline first-rank share | Guarded lead (percentage points) |
|---|---:|---|---:|---:|
| F1 · Classification systems | 4 | UDC | 44.45–88.84% | 10.61 |
| F2 · Subject headings and controlled vocabularies | 3 | YSO | 44.44% | 5.07 |
| F3 · Ontologies and formal knowledge bases | 3 | SUMO | 100.00% | 99.46 |
| F4 · Knowledge graphs and entity authorities | 6 | Wikidata | 100.00% | 99.46 |
| F5 · Lexical-semantic resources | 4 | BabelNet | 49.97–54.15% | 21.67 |

For example, YSO led LCSH (38.84%) and FAST (16.71%) under the baseline draws. All three tie when the four weights are fixed at exactly one quarter. The [family decisions](s2/results/family_leaders.csv), [weight and value sensitivity analyses](s2/results/sensitivity.csv) and [single-judgment challenges](s2/results/evidence_challenges.csv) report where conclusions hold or change. These results concern selection within families. Testing the five representatives on common queries is a subsequent study stage.

## Reproduce and cite

From the repository root, run the following checks with Python. They use the standard library. The first checks the panel and stage totals, the second verifies the detailed discovery and screening records, and the third verifies the index across both supplements. Running `python build_selection_path.py --write` regenerates the index.

```sh
python validate_selection.py
python s1/validate_s1.py
python build_selection_path.py
```

Follow the [S2 reproduction instructions](s2/README.md) to run the within-family calculation from its source judgments, compare it with the published results and inspect the model assumptions. The calculations reproduce decisions conditional on the recorded inputs. Independent reassessment of a judgment requires reviewing its cited source and its specified edition or subset.

When citing the selection in a paper, link to the Git commit for the version consulted. This preserves both supplements and the inputs used to obtain the five representatives. The [earlier 224-to-20 publication](https://github.com/Zhshs11/KOS-Resource-Selection/tree/4bf6bb3141b54963caa3b17abb832281e405bc4a) remains available for existing citations. The historical Word file and `build_document.py` at the repository root belong to that earlier record. The current supplements are the S1 and S2 documents linked above.
