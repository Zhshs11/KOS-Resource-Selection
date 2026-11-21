"""Select a representative in each of five knowledge organization system families.

Run with Python 3.10 or later and NumPy. The embedded documentary assessment
is the input to the numerical analysis. See README.md for the protocol and
output definitions.
"""
import json

# Embedded source assessment. Amend only with traceable evidence and rerun.
BUNDLE = json.loads(r'''
{
  "assessment_date": "2026-10-13",
  "basis": "Source-based assessment of the confirmed panel under the declared family-specific requests",
  "review_mode": "single_assessor_documentary",
  "independent_review_completed": false,
  "source_adapters_executed": false,
  "raw_source_snapshots_captured": false,
  "protocol": {
    "allow_legacy_scores": false,
    "allow_name_override": false,
    "cross_family_pooling": false,
    "date": "2026-10-13",
    "denominator": 4,
    "family_names": {
      "F1": "Classification systems",
      "F2": "Subject headings and controlled vocabularies",
      "F3": "Ontologies and formal knowledge bases",
      "F4": "Knowledge graphs and entity authorities",
      "F5": "Lexical-semantic resources"
    },
    "nature": "Exploratory documentary conformance assessment; not preregistered and not an operational benchmark",
    "score_meaning": "count of satisfied, equally valued obligations within the declared family profile",
    "status_values": [
      0,
      1,
      null
    ],
    "tests": [
      {
        "criterion": "C1",
        "family": "F1",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Return an identified atomic subject category.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F1-C1a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C1",
        "family": "F1",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Recover the category’s broader disciplinary context.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F1-C1b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C1",
        "family": "F1",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Express a combination of independent subjects in source-defined compound notation.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F1-C1c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C1",
        "family": "F1",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Retain a separately interpretable place, time or form qualifier in a constructed class expression.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F1-C1d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F1",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Find a native reference from its canonical English caption.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F1-C2a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F1",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Use a separately supplied index term, keyword or note as an additional lexical access cue.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F1-C2b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F1",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Use source context to distinguish different subject interpretations of similar wording.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F1-C2c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F1",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Recover the native subject reference from a supplied external record’s classification assignment (record-to-subject anchoring, not subject-to-document retrieval).",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F1-C2d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F1",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Follow one source-defined broader/narrower step.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F1-C3a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F1",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Follow two hierarchical steps without inventing an intermediate subject.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F1-C3b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F1",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Follow a documented nonhierarchical class cross-reference.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F1-C3c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F1",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Navigate from a compound subject expression to its independently identified subject components.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F1-C3d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F1",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Return the caption and classification context for a located class.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F1-C4a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F1",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Return a class-specific explanatory or scope note beyond its caption.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F1-C4b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F1",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Return a source instruction that redirects or excludes a competing classification.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F1-C4c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F1",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Return a source-linked documentary record associated with the class rather than an unrestricted web search.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F1-C4d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C1",
        "family": "F2",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Represent an identified controlled subject.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F2-C1a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C1",
        "family": "F2",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Preserve an ordered cross-facet subject expression (topic together with place, time or form) and its subdivision roles. Within-topical precoordination alone is not this test.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F2-C1b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C1",
        "family": "F2",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Distinguish topic from at least one place, time or form component through native field/facet types, rather than inferring the role from its label.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F2-C1c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C1",
        "family": "F2",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Retain a source qualification that distinguishes a subject meaning.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F2-C1d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F2",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Resolve a preferred subject expression to an existing reference.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F2-C2a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F2",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Resolve an authorized alternative expression through a native equivalence reference.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F2-C2b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F2",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Inspect source context that distinguishes a qualified or ambiguous subject label.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F2-C2c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F2",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "For a qualified subject input, supply its complete postcoordinate anchor set through the native model without constructing a new authorized compound heading; lookup of an already established heading alone is not this request.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F2-C2d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F2",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Follow a source broader/narrower subject relationship.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F2-C3a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F2",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Follow a source associative subject relationship.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F2-C3b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F2",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Keep lexical equivalence distinct from broader/narrower subject meaning.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F2-C3c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F2",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Keep separately encoded part-whole relations distinct from generic hierarchical relations.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F2-C3d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F2",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Return the native heading or concept content together with its identifier.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F2-C4a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F2",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Return a supplied note that clarifies the subject’s scope or use.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F2-C4b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F2",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Trace an authority/concept record to its documented supplying source or source vocabulary.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F2-C4c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F2",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Retain a native record status or modification marker when exporting the evidence.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F2-C4d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C1",
        "family": "F3",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Represent identified classes and typed relations.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F3-C1a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C1",
        "family": "F3",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Represent a situation with more than two independently named participant roles.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F3-C1b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C1",
        "family": "F3",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Express explicit logical restriction such as disjointness, negation or cardinality.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F3-C1c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C1",
        "family": "F3",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Supply a native variable-bearing conditional clause with explicit logical scope beyond fixed class-restriction or property-chain templates; a published definite-clause rule qualifies.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F3-C1d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F3",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Locate a class or relation through its supplied English wording.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F3-C2a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F3",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Locate a meaning through an alternative lexical expression supplied by the source.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F3-C2b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F3",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Use released links between ontology references and an independent lexical-sense inventory.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F3-C2c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F3",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Distinguish equivalence, subsumption, instance or approximate meaning in the supplied lexical mapping.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F3-C2d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F3",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Follow native class-subclass relationships.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F3-C3a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F3",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Follow named participant or relation roles in their source direction.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F3-C3b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F3",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Use an explicitly stated inverse or subproperty relation instead of reversing edges indiscriminately.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F3-C3c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F3",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Apply a supplied non-taxonomic relation-composition or transitivity rule to a two-link path.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F3-C3d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F3",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Retrieve a source definition associated with an identified class or relation.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F3-C4a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F3",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Retrieve an individually inspectable schema statement or axiom.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F3-C4b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F3",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Retrieve a logical restriction or rule beyond plain RDFS subclass/subproperty propagation.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F3-C4c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F3",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Trace a lexical mapping or definition to its specified source record or source identifier.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F3-C4d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C1",
        "family": "F4",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Represent a typed subject-relation-object assertion.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F4-C1a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C1",
        "family": "F4",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Attach independently identified qualifications to an individual assertion.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F4-C1b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C1",
        "family": "F4",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Represent an explicit negative claim or known absence rather than treating an omitted edge as false.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F4-C1c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C1",
        "family": "F4",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Distinguish an unknown value from a known absence in the assertion representation.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F4-C1d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F4",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Locate a native node from supplied English text.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F4-C2a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F4",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Follow an explicit alias, synonym or equivalence route for an alternative expression.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F4-C2b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F4",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Retain supplied sense, description or entity-type context instead of silently merging homonymous references.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F4-C2c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F4",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Follow a native cross-resource reference to an identified source concept or entity.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F4-C2d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F4",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Follow a relation in its documented semantic direction.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F4-C3a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F4",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Join two recorded links through the same native reference.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F4-C3b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F4",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Use a declared inverse, symmetric or subproperty meaning to interpret a reverse or equivalent transition.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F4-C3c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F4",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Consult native, machine-inspectable argument-type, domain/range or property-constraint declarations. A prose relation description alone is not this additional service.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F4-C3d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F4",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Retrieve a recorded assertion with a repeatable native locator.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F4-C4a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F4",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Retrieve assertion-associated attribution beyond the dataset’s general homepage.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F4-C4b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F4",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Retrieve a supplied rank, confidence or strength value with its documented interpretation.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F4-C4c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F4",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Select or inspect evidence using source/provenance or evidential-status metadata rather than the node label alone.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F4-C4d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C1",
        "family": "F5",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Distinguish a lexical meaning from the word form expressing it.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F5-C1a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C1",
        "family": "F5",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Represent named semantic participants or roles within that meaning.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F5-C1b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C1",
        "family": "F5",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Represent nested compositional semantic structure inside one lexical meaning.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F5-C1c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C1",
        "family": "F5",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Distinguish a named instance from a general lexical concept in the native semantic model.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2"
        ],
        "test_id": "F5-C1d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F5",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Locate native meanings from an English lexical expression.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F5-C2a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F5",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Use an explicit synonym/sense-equivalence grouping, not merely membership of the same situation frame.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F5-C2b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F5",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Retrieve meaning-bearing English gloss or structured semantic context for disambiguation.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F5-C2c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C2",
        "family": "F5",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Resolve a supplied identifier from an independent lexical or encyclopedic source to the native meaning.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R3",
          "R4"
        ],
        "test_id": "F5-C2d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F5",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Follow a documented semantic inheritance or hypernym relation.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F5-C3a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F5",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Follow a documented nonhierarchical semantic relation.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F5-C3b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F5",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Retain the declared relation direction and its inverse/symmetry convention.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F5-C3c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C3",
        "family": "F5",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Follow an explicit inter-frame participant correspondence rather than an untyped lexical association.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R2",
          "R3"
        ],
        "test_id": "F5-C3d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F5",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Retrieve a gloss, frame definition or compositional meaning attached to its native reference.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F5-C4a",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F5",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Retrieve a source-supplied English contextual usage example for a native lexical meaning.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F5-C4b",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F5",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Recover the upstream source/document or annotated corpus location supplying a description or example, beyond the output record’s own identifier.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F5-C4c",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      },
      {
        "criterion": "C4",
        "family": "F5",
        "no_rule": "The requested facility is absent from, or incompatible with, the explicitly bounded representation being assessed. This is not a claim of universal resource incapacity.",
        "obligation": "Retrieve source-defined entailment, inheritance or causative semantics supporting a limited inference rather than claiming arbitrary reasoning.",
        "pass_rule": "The declared source profile supplies the requested distinction/route, established by a specification and a checkable example or complete bounded representation. Mere ability to add a new field or external semantic model is insufficient.",
        "requirements": [
          "R1",
          "R2",
          "R3"
        ],
        "test_id": "F5-C4d",
        "unknown_rule": "A missing source, uninspected field or disputed interpretation is Unknown and is not converted to a zero score."
      }
    ],
    "title": "Family-specific native-service evidence audit",
    "interpretation": "Counts cover a fixed set of family-specific native-service requests. They are source-based conformance observations, not population coverage, operational accuracy or a universal capability scale.",
    "scope_policy": "Use the public content/profile identified for each candidate, together with its documented interpretation rules. No new semantic enrichment is credited. Documentation-level support is distinguished from an executed source-adapter benchmark.",
    "clarification_record": [
      "F2-C1b",
      "F2-C1c",
      "F4-C3d",
      "F5-C4b",
      "F5-C4c",
      "F1-C2d",
      "F2-C2d",
      "F3-C1d"
    ],
    "eligibility_boundary": "The numerical audit assumes the confirmed panel remains admitted for documentary comparison. It does not re-verify R5 permissions, freeze complete releases, or certify implementation eligibility.",
    "overlap_boundary": "F1-C2d and F1-C4d assess opposite access directions on shared assignment data. Related requests can share supporting features; equal contributions are an explicit value model, not proof of independent benefits."
  },
  "panel": [
    {
      "candidate_id": "F1-001",
      "family": "F1",
      "resource": "DDC",
      "profile": "DDC 22 public three-level summaries (2003), with their introductory reading rules; not full WebDewey",
      "boundary": "This is a finding about the freely cataloged summary, not about full DDC capability. An authorized full DDC profile must be rescored, not assumed equivalent.",
      "source_ids": [
        "D01"
      ]
    },
    {
      "candidate_id": "F1-002",
      "family": "F1",
      "resource": "LCC",
      "profile": "May 2024 public schedule texts; Q schedule and published table instructions as concrete witnesses",
      "boundary": "Witnesses establish types of native support, not completeness or average readability of all LCC schedules.",
      "source_ids": [
        "D02",
        "D03"
      ]
    },
    {
      "candidate_id": "F1-003",
      "family": "F1",
      "resource": "UDC",
      "profile": "Public UDC Summary with notes, auxiliary records and its published notation/combination rules",
      "boundary": "Only the declared Summary profile and its published rules are credited, not the full MRF. Nonhierarchical cross-referencing and a Summary-specific exclusion/redirect witness remain unresolved. Export delivery was not executed.",
      "source_ids": [
        "D04",
        "D05",
        "D06",
        "D07"
      ]
    },
    {
      "candidate_id": "F1-049",
      "family": "F1",
      "resource": "OpenAlex Topics",
      "profile": "Topic-object contract inspected 13 October 2026, including the published October 2026 fields",
      "boundary": "Documented API fields are assessed; no classifier accuracy, work coverage or live-query benchmark is claimed.",
      "source_ids": [
        "D08"
      ]
    },
    {
      "candidate_id": "F2-001",
      "family": "F2",
      "resource": "FAST",
      "profile": "FAST authority model and nine-facet rules in the October 2024 guide; authority/update fields",
      "boundary": "A source-supported field is not a claim that every FAST record populates it. Source-derived joint assignments are not invented from separate facets.",
      "source_ids": [
        "V01",
        "V02"
      ]
    },
    {
      "candidate_id": "F2-002",
      "family": "F2",
      "resource": "LCSH",
      "profile": "LCSH authority records plus MARC 21 subdivision and application rules",
      "boundary": "C2d concerns the full qualified-expression route, not a deliberately restricted lookup of already-established headings.",
      "source_ids": [
        "V03",
        "V04",
        "V05"
      ]
    },
    {
      "candidate_id": "F2-045",
      "family": "F2",
      "resource": "YSO",
      "profile": "YSO core English concept model inspected 13 October 2026; separate YSO places is not included",
      "boundary": "Separate part-whole support does not imply it exists on every concept. The weighting of that extra service is a sensitivity case.",
      "source_ids": [
        "V06",
        "V07",
        "V08"
      ]
    },
    {
      "candidate_id": "F3-001",
      "family": "F3",
      "resource": "SUMO",
      "profile": "Inspected Merge.kif branch with published WordNet 3.0 mappings; source profile dated 13 October 2026",
      "boundary": "Axiom availability and mapping presence are not reasoning accuracy or complete lexical coverage; mutable branches need pinning before implementation.",
      "source_ids": [
        "O01",
        "O02"
      ]
    },
    {
      "candidate_id": "F3-009",
      "family": "F3",
      "resource": "CCO",
      "profile": "CCO merged 2.2, version IRI 2026-08-13, including declared BFO imports",
      "boundary": "A textual definition containing “if” is not automatically an executable general rule; OWL constraints still receive their own credit.",
      "source_ids": [
        "O03"
      ]
    },
    {
      "candidate_id": "F3-029",
      "family": "F3",
      "resource": "FrameBase",
      "profile": "FrameBase 2.0 RDFS schema with its documented ReDer companion rules; no unverified instance integration",
      "boundary": "Do not silently omit ReDer rules to depress the score; no claim of general first-order expressiveness follows from including them.",
      "source_ids": [
        "O04",
        "O05",
        "O06"
      ]
    },
    {
      "candidate_id": "F4-001",
      "family": "F4",
      "resource": "DBpedia",
      "profile": "Mapping-based DBpedia ontology/core assertion model, with source/identity links; not arbitrary custom RDF extensions",
      "boundary": "This does not rate DBpedia factual error or deny separately available reified/extraction extensions.",
      "source_ids": [
        "G01",
        "G02"
      ]
    },
    {
      "candidate_id": "F4-002",
      "family": "F4",
      "resource": "Wikidata",
      "profile": "Full statement model inspected 13 October 2026; not the truthy-only RDF view",
      "boundary": "Documentation proves native field support, not complete sourcing, universal constraint compliance or factual correctness.",
      "source_ids": [
        "G03",
        "G04",
        "G05",
        "G06"
      ]
    },
    {
      "candidate_id": "F4-003",
      "family": "F4",
      "resource": "YAGO",
      "profile": "YAGO 4.6 published schema/facts/labels/meta/logs; inspected release samples and contract",
      "boundary": "One attribution request remains Unknown. No false zero or transferred 4.5 measurement is used; all possible completions are evaluated.",
      "source_ids": [
        "G07",
        "G08",
        "G11",
        "G10",
        "G09"
      ]
    },
    {
      "candidate_id": "F4-006",
      "family": "F4",
      "resource": "ATOMIC",
      "profile": "ATOMIC 2020 released symbolic head/relation/tail profile, excluding neural-generated expansions",
      "boundary": "Textual context is credited. The resource is not failed just because its nodes are phrases. Absence claims are restricted to the declared tuple record.",
      "source_ids": [
        "G12",
        "G13"
      ]
    },
    {
      "candidate_id": "F4-009",
      "family": "F4",
      "resource": "ConceptNet",
      "profile": "ConceptNet 5.7 assertion/API model with its documented relation vocabulary",
      "boundary": "The supported optional URI distinctions do not imply one unambiguous sense per node or a measured anchoring rate.",
      "source_ids": [
        "G14",
        "G15",
        "G16"
      ]
    },
    {
      "candidate_id": "F4-010",
      "family": "F4",
      "resource": "CSKG",
      "profile": "CSKG 1.0 cskg.tsv release and its published relation/source interpretation; no later confidence enrichment or embeddings credited",
      "boundary": "Source labels and provenance do not prove correct alignment or complete attribution on every edge. The assessed TSV has no assertion weight/confidence column; source overlap is explicit.",
      "source_ids": [
        "G17",
        "G18",
        "G15",
        "G16",
        "G19"
      ]
    },
    {
      "candidate_id": "F5-001",
      "family": "F5",
      "resource": "BabelNet",
      "profile": "Published API v9/V5_3 example model: synsets, sense sources, glosses, examples and edge pointers; no account execution",
      "boundary": "This audits the published response contract, not actual API coverage or access authorization. Richer multilingual size earns no separate points.",
      "source_ids": [
        "L01",
        "L02",
        "L09"
      ]
    },
    {
      "candidate_id": "F5-002",
      "family": "F5",
      "resource": "FrameNet",
      "profile": "Berkeley FrameNet 1.7 native lexical-unit, frame, FE, relation and annotation model",
      "boundary": "Syntactic parsing performance and general reasoning success are not inferred from annotated examples.",
      "source_ids": [
        "L03",
        "L04"
      ]
    },
    {
      "candidate_id": "F5-003",
      "family": "F5",
      "resource": "HowNet / OpenHowNet",
      "profile": "OpenHowNet core dictionary and sememe relations; separate BabelNet-annotation extension is reported but not merged into the core profile",
      "boundary": "The public Advanced BabelNet extension is not denied. Its inclusion would define a different, explicitly expanded assessment profile that must be rerun.",
      "source_ids": [
        "L05"
      ]
    },
    {
      "candidate_id": "F5-014",
      "family": "F5",
      "resource": "WordNet",
      "profile": "Princeton WordNet 3.0 native sense/synset, pointer and gloss model",
      "boundary": "No external mappings or FrameNet role alignments are imported to make the native core score higher.",
      "source_ids": [
        "L06",
        "L07",
        "L08"
      ]
    }
  ],
  "sources": {
    "R01": {
      "source_id": "R01",
      "title": "Original local family-selection outline (public counterpart linked)",
      "url": "local:../Supplementary_S2_Family_Representatives.docx",
      "locator": "Original outline, pp. 1–10, for the organization and R1–R5. The linked public S2 reports the resulting protocol and evidence.",
      "access_date": "2026-10-13"
    },
    "R02": {
      "source_id": "R02",
      "title": "Original local 20-resource panel (public counterpart linked)",
      "url": "local:../../s1/Supplementary_S1_Resource_Screening.docx",
      "locator": "Original panel table 2 supplies the 20 IDs and five families. The linked public S1 reports that selection.",
      "access_date": "2026-10-13"
    },
    "M01": {
      "source_id": "M01",
      "title": "Lahdelma and Salminen (2001), SMAA-2",
      "url": "https://pubsonline.informs.org/doi/10.1287/opre.49.3.444.11220",
      "locator": "Rank acceptability and preference uncertainty; the particular score model is study-defined",
      "access_date": "2026-10-13"
    },
    "M02": {
      "source_id": "M02",
      "title": "NumPy Generator.dirichlet",
      "url": "https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.dirichlet.html",
      "locator": "Dirichlet sampling; direct normalized-Gamma construction",
      "access_date": "2026-10-13"
    },
    "M03": {
      "source_id": "M03",
      "title": "Kaggle Python environment",
      "url": "https://github.com/Kaggle/docker-python",
      "locator": "Python notebook environment; Kaggle-service execution is not claimed",
      "access_date": "2026-10-13"
    },
    "M04": {
      "source_id": "M04",
      "title": "SKOS Reference",
      "url": "https://www.w3.org/TR/skos-reference/",
      "locator": "Concept labels, semantic relations, documentation and mappings",
      "access_date": "2026-10-13"
    },
    "M05": {
      "source_id": "M05",
      "title": "OWL 2 Primer",
      "url": "https://www.w3.org/TR/owl2-primer/",
      "locator": "Classes, restrictions, properties and logical interpretation",
      "access_date": "2026-10-13"
    },
    "M06": {
      "source_id": "M06",
      "title": "KGTK data model",
      "url": "https://kgtk.readthedocs.io/en/latest/data_model/",
      "locator": "Native distinctions must survive the common graph adapter",
      "access_date": "2026-10-13"
    },
    "D01": {
      "source_id": "D01",
      "title": "OCLC DDC 22 Summaries (2003)",
      "url": "https://www.oclc.org/content/dam/oclc/dewey/resources/summaries/deweysummaries.pdf",
      "locator": "PDF pages 3–6: introduction; pages 9–20: the three-level summaries; no full schedules/tables/index",
      "access_date": "2026-10-13"
    },
    "D02": {
      "source_id": "D02",
      "title": "Library of Congress free LCC schedules",
      "url": "https://www.loc.gov/aba/publications/FreeLCC/freelcc.html",
      "locator": "May 2024 schedule texts; the subscription service is outside the assessed profile",
      "access_date": "2026-10-13"
    },
    "D03": {
      "source_id": "D03",
      "title": "LCC Q schedule (May 2024)",
      "url": "https://www.loc.gov/aba/publications/FreeLCC/LCC_Q2024TEXT.pdf",
      "locator": "Q175 social-aspect scope, QA76.76.W56 redirect, QL514.8815 Table Q3, QL69 Table Q6",
      "access_date": "2026-10-13"
    },
    "D04": {
      "source_id": "D04",
      "title": "UDC Summary export specification",
      "url": "https://udcsummary.info/exports.htm",
      "locator": "Complete text export includes notes and examples; request-based acquisition is not claimed completed",
      "access_date": "2026-10-13"
    },
    "D05": {
      "source_id": "D05",
      "title": "UDC notation",
      "url": "https://udcc.org/index.php/site/page?view=about_notation",
      "locator": "Syntactically expressive notation; published polar-bear/metabolism/time construction",
      "access_date": "2026-10-13"
    },
    "D06": {
      "source_id": "D06",
      "title": "UDC Summary",
      "url": "https://udcsummary.info/about.htm",
      "locator": "Main, common auxiliary and special auxiliary numbers; MRF 2011 / August 2012 identification, not a current-full-MRF claim",
      "access_date": "2026-10-13"
    },
    "D07": {
      "source_id": "D07",
      "title": "UDC structure and tables",
      "url": "https://udcc.org/index.php/site/page?view=about_structure",
      "locator": "Combination signs, auxiliaries and reference functions",
      "access_date": "2026-10-13"
    },
    "D08": {
      "source_id": "D08",
      "title": "OpenAlex topic model",
      "url": "https://help.openalex.org/data/topics/",
      "locator": "Documentation inspected 13 October 2026: IDs, description, keywords, hierarchy, works_api_url; siblings are hierarchical peers",
      "access_date": "2026-10-13"
    },
    "V01": {
      "source_id": "V01",
      "title": "OCLC FAST Quick Start Guide (October 2024)",
      "url": "https://www.oclc.org/content/dam/oclc/fast/FAST-quick-start-guide-2022.pdf",
      "locator": "Printed pages 2 and 11–16: nine facets, native record comparison and within-topical precoordination",
      "access_date": "2026-10-13"
    },
    "V02": {
      "source_id": "V02",
      "title": "FAST download and update records",
      "url": "https://www.oclc.org/research/areas/data-science/fast/download.html",
      "locator": "Authority distributions and change records; not all records are assumed to have a note",
      "access_date": "2026-10-13"
    },
    "V03": {
      "source_id": "V03",
      "title": "LCSH training, Module 2.1",
      "url": "https://www.loc.gov/catworkshop/lcsh/PDF%20scripts/2-1-Structural-Overview.pdf",
      "locator": "Printed pages 4–11 and 16–32; Literature record sh85077507, UF/BT/RT/notes",
      "access_date": "2026-10-13"
    },
    "V04": {
      "source_id": "V04",
      "title": "MARC 21 Authority 150",
      "url": "https://www.loc.gov/marc/authority/ad150.html",
      "locator": "Topical term with x/y/z/v subdivisions; role and order are encoded",
      "access_date": "2026-10-13"
    },
    "V05": {
      "source_id": "V05",
      "title": "MARC 21 Authority contents",
      "url": "https://www.loc.gov/marc/authority/ecadhome.html",
      "locator": "005, 040, 450, 550, 670, 680 and 008; source and status fields",
      "access_date": "2026-10-13"
    },
    "V06": {
      "source_id": "V06",
      "title": "YSO official description",
      "url": "https://finto.fi/yso/en/",
      "locator": "Core YSO, including English; YSO places is separate; part-whole links, equivalence sources, concept collections",
      "access_date": "2026-10-13"
    },
    "V07": {
      "source_id": "V07",
      "title": "YSO dogmatism concept",
      "url": "https://finto.fi/yso/en/page/p290",
      "locator": "Qualified concept record; English label and source/hierarchy/context, where supplied",
      "access_date": "2026-10-13"
    },
    "V08": {
      "source_id": "V08",
      "title": "YSO percussion-instrument concept",
      "url": "https://finto.fi/yso/en/page/p441",
      "locator": "Broader/narrower references and concept metadata; source-record inspection",
      "access_date": "2026-10-13"
    },
    "O01": {
      "source_id": "O01",
      "title": "SUMO Merge.kif",
      "url": "https://raw.githubusercontent.com/ontologyportal/sumo/master/Merge.kif",
      "locator": "Inspected branch on 13 October 2026: CaseRole, TransitiveRelation, subclass, documentation, termFormat; not commit-pinned",
      "access_date": "2026-10-13"
    },
    "O02": {
      "source_id": "O02",
      "title": "SUMO WordNet 3.0 mappings",
      "url": "https://raw.githubusercontent.com/ontologyportal/sumo/master/WordNetMappings/WordNetMappings30-adv.txt",
      "locator": "Header defines = / + / @ and complements; offset 00001740 maps to AcapellaMusic; 00002436 maps to On",
      "access_date": "2026-10-13"
    },
    "O03": {
      "source_id": "O03",
      "title": "CCO 2.2 merged ontology",
      "url": "https://raw.githubusercontent.com/CommonCoreOntology/CommonCoreOntologies/develop/src/cco-merged/CommonCoreOntologiesMerged.ttl",
      "locator": "Version IRI 2026-08-13; altLabel, restrictions, inverseOf, propertyChainAxiom, definition-source annotations; no source snapshot captured",
      "access_date": "2026-10-13"
    },
    "O04": {
      "source_id": "O04",
      "title": "FrameBase schema",
      "url": "https://www.framebase.org/schema",
      "locator": "RDFS core, microframes, near-equivalence, source IDs and reversible 2.0 IRI grammar; some illustrations use 1.x IRIs",
      "access_date": "2026-10-13"
    },
    "O05": {
      "source_id": "O05",
      "title": "FrameBase ReDer rules",
      "url": "https://www.framebase.org/reder",
      "locator": "Separating frame roles and isPartitionedIntoParts definite-clause example; included as published companion rules",
      "access_date": "2026-10-13"
    },
    "O06": {
      "source_id": "O06",
      "title": "FrameBase data releases",
      "url": "https://www.framebase.org/data",
      "locator": "2.0 schema and companion rule descriptions; no credit for unrelated instance endpoint",
      "access_date": "2026-10-13"
    },
    "G01": {
      "source_id": "G01",
      "title": "DBpedia ontology",
      "url": "https://www.dbpedia.org/resources/ontology/",
      "locator": "Mapping-based ontology profile, class hierarchy and properties; not an arbitrary RDF language envelope",
      "access_date": "2026-10-13"
    },
    "G02": {
      "source_id": "G02",
      "title": "DBpedia Berlin record",
      "url": "https://dbpedia.org/page/Berlin",
      "locator": "Named entity, labels/abstract/type, sameAs and supplying encyclopedia-page route",
      "access_date": "2026-10-13"
    },
    "G03": {
      "source_id": "G03",
      "title": "Wikidata statement model",
      "url": "https://www.wikidata.org/wiki/Help:Statements",
      "locator": "Statements, ranks, references, qualifiers, no-value and unknown-value; Marie Curie and value-state examples",
      "access_date": "2026-10-13"
    },
    "G04": {
      "source_id": "G04",
      "title": "Wikidata qualifiers",
      "url": "https://www.wikidata.org/wiki/Help:Qualifiers",
      "locator": "Population and time; qualifiers apply to a statement, not simply to the subject",
      "access_date": "2026-10-13"
    },
    "G05": {
      "source_id": "G05",
      "title": "Wikidata property constraints",
      "url": "https://www.wikidata.org/wiki/Help:Property_constraints_portal",
      "locator": "Native constraint statements; constraints do not guarantee truth or compliance",
      "access_date": "2026-10-13"
    },
    "G06": {
      "source_id": "G06",
      "title": "Wikidata sources",
      "url": "https://www.wikidata.org/wiki/Help:Sources",
      "locator": "Reference properties, source URLs/items and retrieval dates; many individual claims remain unsourced",
      "access_date": "2026-10-13"
    },
    "G07": {
      "source_id": "G07",
      "title": "YAGO 4.6 release",
      "url": "https://yago-knowledge.org/downloads/yago-4-6",
      "locator": "4.6 schema, facts, labels, RDF-star meta and excluded-statement logs; no transfer from 4.5 without checking",
      "access_date": "2026-10-13"
    },
    "G08": {
      "source_id": "G08",
      "title": "YAGO 4.6 metadata sample",
      "url": "https://yago-knowledge.org/data/yago4.6/samples/meta.txt",
      "locator": "Belgium population/onDate and George Washington startDate/endDate statement annotations",
      "access_date": "2026-10-13"
    },
    "G09": {
      "source_id": "G09",
      "title": "YAGO 4.6 schema sample",
      "url": "https://yago-knowledge.org/data/yago4.6/samples/schema.txt",
      "locator": "SHACL and property declarations in the release",
      "access_date": "2026-10-13"
    },
    "G10": {
      "source_id": "G10",
      "title": "YAGO 4.6 labels sample",
      "url": "https://yago-knowledge.org/data/yago4.6/samples/labels.txt",
      "locator": "Label, alternateName, descriptions and sameAs/source identity links",
      "access_date": "2026-10-13"
    },
    "G11": {
      "source_id": "G11",
      "title": "YAGO 4.6 excluded-statement sample",
      "url": "https://yago-knowledge.org/data/yago4.6/samples/logs.txt",
      "locator": "Log status describes rejected source statements, not accepted negative assertions",
      "access_date": "2026-10-13"
    },
    "G12": {
      "source_id": "G12",
      "title": "ATOMIC 2020 author paper",
      "url": "https://arxiv.org/html/2010.05953",
      "locator": "Released textual head/relation/tail model; relation inventory including NotDesires and temporal relations; source construction",
      "access_date": "2026-10-13"
    },
    "G13": {
      "source_id": "G13",
      "title": "ATOMIC 2020 release repository",
      "url": "https://github.com/allenai/comet-atomic-2020",
      "locator": "Published symbolic tuple resource, separate from generated COMET outputs",
      "access_date": "2026-10-13"
    },
    "G14": {
      "source_id": "G14",
      "title": "ConceptNet API model",
      "url": "https://github.com/commonsense/conceptnet5/wiki/API",
      "locator": "Node/sense URIs, sources, dataset, surfaceText, weight and assertion records",
      "access_date": "2026-10-13"
    },
    "G15": {
      "source_id": "G15",
      "title": "ConceptNet relation definitions",
      "url": "https://github.com/commonsense/conceptnet5/wiki/Relations",
      "locator": "Synonym, ExternalURL, PartOf, UsedFor, NotDesires and their intended meanings",
      "access_date": "2026-10-13"
    },
    "G16": {
      "source_id": "G16",
      "title": "ConceptNet relation symmetry declarations",
      "url": "https://raw.githubusercontent.com/commonsense/conceptnet5/master/conceptnet5/relations.py",
      "locator": "SYMMETRIC_RELATIONS and negative relation names; source interpretation, not empirical path accuracy",
      "access_date": "2026-10-13"
    },
    "G17": {
      "source_id": "G17",
      "title": "CSKG representation",
      "url": "https://cskg.readthedocs.io/en/latest/representation/",
      "locator": "Released columns and keys–piano–music join example; labels/sources may be empty",
      "access_date": "2026-10-13"
    },
    "G18": {
      "source_id": "G18",
      "title": "CSKG release repository",
      "url": "https://github.com/usc-isi-i2/cskg",
      "locator": "Integrated seven sources; creation and source mappings. Embedding files are not assertion-confidence scores.",
      "access_date": "2026-10-13"
    },
    "L01": {
      "source_id": "L01",
      "title": "BabelNet API guide",
      "url": "https://babelnet.org/guide",
      "locator": "Inspected v9 interface; published response version V5_3, synset types, sources, senses, glosses, examples and edge pointers; no API session executed",
      "access_date": "2026-10-13"
    },
    "L02": {
      "source_id": "L02",
      "title": "BabelNet construction and source description",
      "url": "https://babelnet.org/about",
      "locator": "Lexical/encyclopedic sources and their attribution; account authorization is not implied",
      "access_date": "2026-10-13"
    },
    "L03": {
      "source_id": "L03",
      "title": "FrameNet reader documentation",
      "url": "https://www.nltk.org/howto/framenet.html",
      "locator": "FrameNet 1.7 native frame, lexical-unit, FE, relation and sentence/corpus records; documentation examples, not locally run reader",
      "access_date": "2026-10-13"
    },
    "L04": {
      "source_id": "L04",
      "title": "Global FrameNet description",
      "url": "https://www.globalframenet.org/",
      "locator": "Frames represent scenes; inter-frame semantic relationships; native FrameNet rather than the wider multilingual project is assessed",
      "access_date": "2026-10-13"
    },
    "L05": {
      "source_id": "L05",
      "title": "OpenHowNet core dictionary and examples",
      "url": "https://github.com/thunlp/OpenHowNet",
      "locator": "Basic core: No.244401 sememe tree, SpeBrand examples, E_E field, sememe relations. Separately described BabelNet extension is not silently merged",
      "access_date": "2026-10-13"
    },
    "L06": {
      "source_id": "L06",
      "title": "Princeton WordNet database specification",
      "url": "https://wordnet.princeton.edu/documentation/wndb5wn",
      "locator": "WordNet 3.0 offsets, words, pointers, syntactic verb frames and glosses",
      "access_date": "2026-10-13"
    },
    "L07": {
      "source_id": "L07",
      "title": "WordNet relation and sense examples",
      "url": "https://www.nltk.org/howto/wordnet.html",
      "locator": "dog.n.01/car synsets; instance pointers, entailment, usage examples and sense keys",
      "access_date": "2026-10-13"
    },
    "L08": {
      "source_id": "L08",
      "title": "WordNet glossary",
      "url": "https://wordnet.princeton.edu/documentation/wngloss7wn",
      "locator": "Synset, lexical/semantic relation, instance, entailment and usage-example definitions",
      "access_date": "2026-10-13"
    },
    "G19": {
      "source_id": "G19",
      "title": "CSKG 1.0 archived release",
      "url": "https://zenodo.org/records/4331372",
      "locator": "Published 17 December 2020: cskg.tsv.gz and cskg_star.tsv.gz; embedding files are separate. The selected graph contract does not include weights.",
      "access_date": "2026-10-13"
    },
    "L09": {
      "source_id": "L09",
      "title": "BabelNet 5.3 BabelPointer API",
      "url": "https://babelnet.org/javadoc/5.3/it/uniroma1/lcl/babelnet/data/BabelPointer.html",
      "locator": "Typed lexical/semantic pointer enumeration; not evidence that every pointer is instantiated in every synset.",
      "access_date": "2026-10-13"
    },
    "M07": {
      "source_id": "M07",
      "title": "NumPy random-number compatibility policy",
      "url": "https://numpy.org/doc/stable/reference/random/compatibility.html",
      "locator": "Same-stream conditions require the same generator, calls, build and environment; a fixed seed alone is insufficient.",
      "access_date": "2026-10-13"
    }
  },
  "audit": [
    {
      "candidate_id": "F1-001",
      "family": "F1",
      "criterion": "C1",
      "test_id": "F1-C1a",
      "result": 1,
      "observed": "Class 636 has a stable notation in the numbered summary.",
      "source_ids": [
        "D01"
      ],
      "profile": "DDC 22 public three-level summaries (2003), with their introductory reading rules; not full WebDewey",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-001",
      "family": "F1",
      "criterion": "C1",
      "test_id": "F1-C1b",
      "result": 1,
      "observed": "600→630→636 is explicit in the introductory hierarchy.",
      "source_ids": [
        "D01"
      ],
      "profile": "DDC 22 public three-level summaries (2003), with their introductory reading rules; not full WebDewey",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-001",
      "family": "F1",
      "criterion": "C1",
      "test_id": "F1-C1c",
      "result": 0,
      "observed": "The public summary omits the schedules/add tables needed to construct and decode a general combined subject; the introduction describes, but does not supply, them.",
      "source_ids": [
        "D01"
      ],
      "profile": "DDC 22 public three-level summaries (2003), with their introductory reading rules; not full WebDewey",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-001",
      "family": "F1",
      "criterion": "C1",
      "test_id": "F1-C1d",
      "result": 0,
      "observed": "The data profile contains fixed summary captions, not the numbered auxiliary tables needed to construct independent qualifiers.",
      "source_ids": [
        "D01"
      ],
      "profile": "DDC 22 public three-level summaries (2003), with their introductory reading rules; not full WebDewey",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-001",
      "family": "F1",
      "criterion": "C2",
      "test_id": "F1-C2a",
      "result": 1,
      "observed": "Caption-to-code lookup is possible in the three-level schedule.",
      "source_ids": [
        "D01"
      ],
      "profile": "DDC 22 public three-level summaries (2003), with their introductory reading rules; not full WebDewey",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-001",
      "family": "F1",
      "criterion": "C2",
      "test_id": "F1-C2b",
      "result": 0,
      "observed": "A separate Relative Index is identified as part of the full edition, but is not part of this public profile.",
      "source_ids": [
        "D01"
      ],
      "profile": "DDC 22 public three-level summaries (2003), with their introductory reading rules; not full WebDewey",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-001",
      "family": "F1",
      "criterion": "C2",
      "test_id": "F1-C2c",
      "result": 1,
      "observed": "The introduction distinguishes disciplinary readings of clothing; hierarchical context is retained.",
      "source_ids": [
        "D01"
      ],
      "profile": "DDC 22 public three-level summaries (2003), with their introductory reading rules; not full WebDewey",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-001",
      "family": "F1",
      "criterion": "C2",
      "test_id": "F1-C2d",
      "result": 0,
      "observed": "The assessed summary does not include individual bibliographic assignment records from which to recover a subject reference.",
      "source_ids": [
        "D01"
      ],
      "profile": "DDC 22 public three-level summaries (2003), with their introductory reading rules; not full WebDewey",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-001",
      "family": "F1",
      "criterion": "C3",
      "test_id": "F1-C3a",
      "result": 1,
      "observed": "Parent context is defined for the three supplied levels.",
      "source_ids": [
        "D01"
      ],
      "profile": "DDC 22 public three-level summaries (2003), with their introductory reading rules; not full WebDewey",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-001",
      "family": "F1",
      "criterion": "C3",
      "test_id": "F1-C3b",
      "result": 1,
      "observed": "The published 600→630→636 route has a defined intermediate class.",
      "source_ids": [
        "D01"
      ],
      "profile": "DDC 22 public three-level summaries (2003), with their introductory reading rules; not full WebDewey",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-001",
      "family": "F1",
      "criterion": "C3",
      "test_id": "F1-C3c",
      "result": 0,
      "observed": "The actual summary entries are code/caption lists; references described for the full schedules are not provided here.",
      "source_ids": [
        "D01"
      ],
      "profile": "DDC 22 public three-level summaries (2003), with their introductory reading rules; not full WebDewey",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-001",
      "family": "F1",
      "criterion": "C3",
      "test_id": "F1-C3d",
      "result": 0,
      "observed": "No general compound-to-components record is supplied by the three-level profile.",
      "source_ids": [
        "D01"
      ],
      "profile": "DDC 22 public three-level summaries (2003), with their introductory reading rules; not full WebDewey",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-001",
      "family": "F1",
      "criterion": "C4",
      "test_id": "F1-C4a",
      "result": 1,
      "observed": "A class returns its caption and broader summary context.",
      "source_ids": [
        "D01"
      ],
      "profile": "DDC 22 public three-level summaries (2003), with their introductory reading rules; not full WebDewey",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-001",
      "family": "F1",
      "criterion": "C4",
      "test_id": "F1-C4b",
      "result": 0,
      "observed": "The three-level entries are abridged browsing captions, not full class-specific scope-note records.",
      "source_ids": [
        "D01"
      ],
      "profile": "DDC 22 public three-level summaries (2003), with their introductory reading rules; not full WebDewey",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-001",
      "family": "F1",
      "criterion": "C4",
      "test_id": "F1-C4c",
      "result": 0,
      "observed": "Full schedule redirects/exclusion instructions for individual subject classes are outside the summary profile.",
      "source_ids": [
        "D01"
      ],
      "profile": "DDC 22 public three-level summaries (2003), with their introductory reading rules; not full WebDewey",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-001",
      "family": "F1",
      "criterion": "C4",
      "test_id": "F1-C4d",
      "result": 0,
      "observed": "The summary supplies no linked document-assignment records.",
      "source_ids": [
        "D01"
      ],
      "profile": "DDC 22 public three-level summaries (2003), with their introductory reading rules; not full WebDewey",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-002",
      "family": "F1",
      "criterion": "C1",
      "test_id": "F1-C1a",
      "result": 1,
      "observed": "Q/QA/QL notations identify schedule entries.",
      "source_ids": [
        "D02",
        "D03"
      ],
      "profile": "May 2024 public schedule texts; Q schedule and published table instructions as concrete witnesses",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-002",
      "family": "F1",
      "criterion": "C1",
      "test_id": "F1-C1b",
      "result": 1,
      "observed": "Indented Q/QA/QA76 context locates each subdivision.",
      "source_ids": [
        "D02",
        "D03"
      ],
      "profile": "May 2024 public schedule texts; Q schedule and published table instructions as concrete witnesses",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-002",
      "family": "F1",
      "criterion": "C1",
      "test_id": "F1-C1c",
      "result": 0,
      "observed": "The enumerated schedule/table model does not supply a general operator for independently combining two subject classmarks.",
      "source_ids": [
        "D02",
        "D03"
      ],
      "profile": "May 2024 public schedule texts; Q schedule and published table instructions as concrete witnesses",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-002",
      "family": "F1",
      "criterion": "C1",
      "test_id": "F1-C1d",
      "result": 1,
      "observed": "QL514.8815 and Table Q3 distinguish regional subdivision; QL69.A3–Z uses a country subarrangement.",
      "source_ids": [
        "D02",
        "D03"
      ],
      "profile": "May 2024 public schedule texts; Q schedule and published table instructions as concrete witnesses",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-002",
      "family": "F1",
      "criterion": "C2",
      "test_id": "F1-C2a",
      "result": 1,
      "observed": "English schedule captions support deterministic caption lookup.",
      "source_ids": [
        "D02",
        "D03"
      ],
      "profile": "May 2024 public schedule texts; Q schedule and published table instructions as concrete witnesses",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-002",
      "family": "F1",
      "criterion": "C2",
      "test_id": "F1-C2b",
      "result": 1,
      "observed": "Notes and see references provide additional access wording; QA76.76.W56 separates window functionality from named operating systems.",
      "source_ids": [
        "D02",
        "D03"
      ],
      "profile": "May 2024 public schedule texts; Q schedule and published table instructions as concrete witnesses",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-002",
      "family": "F1",
      "criterion": "C2",
      "test_id": "F1-C2c",
      "result": 1,
      "observed": "Scope and redirect notes distinguish alternative subject placements.",
      "source_ids": [
        "D02",
        "D03"
      ],
      "profile": "May 2024 public schedule texts; Q schedule and published table instructions as concrete witnesses",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-002",
      "family": "F1",
      "criterion": "C2",
      "test_id": "F1-C2d",
      "result": 0,
      "observed": "The assessed schedule texts do not include individual class-to-item assignment records for an incoming record-to-subject lookup.",
      "source_ids": [
        "D02",
        "D03"
      ],
      "profile": "May 2024 public schedule texts; Q schedule and published table instructions as concrete witnesses",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-002",
      "family": "F1",
      "criterion": "C3",
      "test_id": "F1-C3a",
      "result": 1,
      "observed": "Indentation and schedule headings determine immediate broader context.",
      "source_ids": [
        "D02",
        "D03"
      ],
      "profile": "May 2024 public schedule texts; Q schedule and published table instructions as concrete witnesses",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-002",
      "family": "F1",
      "criterion": "C3",
      "test_id": "F1-C3b",
      "result": 1,
      "observed": "Q→QA→QA76 is navigable by the declared schedule context.",
      "source_ids": [
        "D02",
        "D03"
      ],
      "profile": "May 2024 public schedule texts; Q schedule and published table instructions as concrete witnesses",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-002",
      "family": "F1",
      "criterion": "C3",
      "test_id": "F1-C3c",
      "result": 1,
      "observed": "Q175 social-aspect and QA76.76.W56 entries direct readers to different schedule locations.",
      "source_ids": [
        "D02",
        "D03"
      ],
      "profile": "May 2024 public schedule texts; Q schedule and published table instructions as concrete witnesses",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-002",
      "family": "F1",
      "criterion": "C3",
      "test_id": "F1-C3d",
      "result": 0,
      "observed": "A general binary compound decomposer is not part of the enumerated schedule profile.",
      "source_ids": [
        "D02",
        "D03"
      ],
      "profile": "May 2024 public schedule texts; Q schedule and published table instructions as concrete witnesses",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-002",
      "family": "F1",
      "criterion": "C4",
      "test_id": "F1-C4a",
      "result": 1,
      "observed": "The schedule returns an identified entry with surrounding class context.",
      "source_ids": [
        "D02",
        "D03"
      ],
      "profile": "May 2024 public schedule texts; Q schedule and published table instructions as concrete witnesses",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-002",
      "family": "F1",
      "criterion": "C4",
      "test_id": "F1-C4b",
      "result": 1,
      "observed": "Q175 social-aspect notes delimit the intended subject treatment.",
      "source_ids": [
        "D02",
        "D03"
      ],
      "profile": "May 2024 public schedule texts; Q schedule and published table instructions as concrete witnesses",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-002",
      "family": "F1",
      "criterion": "C4",
      "test_id": "F1-C4c",
      "result": 1,
      "observed": "The Windows entry distinguishes a functionality class from individual operating-system classes.",
      "source_ids": [
        "D02",
        "D03"
      ],
      "profile": "May 2024 public schedule texts; Q schedule and published table instructions as concrete witnesses",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-002",
      "family": "F1",
      "criterion": "C4",
      "test_id": "F1-C4d",
      "result": 0,
      "observed": "The schedule is not a collection of item-assignment records.",
      "source_ids": [
        "D02",
        "D03"
      ],
      "profile": "May 2024 public schedule texts; Q schedule and published table instructions as concrete witnesses",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-003",
      "family": "F1",
      "criterion": "C1",
      "test_id": "F1-C1a",
      "result": 1,
      "observed": "Main and auxiliary notations identify native subjects.",
      "source_ids": [
        "D04",
        "D05",
        "D06",
        "D07"
      ],
      "profile": "Public UDC Summary with notes, auxiliary records and its published notation/combination rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-003",
      "family": "F1",
      "criterion": "C1",
      "test_id": "F1-C1b",
      "result": 1,
      "observed": "Decimal structure determines the broader context of a class.",
      "source_ids": [
        "D04",
        "D05",
        "D06",
        "D07"
      ],
      "profile": "Public UDC Summary with notes, auxiliary records and its published notation/combination rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-003",
      "family": "F1",
      "criterion": "C1",
      "test_id": "F1-C1c",
      "result": 1,
      "observed": "Published connecting operators and their interpretation combine subject numbers.",
      "source_ids": [
        "D04",
        "D05",
        "D06",
        "D07"
      ],
      "profile": "Public UDC Summary with notes, auxiliary records and its published notation/combination rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-003",
      "family": "F1",
      "criterion": "C1",
      "test_id": "F1-C1d",
      "result": 1,
      "observed": "The notation example distinguishes a main subject, an auxiliary concept and an explicit time expression.",
      "source_ids": [
        "D04",
        "D05",
        "D06",
        "D07"
      ],
      "profile": "Public UDC Summary with notes, auxiliary records and its published notation/combination rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-003",
      "family": "F1",
      "criterion": "C2",
      "test_id": "F1-C2a",
      "result": 1,
      "observed": "The English Summary offers caption-to-class access.",
      "source_ids": [
        "D04",
        "D05",
        "D06",
        "D07"
      ],
      "profile": "Public UDC Summary with notes, auxiliary records and its published notation/combination rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-003",
      "family": "F1",
      "criterion": "C2",
      "test_id": "F1-C2b",
      "result": 1,
      "observed": "Its declared full text exports include notes and examples as lexical/contextual cues, unlike caption-only exports.",
      "source_ids": [
        "D04",
        "D05",
        "D06",
        "D07"
      ],
      "profile": "Public UDC Summary with notes, auxiliary records and its published notation/combination rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-003",
      "family": "F1",
      "criterion": "C2",
      "test_id": "F1-C2c",
      "result": 1,
      "observed": "Main and auxiliary contexts distinguish readings of a notation and its caption.",
      "source_ids": [
        "D04",
        "D05",
        "D06",
        "D07"
      ],
      "profile": "Public UDC Summary with notes, auxiliary records and its published notation/combination rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-003",
      "family": "F1",
      "criterion": "C2",
      "test_id": "F1-C2d",
      "result": 0,
      "observed": "External catalog assignments are not included in the selected Summary profile; planned mappings are not an incoming assignment dataset.",
      "source_ids": [
        "D04",
        "D05",
        "D06",
        "D07"
      ],
      "profile": "Public UDC Summary with notes, auxiliary records and its published notation/combination rules",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-003",
      "family": "F1",
      "criterion": "C3",
      "test_id": "F1-C3a",
      "result": 1,
      "observed": "Decimal reading rules identify immediate hierarchy.",
      "source_ids": [
        "D04",
        "D05",
        "D06",
        "D07"
      ],
      "profile": "Public UDC Summary with notes, auxiliary records and its published notation/combination rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-003",
      "family": "F1",
      "criterion": "C3",
      "test_id": "F1-C3b",
      "result": 1,
      "observed": "The notation guide explicitly gives a multi-level zoological hierarchy.",
      "source_ids": [
        "D04",
        "D05",
        "D06",
        "D07"
      ],
      "profile": "Public UDC Summary with notes, auxiliary records and its published notation/combination rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-003",
      "family": "F1",
      "criterion": "C3",
      "test_id": "F1-C3c",
      "result": null,
      "observed": "General UDC documentation describes linked subjects, but a concrete nonhierarchical class cross-reference in the selected Summary was not retrieved in this review. Treat this profile-level service as Unknown, not as confirmed absence or support.",
      "source_ids": [
        "D04",
        "D05",
        "D06",
        "D07"
      ],
      "profile": "Public UDC Summary with notes, auxiliary records and its published notation/combination rules",
      "evidence_kind": "unresolved_documentary_evidence",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-003",
      "family": "F1",
      "criterion": "C3",
      "test_id": "F1-C3d",
      "result": 1,
      "observed": "Explicit notation boundaries allow a compound to be decomposed into source subject/auxiliary components.",
      "source_ids": [
        "D04",
        "D05",
        "D06",
        "D07"
      ],
      "profile": "Public UDC Summary with notes, auxiliary records and its published notation/combination rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-003",
      "family": "F1",
      "criterion": "C4",
      "test_id": "F1-C4a",
      "result": 1,
      "observed": "Identified class content and hierarchy are retained.",
      "source_ids": [
        "D04",
        "D05",
        "D06",
        "D07"
      ],
      "profile": "Public UDC Summary with notes, auxiliary records and its published notation/combination rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-003",
      "family": "F1",
      "criterion": "C4",
      "test_id": "F1-C4b",
      "result": 1,
      "observed": "The full Summary text profile includes notes and examples; caption-only export is not credited with them.",
      "source_ids": [
        "D04",
        "D05",
        "D06",
        "D07"
      ],
      "profile": "Public UDC Summary with notes, auxiliary records and its published notation/combination rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-003",
      "family": "F1",
      "criterion": "C4",
      "test_id": "F1-C4c",
      "result": null,
      "observed": "General UDC application and auxiliary rules explain composition, but the cited material does not identify a concrete redirection or exclusion instruction for a competing classification in the selected Summary. This service remains unresolved; no absence is inferred from an inaccessible page.",
      "source_ids": [
        "D04",
        "D05",
        "D06",
        "D07"
      ],
      "profile": "Public UDC Summary with notes, auxiliary records and its published notation/combination rules",
      "evidence_kind": "unresolved_source_scope",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-003",
      "family": "F1",
      "criterion": "C4",
      "test_id": "F1-C4d",
      "result": 0,
      "observed": "No document-assignment table is included in the assessed Summary.",
      "source_ids": [
        "D04",
        "D05",
        "D06",
        "D07"
      ],
      "profile": "Public UDC Summary with notes, auxiliary records and its published notation/combination rules",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-049",
      "family": "F1",
      "criterion": "C1",
      "test_id": "F1-C1a",
      "result": 1,
      "observed": "T-prefixed IDs identify topics.",
      "source_ids": [
        "D08"
      ],
      "profile": "Topic-object contract inspected 13 October 2026, including the published October 2026 fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-049",
      "family": "F1",
      "criterion": "C1",
      "test_id": "F1-C1b",
      "result": 1,
      "observed": "domain/field/subfield fields preserve the topic hierarchy.",
      "source_ids": [
        "D08"
      ],
      "profile": "Topic-object contract inspected 13 October 2026, including the published October 2026 fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-049",
      "family": "F1",
      "criterion": "C1",
      "test_id": "F1-C1c",
      "result": 0,
      "observed": "Independent topics cannot be combined into a new native compound-topic identifier through this contract.",
      "source_ids": [
        "D08"
      ],
      "profile": "Topic-object contract inspected 13 October 2026, including the published October 2026 fields",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-049",
      "family": "F1",
      "criterion": "C1",
      "test_id": "F1-C1d",
      "result": 0,
      "observed": "Topic objects do not define place/time/form modifiers of a constructed class expression.",
      "source_ids": [
        "D08"
      ],
      "profile": "Topic-object contract inspected 13 October 2026, including the published October 2026 fields",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-049",
      "family": "F1",
      "criterion": "C2",
      "test_id": "F1-C2a",
      "result": 1,
      "observed": "display_name provides English lexical access.",
      "source_ids": [
        "D08"
      ],
      "profile": "Topic-object contract inspected 13 October 2026, including the published October 2026 fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-049",
      "family": "F1",
      "criterion": "C2",
      "test_id": "F1-C2b",
      "result": 1,
      "observed": "description, keywords and legacy_keywords add lexical cues.",
      "source_ids": [
        "D08"
      ],
      "profile": "Topic-object contract inspected 13 October 2026, including the published October 2026 fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-049",
      "family": "F1",
      "criterion": "C2",
      "test_id": "F1-C2c",
      "result": 1,
      "observed": "Descriptions and hierarchy help distinguish related labels.",
      "source_ids": [
        "D08"
      ],
      "profile": "Topic-object contract inspected 13 October 2026, including the published October 2026 fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-049",
      "family": "F1",
      "criterion": "C2",
      "test_id": "F1-C2d",
      "result": 1,
      "observed": "A supplied work-level primary_topic/topics assignment identifies its native topic reference. This is the record-to-subject anchoring direction; topic-to-work evidence retrieval is assessed separately under C4d. Both use the documented assignment relation.",
      "source_ids": [
        "D08"
      ],
      "profile": "Topic-object contract inspected 13 October 2026, including the published October 2026 fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-049",
      "family": "F1",
      "criterion": "C3",
      "test_id": "F1-C3a",
      "result": 1,
      "observed": "Topic-to-subfield and higher-level links are explicit.",
      "source_ids": [
        "D08"
      ],
      "profile": "Topic-object contract inspected 13 October 2026, including the published October 2026 fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-049",
      "family": "F1",
      "criterion": "C3",
      "test_id": "F1-C3b",
      "result": 1,
      "observed": "Topic→subfield→field supplies an identified two-link route.",
      "source_ids": [
        "D08"
      ],
      "profile": "Topic-object contract inspected 13 October 2026, including the published October 2026 fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-049",
      "family": "F1",
      "criterion": "C3",
      "test_id": "F1-C3c",
      "result": 0,
      "observed": "The new siblings field is a same-parent grouping, not an independently asserted nonhierarchical semantic cross-reference.",
      "source_ids": [
        "D08"
      ],
      "profile": "Topic-object contract inspected 13 October 2026, including the published October 2026 fields",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-049",
      "family": "F1",
      "criterion": "C3",
      "test_id": "F1-C3d",
      "result": 0,
      "observed": "No native compound-topic decomposition is defined.",
      "source_ids": [
        "D08"
      ],
      "profile": "Topic-object contract inspected 13 October 2026, including the published October 2026 fields",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-049",
      "family": "F1",
      "criterion": "C4",
      "test_id": "F1-C4a",
      "result": 1,
      "observed": "Topic ID and hierarchical content are retrievable.",
      "source_ids": [
        "D08"
      ],
      "profile": "Topic-object contract inspected 13 October 2026, including the published October 2026 fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-049",
      "family": "F1",
      "criterion": "C4",
      "test_id": "F1-C4b",
      "result": 1,
      "observed": "A topic description adds content beyond its name.",
      "source_ids": [
        "D08"
      ],
      "profile": "Topic-object contract inspected 13 October 2026, including the published October 2026 fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-049",
      "family": "F1",
      "criterion": "C4",
      "test_id": "F1-C4c",
      "result": 0,
      "observed": "A description or classifier output is not a classification exclusion/redirect rule.",
      "source_ids": [
        "D08"
      ],
      "profile": "Topic-object contract inspected 13 October 2026, including the published October 2026 fields",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F1-049",
      "family": "F1",
      "criterion": "C4",
      "test_id": "F1-C4d",
      "result": 1,
      "observed": "The topic contract explicitly links to assigned-work records.",
      "source_ids": [
        "D08"
      ],
      "profile": "Topic-object contract inspected 13 October 2026, including the published October 2026 fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-001",
      "family": "F2",
      "criterion": "C1",
      "test_id": "F2-C1a",
      "result": 1,
      "observed": "FAST authority IDs identify controlled headings.",
      "source_ids": [
        "V01",
        "V02"
      ],
      "profile": "FAST authority model and nine-facet rules in the October 2024 guide; authority/update fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-001",
      "family": "F2",
      "criterion": "C1",
      "test_id": "F2-C1b",
      "result": 0,
      "observed": "Independent facets do not encode one ordered cross-facet assertion; within-topical precoordination is acknowledged but is a different service.",
      "source_ids": [
        "V01",
        "V02"
      ],
      "profile": "FAST authority model and nine-facet rules in the October 2024 guide; authority/update fields",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-001",
      "family": "F2",
      "criterion": "C1",
      "test_id": "F2-C1c",
      "result": 1,
      "observed": "Nine facets distinguish the roles of topic, place, chronology and form.",
      "source_ids": [
        "V01",
        "V02"
      ],
      "profile": "FAST authority model and nine-facet rules in the October 2024 guide; authority/update fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-001",
      "family": "F2",
      "criterion": "C1",
      "test_id": "F2-C1d",
      "result": 1,
      "observed": "Heading wording, authorized qualifiers and source notes distinguish interpretations.",
      "source_ids": [
        "V01",
        "V02"
      ],
      "profile": "FAST authority model and nine-facet rules in the October 2024 guide; authority/update fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-001",
      "family": "F2",
      "criterion": "C2",
      "test_id": "F2-C2a",
      "result": 1,
      "observed": "Fully enumerated headings can serve as native anchors.",
      "source_ids": [
        "V01",
        "V02"
      ],
      "profile": "FAST authority model and nine-facet rules in the October 2024 guide; authority/update fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-001",
      "family": "F2",
      "criterion": "C2",
      "test_id": "F2-C2b",
      "result": 1,
      "observed": "Cross-reference/variant terms supply authorized alternative access.",
      "source_ids": [
        "V01",
        "V02"
      ],
      "profile": "FAST authority model and nine-facet rules in the October 2024 guide; authority/update fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-001",
      "family": "F2",
      "criterion": "C2",
      "test_id": "F2-C2c",
      "result": 1,
      "observed": "Facet and qualifier context disambiguate wording.",
      "source_ids": [
        "V01",
        "V02"
      ],
      "profile": "FAST authority model and nine-facet rules in the October 2024 guide; authority/update fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-001",
      "family": "F2",
      "criterion": "C2",
      "test_id": "F2-C2d",
      "result": 1,
      "observed": "The published model explicitly supports separately enumerated postcoordinate facets.",
      "source_ids": [
        "V01",
        "V02"
      ],
      "profile": "FAST authority model and nine-facet rules in the October 2024 guide; authority/update fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-001",
      "family": "F2",
      "criterion": "C3",
      "test_id": "F2-C3a",
      "result": 1,
      "observed": "Native broader/narrower references are retained.",
      "source_ids": [
        "V01",
        "V02"
      ],
      "profile": "FAST authority model and nine-facet rules in the October 2024 guide; authority/update fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-001",
      "family": "F2",
      "criterion": "C3",
      "test_id": "F2-C3b",
      "result": 1,
      "observed": "Source related-term links are distinct from hierarchy.",
      "source_ids": [
        "V01",
        "V02"
      ],
      "profile": "FAST authority model and nine-facet rules in the October 2024 guide; authority/update fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-001",
      "family": "F2",
      "criterion": "C3",
      "test_id": "F2-C3c",
      "result": 1,
      "observed": "USE/UF/equivalence is distinct from broader/narrower.",
      "source_ids": [
        "V01",
        "V02"
      ],
      "profile": "FAST authority model and nine-facet rules in the October 2024 guide; authority/update fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-001",
      "family": "F2",
      "criterion": "C3",
      "test_id": "F2-C3d",
      "result": 0,
      "observed": "The generic hierarchical field does not separately encode genus/species versus whole/part semantics in the assessed representation.",
      "source_ids": [
        "V01",
        "V02"
      ],
      "profile": "FAST authority model and nine-facet rules in the October 2024 guide; authority/update fields",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-001",
      "family": "F2",
      "criterion": "C4",
      "test_id": "F2-C4a",
      "result": 1,
      "observed": "Authority content is returned with a FAST ID.",
      "source_ids": [
        "V01",
        "V02"
      ],
      "profile": "FAST authority model and nine-facet rules in the October 2024 guide; authority/update fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-001",
      "family": "F2",
      "criterion": "C4",
      "test_id": "F2-C4b",
      "result": 1,
      "observed": "Scope/note fields supply interpretation where populated.",
      "source_ids": [
        "V01",
        "V02"
      ],
      "profile": "FAST authority model and nine-facet rules in the October 2024 guide; authority/update fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-001",
      "family": "F2",
      "criterion": "C4",
      "test_id": "F2-C4c",
      "result": 1,
      "observed": "LC source links and vocabulary provenance identify the supplying authority.",
      "source_ids": [
        "V01",
        "V02"
      ],
      "profile": "FAST authority model and nine-facet rules in the October 2024 guide; authority/update fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-001",
      "family": "F2",
      "criterion": "C4",
      "test_id": "F2-C4d",
      "result": 1,
      "observed": "The distribution’s authority/change records carry status/change information.",
      "source_ids": [
        "V01",
        "V02"
      ],
      "profile": "FAST authority model and nine-facet rules in the October 2024 guide; authority/update fields",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-002",
      "family": "F2",
      "criterion": "C1",
      "test_id": "F2-C1a",
      "result": 1,
      "observed": "An authority number identifies each established heading.",
      "source_ids": [
        "V03",
        "V04",
        "V05"
      ],
      "profile": "LCSH authority records plus MARC 21 subdivision and application rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-002",
      "family": "F2",
      "criterion": "C1",
      "test_id": "F2-C1b",
      "result": 1,
      "observed": "MARC x/y/z/v preserve ordered subject components across topical/time/place/form roles.",
      "source_ids": [
        "V03",
        "V04",
        "V05"
      ],
      "profile": "LCSH authority records plus MARC 21 subdivision and application rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-002",
      "family": "F2",
      "criterion": "C1",
      "test_id": "F2-C1c",
      "result": 1,
      "observed": "Subdivision subfields distinguish component roles.",
      "source_ids": [
        "V03",
        "V04",
        "V05"
      ],
      "profile": "LCSH authority records plus MARC 21 subdivision and application rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-002",
      "family": "F2",
      "criterion": "C1",
      "test_id": "F2-C1d",
      "result": 1,
      "observed": "Qualifiers and scope notes distinguish subject readings.",
      "source_ids": [
        "V03",
        "V04",
        "V05"
      ],
      "profile": "LCSH authority records plus MARC 21 subdivision and application rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-002",
      "family": "F2",
      "criterion": "C2",
      "test_id": "F2-C2a",
      "result": 1,
      "observed": "Existing headings support direct canonical lookup.",
      "source_ids": [
        "V03",
        "V04",
        "V05"
      ],
      "profile": "LCSH authority records plus MARC 21 subdivision and application rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-002",
      "family": "F2",
      "criterion": "C2",
      "test_id": "F2-C2b",
      "result": 1,
      "observed": "The Sofas USE/UF example provides alternative expressions.",
      "source_ids": [
        "V03",
        "V04",
        "V05"
      ],
      "profile": "LCSH authority records plus MARC 21 subdivision and application rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-002",
      "family": "F2",
      "criterion": "C2",
      "test_id": "F2-C2c",
      "result": 1,
      "observed": "The Literature record’s qualifier/use restrictions preserve non-equivalent readings.",
      "source_ids": [
        "V03",
        "V04",
        "V05"
      ],
      "profile": "LCSH authority records plus MARC 21 subdivision and application rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-002",
      "family": "F2",
      "criterion": "C2",
      "test_id": "F2-C2d",
      "result": 0,
      "observed": "Only a subset of all permitted compound headings is established; a complete qualified anchor can require rule-based construction.",
      "source_ids": [
        "V03",
        "V04",
        "V05"
      ],
      "profile": "LCSH authority records plus MARC 21 subdivision and application rules",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-002",
      "family": "F2",
      "criterion": "C3",
      "test_id": "F2-C3a",
      "result": 1,
      "observed": "BT/NT supports hierarchical traversal.",
      "source_ids": [
        "V03",
        "V04",
        "V05"
      ],
      "profile": "LCSH authority records plus MARC 21 subdivision and application rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-002",
      "family": "F2",
      "criterion": "C3",
      "test_id": "F2-C3b",
      "result": 1,
      "observed": "RT links such as Literature–Authorship are associative.",
      "source_ids": [
        "V03",
        "V04",
        "V05"
      ],
      "profile": "LCSH authority records plus MARC 21 subdivision and application rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-002",
      "family": "F2",
      "criterion": "C3",
      "test_id": "F2-C3c",
      "result": 1,
      "observed": "USE/UF and BT/NT are separately represented.",
      "source_ids": [
        "V03",
        "V04",
        "V05"
      ],
      "profile": "LCSH authority records plus MARC 21 subdivision and application rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-002",
      "family": "F2",
      "criterion": "C3",
      "test_id": "F2-C3d",
      "result": 0,
      "observed": "The same BT/NT notation covers genus/species, whole/part and instance relations; it does not carry a separate partitive edge tag.",
      "source_ids": [
        "V03",
        "V04",
        "V05"
      ],
      "profile": "LCSH authority records plus MARC 21 subdivision and application rules",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-002",
      "family": "F2",
      "criterion": "C4",
      "test_id": "F2-C4a",
      "result": 1,
      "observed": "The Literature authority record supplies identified content.",
      "source_ids": [
        "V03",
        "V04",
        "V05"
      ],
      "profile": "LCSH authority records plus MARC 21 subdivision and application rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-002",
      "family": "F2",
      "criterion": "C4",
      "test_id": "F2-C4b",
      "result": 1,
      "observed": "The 680 field returns scope text.",
      "source_ids": [
        "V03",
        "V04",
        "V05"
      ],
      "profile": "LCSH authority records plus MARC 21 subdivision and application rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-002",
      "family": "F2",
      "criterion": "C4",
      "test_id": "F2-C4c",
      "result": 1,
      "observed": "040/670 authority fields identify supplying agency/evidence.",
      "source_ids": [
        "V03",
        "V04",
        "V05"
      ],
      "profile": "LCSH authority records plus MARC 21 subdivision and application rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-002",
      "family": "F2",
      "criterion": "C4",
      "test_id": "F2-C4d",
      "result": 1,
      "observed": "005/008 and authority status information are available.",
      "source_ids": [
        "V03",
        "V04",
        "V05"
      ],
      "profile": "LCSH authority records plus MARC 21 subdivision and application rules",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-045",
      "family": "F2",
      "criterion": "C1",
      "test_id": "F2-C1a",
      "result": 1,
      "observed": "Concept URIs identify controlled subject meanings.",
      "source_ids": [
        "V06",
        "V07",
        "V08"
      ],
      "profile": "YSO core English concept model inspected 13 October 2026; separate YSO places is not included",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-045",
      "family": "F2",
      "criterion": "C1",
      "test_id": "F2-C1b",
      "result": 0,
      "observed": "Independent core concepts do not encode ordered cross-facet subject strings.",
      "source_ids": [
        "V06",
        "V07",
        "V08"
      ],
      "profile": "YSO core English concept model inspected 13 October 2026; separate YSO places is not included",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-045",
      "family": "F2",
      "criterion": "C1",
      "test_id": "F2-C1c",
      "result": 0,
      "observed": "Thematic groups are not topic/place/time/form subdivision fields; place names belong to a separate ontology.",
      "source_ids": [
        "V06",
        "V07",
        "V08"
      ],
      "profile": "YSO core English concept model inspected 13 October 2026; separate YSO places is not included",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-045",
      "family": "F2",
      "criterion": "C1",
      "test_id": "F2-C1d",
      "result": 1,
      "observed": "Qualified labels, definitions and context distinguish meanings.",
      "source_ids": [
        "V06",
        "V07",
        "V08"
      ],
      "profile": "YSO core English concept model inspected 13 October 2026; separate YSO places is not included",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-045",
      "family": "F2",
      "criterion": "C2",
      "test_id": "F2-C2a",
      "result": 1,
      "observed": "Preferred English labels identify concepts.",
      "source_ids": [
        "V06",
        "V07",
        "V08"
      ],
      "profile": "YSO core English concept model inspected 13 October 2026; separate YSO places is not included",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-045",
      "family": "F2",
      "criterion": "C2",
      "test_id": "F2-C2b",
      "result": 1,
      "observed": "Alternative labels and equivalence to source thesauri provide lexical alternatives.",
      "source_ids": [
        "V06",
        "V07",
        "V08"
      ],
      "profile": "YSO core English concept model inspected 13 October 2026; separate YSO places is not included",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-045",
      "family": "F2",
      "criterion": "C2",
      "test_id": "F2-C2c",
      "result": 1,
      "observed": "Qualified concepts and the ballet/ballets distinction preserve context.",
      "source_ids": [
        "V06",
        "V07",
        "V08"
      ],
      "profile": "YSO core English concept model inspected 13 October 2026; separate YSO places is not included",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-045",
      "family": "F2",
      "criterion": "C2",
      "test_id": "F2-C2d",
      "result": 1,
      "observed": "Enumerated concepts can be assigned as independent postcoordinate units.",
      "source_ids": [
        "V06",
        "V07",
        "V08"
      ],
      "profile": "YSO core English concept model inspected 13 October 2026; separate YSO places is not included",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-045",
      "family": "F2",
      "criterion": "C3",
      "test_id": "F2-C3a",
      "result": 1,
      "observed": "Parent-child relations support hierarchical navigation.",
      "source_ids": [
        "V06",
        "V07",
        "V08"
      ],
      "profile": "YSO core English concept model inspected 13 October 2026; separate YSO places is not included",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-045",
      "family": "F2",
      "criterion": "C3",
      "test_id": "F2-C3b",
      "result": 1,
      "observed": "Associative relations are separately supplied.",
      "source_ids": [
        "V06",
        "V07",
        "V08"
      ],
      "profile": "YSO core English concept model inspected 13 October 2026; separate YSO places is not included",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-045",
      "family": "F2",
      "criterion": "C3",
      "test_id": "F2-C3c",
      "result": 1,
      "observed": "Labels/equivalence mappings remain distinct from subject hierarchy.",
      "source_ids": [
        "V06",
        "V07",
        "V08"
      ],
      "profile": "YSO core English concept model inspected 13 October 2026; separate YSO places is not included",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-045",
      "family": "F2",
      "criterion": "C3",
      "test_id": "F2-C3d",
      "result": 1,
      "observed": "The official model explicitly distinguishes additional part-whole relations from hierarchy.",
      "source_ids": [
        "V06",
        "V07",
        "V08"
      ],
      "profile": "YSO core English concept model inspected 13 October 2026; separate YSO places is not included",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-045",
      "family": "F2",
      "criterion": "C4",
      "test_id": "F2-C4a",
      "result": 1,
      "observed": "Concept content is linked to its URI.",
      "source_ids": [
        "V06",
        "V07",
        "V08"
      ],
      "profile": "YSO core English concept model inspected 13 October 2026; separate YSO places is not included",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-045",
      "family": "F2",
      "criterion": "C4",
      "test_id": "F2-C4b",
      "result": 1,
      "observed": "Concept notes and scope/context are accessible where supplied.",
      "source_ids": [
        "V06",
        "V07",
        "V08"
      ],
      "profile": "YSO core English concept model inspected 13 October 2026; separate YSO places is not included",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-045",
      "family": "F2",
      "criterion": "C4",
      "test_id": "F2-C4c",
      "result": 1,
      "observed": "YSA/Allärs links and recorded sources identify origins.",
      "source_ids": [
        "V06",
        "V07",
        "V08"
      ],
      "profile": "YSO core English concept model inspected 13 October 2026; separate YSO places is not included",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F2-045",
      "family": "F2",
      "criterion": "C4",
      "test_id": "F2-C4d",
      "result": 1,
      "observed": "The p441 concept page gives record-level created and last-modified dates and identifies the concept URI; these are not merely the vocabulary collection update date.",
      "source_ids": [
        "V06",
        "V07",
        "V08"
      ],
      "profile": "YSO core English concept model inspected 13 October 2026; separate YSO places is not included",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-001",
      "family": "F3",
      "criterion": "C1",
      "test_id": "F3-C1a",
      "result": 1,
      "observed": "Classes/predicates have native names and typed domains.",
      "source_ids": [
        "O01"
      ],
      "profile": "Inspected Merge.kif branch with published WordNet 3.0 mappings; source profile dated 13 October 2026",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-001",
      "family": "F3",
      "criterion": "C1",
      "test_id": "F3-C1b",
      "result": 1,
      "observed": "CaseRole predicates distinguish agents, patients and other participants.",
      "source_ids": [
        "O01"
      ],
      "profile": "Inspected Merge.kif branch with published WordNet 3.0 mappings; source profile dated 13 October 2026",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-001",
      "family": "F3",
      "criterion": "C1",
      "test_id": "F3-C1c",
      "result": 1,
      "observed": "Disjoint and negative formulas encode logical restrictions.",
      "source_ids": [
        "O01"
      ],
      "profile": "Inspected Merge.kif branch with published WordNet 3.0 mappings; source profile dated 13 October 2026",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-001",
      "family": "F3",
      "criterion": "C1",
      "test_id": "F3-C1d",
      "result": 1,
      "observed": "TransitiveRelation contains nested variable-bearing conditional and quantified scope.",
      "source_ids": [
        "O01"
      ],
      "profile": "Inspected Merge.kif branch with published WordNet 3.0 mappings; source profile dated 13 October 2026",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-001",
      "family": "F3",
      "criterion": "C2",
      "test_id": "F3-C2a",
      "result": 1,
      "observed": "documentation and termFormat supply English wording.",
      "source_ids": [
        "O01",
        "O02"
      ],
      "profile": "Inspected Merge.kif branch with published WordNet 3.0 mappings; source profile dated 13 October 2026",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-001",
      "family": "F3",
      "criterion": "C2",
      "test_id": "F3-C2b",
      "result": 1,
      "observed": "WordNet synonym expressions and termFormat supply alternative access without a new synonym generator.",
      "source_ids": [
        "O01",
        "O02"
      ],
      "profile": "Inspected Merge.kif branch with published WordNet 3.0 mappings; source profile dated 13 October 2026",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-001",
      "family": "F3",
      "criterion": "C2",
      "test_id": "F3-C2c",
      "result": 1,
      "observed": "Released synset offsets map to ontology references.",
      "source_ids": [
        "O01",
        "O02"
      ],
      "profile": "Inspected Merge.kif branch with published WordNet 3.0 mappings; source profile dated 13 October 2026",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-001",
      "family": "F3",
      "criterion": "C2",
      "test_id": "F3-C2d",
      "result": 1,
      "observed": "The mapping header distinguishes equivalence, subsumption, instance and their complements.",
      "source_ids": [
        "O01",
        "O02"
      ],
      "profile": "Inspected Merge.kif branch with published WordNet 3.0 mappings; source profile dated 13 October 2026",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-001",
      "family": "F3",
      "criterion": "C3",
      "test_id": "F3-C3a",
      "result": 1,
      "observed": "subclass is explicitly defined.",
      "source_ids": [
        "O01"
      ],
      "profile": "Inspected Merge.kif branch with published WordNet 3.0 mappings; source profile dated 13 October 2026",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-001",
      "family": "F3",
      "criterion": "C3",
      "test_id": "F3-C3b",
      "result": 1,
      "observed": "Predicate argument positions and domain statements preserve roles.",
      "source_ids": [
        "O01"
      ],
      "profile": "Inspected Merge.kif branch with published WordNet 3.0 mappings; source profile dated 13 October 2026",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-001",
      "family": "F3",
      "criterion": "C3",
      "test_id": "F3-C3c",
      "result": 1,
      "observed": "Inverse/subrelation and symmetric/transitive classes are native constructs.",
      "source_ids": [
        "O01"
      ],
      "profile": "Inspected Merge.kif branch with published WordNet 3.0 mappings; source profile dated 13 October 2026",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-001",
      "family": "F3",
      "criterion": "C3",
      "test_id": "F3-C3d",
      "result": 1,
      "observed": "The supplied TransitiveRelation rule licenses a specified two-link composition.",
      "source_ids": [
        "O01"
      ],
      "profile": "Inspected Merge.kif branch with published WordNet 3.0 mappings; source profile dated 13 October 2026",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-001",
      "family": "F3",
      "criterion": "C4",
      "test_id": "F3-C4a",
      "result": 1,
      "observed": "English documentation is tied to the native reference.",
      "source_ids": [
        "O01",
        "O02"
      ],
      "profile": "Inspected Merge.kif branch with published WordNet 3.0 mappings; source profile dated 13 October 2026",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-001",
      "family": "F3",
      "criterion": "C4",
      "test_id": "F3-C4b",
      "result": 1,
      "observed": "Individual KIF formulas remain inspectable.",
      "source_ids": [
        "O01",
        "O02"
      ],
      "profile": "Inspected Merge.kif branch with published WordNet 3.0 mappings; source profile dated 13 October 2026",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-001",
      "family": "F3",
      "criterion": "C4",
      "test_id": "F3-C4c",
      "result": 1,
      "observed": "Conditional/negative formulas supply premises and rules beyond taxonomy.",
      "source_ids": [
        "O01",
        "O02"
      ],
      "profile": "Inspected Merge.kif branch with published WordNet 3.0 mappings; source profile dated 13 October 2026",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-001",
      "family": "F3",
      "criterion": "C4",
      "test_id": "F3-C4d",
      "result": 1,
      "observed": "WordNet offsets and mapping markers retain the supplying sense identity.",
      "source_ids": [
        "O01",
        "O02"
      ],
      "profile": "Inspected Merge.kif branch with published WordNet 3.0 mappings; source profile dated 13 October 2026",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-009",
      "family": "F3",
      "criterion": "C1",
      "test_id": "F3-C1a",
      "result": 1,
      "observed": "OWL classes and properties identify native types and relations.",
      "source_ids": [
        "O03"
      ],
      "profile": "CCO merged 2.2, version IRI 2026-08-13, including declared BFO imports",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-009",
      "family": "F3",
      "criterion": "C1",
      "test_id": "F3-C1b",
      "result": 1,
      "observed": "Event/act/agent/participant properties allow role-distinguished situations.",
      "source_ids": [
        "O03"
      ],
      "profile": "CCO merged 2.2, version IRI 2026-08-13, including declared BFO imports",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-009",
      "family": "F3",
      "criterion": "C1",
      "test_id": "F3-C1c",
      "result": 1,
      "observed": "OWL restrictions, complements and disjointness are present.",
      "source_ids": [
        "O03"
      ],
      "profile": "CCO merged 2.2, version IRI 2026-08-13, including declared BFO imports",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-009",
      "family": "F3",
      "criterion": "C1",
      "test_id": "F3-C1d",
      "result": 0,
      "observed": "The OWL profile does not provide a general free-variable rule language with arbitrary quantifier scope; property chains are assessed separately.",
      "source_ids": [
        "O03"
      ],
      "profile": "CCO merged 2.2, version IRI 2026-08-13, including declared BFO imports",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-009",
      "family": "F3",
      "criterion": "C2",
      "test_id": "F3-C2a",
      "result": 1,
      "observed": "rdfs:label and definitions provide English access.",
      "source_ids": [
        "O03"
      ],
      "profile": "CCO merged 2.2, version IRI 2026-08-13, including declared BFO imports",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-009",
      "family": "F3",
      "criterion": "C2",
      "test_id": "F3-C2b",
      "result": 1,
      "observed": "altLabel/doctrinal label/acronym annotations supply alternative wording.",
      "source_ids": [
        "O03"
      ],
      "profile": "CCO merged 2.2, version IRI 2026-08-13, including declared BFO imports",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-009",
      "family": "F3",
      "criterion": "C2",
      "test_id": "F3-C2c",
      "result": 0,
      "observed": "The inspected ontology does not include a WordNet-like lexical-sense alignment layer.",
      "source_ids": [
        "O03"
      ],
      "profile": "CCO merged 2.2, version IRI 2026-08-13, including declared BFO imports",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-009",
      "family": "F3",
      "criterion": "C2",
      "test_id": "F3-C2d",
      "result": 0,
      "observed": "Without that layer, no lexical-sense equivalence/subsumption/instance mapping route is credited.",
      "source_ids": [
        "O03"
      ],
      "profile": "CCO merged 2.2, version IRI 2026-08-13, including declared BFO imports",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-009",
      "family": "F3",
      "criterion": "C3",
      "test_id": "F3-C3a",
      "result": 1,
      "observed": "rdfs:subClassOf provides hierarchy.",
      "source_ids": [
        "O03"
      ],
      "profile": "CCO merged 2.2, version IRI 2026-08-13, including declared BFO imports",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-009",
      "family": "F3",
      "criterion": "C3",
      "test_id": "F3-C3b",
      "result": 1,
      "observed": "Named roles and property directions are explicit.",
      "source_ids": [
        "O03"
      ],
      "profile": "CCO merged 2.2, version IRI 2026-08-13, including declared BFO imports",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-009",
      "family": "F3",
      "criterion": "C3",
      "test_id": "F3-C3c",
      "result": 1,
      "observed": "inverseOf and subPropertyOf are supplied.",
      "source_ids": [
        "O03"
      ],
      "profile": "CCO merged 2.2, version IRI 2026-08-13, including declared BFO imports",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-009",
      "family": "F3",
      "criterion": "C3",
      "test_id": "F3-C3d",
      "result": 1,
      "observed": "propertyChainAxiom and transitive properties express non-taxonomic path rules.",
      "source_ids": [
        "O03"
      ],
      "profile": "CCO merged 2.2, version IRI 2026-08-13, including declared BFO imports",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-009",
      "family": "F3",
      "criterion": "C4",
      "test_id": "F3-C4a",
      "result": 1,
      "observed": "SKOS definitions identify meaning.",
      "source_ids": [
        "O03"
      ],
      "profile": "CCO merged 2.2, version IRI 2026-08-13, including declared BFO imports",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-009",
      "family": "F3",
      "criterion": "C4",
      "test_id": "F3-C4b",
      "result": 1,
      "observed": "OWL axioms are individually inspectable.",
      "source_ids": [
        "O03"
      ],
      "profile": "CCO merged 2.2, version IRI 2026-08-13, including declared BFO imports",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-009",
      "family": "F3",
      "criterion": "C4",
      "test_id": "F3-C4c",
      "result": 1,
      "observed": "Restrictions and property chains go beyond plain RDFS propagation.",
      "source_ids": [
        "O03"
      ],
      "profile": "CCO merged 2.2, version IRI 2026-08-13, including declared BFO imports",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-009",
      "family": "F3",
      "criterion": "C4",
      "test_id": "F3-C4d",
      "result": 1,
      "observed": "Definition-source and is-curated-in-ontology annotations identify source/provenance.",
      "source_ids": [
        "O03"
      ],
      "profile": "CCO merged 2.2, version IRI 2026-08-13, including declared BFO imports",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-029",
      "family": "F3",
      "criterion": "C1",
      "test_id": "F3-C1a",
      "result": 1,
      "observed": "Frames and frame-element properties supply identified classes and roles.",
      "source_ids": [
        "O04",
        "O05",
        "O06"
      ],
      "profile": "FrameBase 2.0 RDFS schema with its documented ReDer companion rules; no unverified instance integration",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-029",
      "family": "F3",
      "criterion": "C1",
      "test_id": "F3-C1b",
      "result": 1,
      "observed": "The marriage example distinguishes both partners and time.",
      "source_ids": [
        "O04",
        "O05",
        "O06"
      ],
      "profile": "FrameBase 2.0 RDFS schema with its documented ReDer companion rules; no unverified instance integration",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-029",
      "family": "F3",
      "criterion": "C1",
      "test_id": "F3-C1c",
      "result": 0,
      "observed": "Strict RDFS plus the published ReDer clauses do not express general OWL-style disjointness/cardinality/negation restrictions.",
      "source_ids": [
        "O04",
        "O05",
        "O06"
      ],
      "profile": "FrameBase 2.0 RDFS schema with its documented ReDer companion rules; no unverified instance integration",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-029",
      "family": "F3",
      "criterion": "C1",
      "test_id": "F3-C1d",
      "result": 1,
      "observed": "ReDer explicitly supplies variable-bearing definite-clause equivalences between frame structure and a binary predicate.",
      "source_ids": [
        "O04",
        "O05",
        "O06"
      ],
      "profile": "FrameBase 2.0 RDFS schema with its documented ReDer companion rules; no unverified instance integration",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-029",
      "family": "F3",
      "criterion": "C2",
      "test_id": "F3-C2a",
      "result": 1,
      "observed": "Lexical-form and definition properties supply English access.",
      "source_ids": [
        "O04",
        "O05",
        "O06"
      ],
      "profile": "FrameBase 2.0 RDFS schema with its documented ReDer companion rules; no unverified instance integration",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-029",
      "family": "F3",
      "criterion": "C2",
      "test_id": "F3-C2b",
      "result": 1,
      "observed": "Nominalizations and near-equivalent microframes supply alternative expression routes.",
      "source_ids": [
        "O04",
        "O05",
        "O06"
      ],
      "profile": "FrameBase 2.0 RDFS schema with its documented ReDer companion rules; no unverified instance integration",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-029",
      "family": "F3",
      "criterion": "C2",
      "test_id": "F3-C2c",
      "result": 1,
      "observed": "FrameNet and WordNet identifiers are preserved.",
      "source_ids": [
        "O04",
        "O05",
        "O06"
      ],
      "profile": "FrameBase 2.0 RDFS schema with its documented ReDer companion rules; no unverified instance integration",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-029",
      "family": "F3",
      "criterion": "C2",
      "test_id": "F3-C2d",
      "result": 1,
      "observed": "isSimilarTo and distinct source/microframe links preserve approximate versus asserted structural relationships.",
      "source_ids": [
        "O04",
        "O05",
        "O06"
      ],
      "profile": "FrameBase 2.0 RDFS schema with its documented ReDer companion rules; no unverified instance integration",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-029",
      "family": "F3",
      "criterion": "C3",
      "test_id": "F3-C3a",
      "result": 1,
      "observed": "Frame/microframe inheritance is represented.",
      "source_ids": [
        "O04",
        "O05",
        "O06"
      ],
      "profile": "FrameBase 2.0 RDFS schema with its documented ReDer companion rules; no unverified instance integration",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-029",
      "family": "F3",
      "criterion": "C3",
      "test_id": "F3-C3b",
      "result": 1,
      "observed": "Frame-element properties preserve participant direction.",
      "source_ids": [
        "O04",
        "O05",
        "O06"
      ],
      "profile": "FrameBase 2.0 RDFS schema with its documented ReDer companion rules; no unverified instance integration",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-029",
      "family": "F3",
      "criterion": "C3",
      "test_id": "F3-C3c",
      "result": 1,
      "observed": "RDFS subproperty and frame-element inheritance are explicit.",
      "source_ids": [
        "O04",
        "O05",
        "O06"
      ],
      "profile": "FrameBase 2.0 RDFS schema with its documented ReDer companion rules; no unverified instance integration",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-029",
      "family": "F3",
      "criterion": "C3",
      "test_id": "F3-C3d",
      "result": 1,
      "observed": "The ReDer example licenses a shortcut through the identified intermediate frame.",
      "source_ids": [
        "O04",
        "O05",
        "O06"
      ],
      "profile": "FrameBase 2.0 RDFS schema with its documented ReDer companion rules; no unverified instance integration",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-029",
      "family": "F3",
      "criterion": "C4",
      "test_id": "F3-C4a",
      "result": 1,
      "observed": "Definitions are tied to frames and lexical microframes.",
      "source_ids": [
        "O04",
        "O05",
        "O06"
      ],
      "profile": "FrameBase 2.0 RDFS schema with its documented ReDer companion rules; no unverified instance integration",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-029",
      "family": "F3",
      "criterion": "C4",
      "test_id": "F3-C4b",
      "result": 1,
      "observed": "Native schema statements remain inspectable.",
      "source_ids": [
        "O04",
        "O05",
        "O06"
      ],
      "profile": "FrameBase 2.0 RDFS schema with its documented ReDer companion rules; no unverified instance integration",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-029",
      "family": "F3",
      "criterion": "C4",
      "test_id": "F3-C4c",
      "result": 1,
      "observed": "ReDer rules add a declared inference beyond subclass propagation.",
      "source_ids": [
        "O04",
        "O05",
        "O06"
      ],
      "profile": "FrameBase 2.0 RDFS schema with its documented ReDer companion rules; no unverified instance integration",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F3-029",
      "family": "F3",
      "criterion": "C4",
      "test_id": "F3-C4d",
      "result": 1,
      "observed": "hasFramenetLU/FE and hasSynsetNumber retain source identifiers.",
      "source_ids": [
        "O04",
        "O05",
        "O06"
      ],
      "profile": "FrameBase 2.0 RDFS schema with its documented ReDer companion rules; no unverified instance integration",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-001",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1a",
      "result": 1,
      "observed": "Mapping-based triples preserve subjects, predicates and values.",
      "source_ids": [
        "G01",
        "G02"
      ],
      "profile": "Mapping-based DBpedia ontology/core assertion model, with source/identity links; not arbitrary custom RDF extensions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-001",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1b",
      "result": 0,
      "observed": "The credited core triple record does not attach a general independent qualifier bundle to each fact.",
      "source_ids": [
        "G01",
        "G02"
      ],
      "profile": "Mapping-based DBpedia ontology/core assertion model, with source/identity links; not arbitrary custom RDF extensions",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-001",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1c",
      "result": 0,
      "observed": "Absence of a triple is not an explicit negative/known-none value in this profile.",
      "source_ids": [
        "G01",
        "G02"
      ],
      "profile": "Mapping-based DBpedia ontology/core assertion model, with source/identity links; not arbitrary custom RDF extensions",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-001",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1d",
      "result": 0,
      "observed": "The core assertion route lacks the Wikibase-style unknown/no-value distinction.",
      "source_ids": [
        "G01",
        "G02"
      ],
      "profile": "Mapping-based DBpedia ontology/core assertion model, with source/identity links; not arbitrary custom RDF extensions",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-001",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2a",
      "result": 1,
      "observed": "Labels/abstracts locate English entities.",
      "source_ids": [
        "G01",
        "G02"
      ],
      "profile": "Mapping-based DBpedia ontology/core assertion model, with source/identity links; not arbitrary custom RDF extensions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-001",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2b",
      "result": 1,
      "observed": "Redirect/equivalence/name routes support alternative expressions.",
      "source_ids": [
        "G01",
        "G02"
      ],
      "profile": "Mapping-based DBpedia ontology/core assertion model, with source/identity links; not arbitrary custom RDF extensions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-001",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2c",
      "result": 1,
      "observed": "Entity identity, type and description distinguish contexts.",
      "source_ids": [
        "G01",
        "G02"
      ],
      "profile": "Mapping-based DBpedia ontology/core assertion model, with source/identity links; not arbitrary custom RDF extensions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-001",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2d",
      "result": 1,
      "observed": "sameAs and source-page links connect outside identifiers.",
      "source_ids": [
        "G01",
        "G02"
      ],
      "profile": "Mapping-based DBpedia ontology/core assertion model, with source/identity links; not arbitrary custom RDF extensions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-001",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3a",
      "result": 1,
      "observed": "Ontology property direction is documented.",
      "source_ids": [
        "G01",
        "G02"
      ],
      "profile": "Mapping-based DBpedia ontology/core assertion model, with source/identity links; not arbitrary custom RDF extensions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-001",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3b",
      "result": 1,
      "observed": "Identified entity links and type links can be joined.",
      "source_ids": [
        "G01",
        "G02"
      ],
      "profile": "Mapping-based DBpedia ontology/core assertion model, with source/identity links; not arbitrary custom RDF extensions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-001",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3c",
      "result": 1,
      "observed": "Ontology subproperties/inverse declarations provide source-defined transitions.",
      "source_ids": [
        "G01",
        "G02"
      ],
      "profile": "Mapping-based DBpedia ontology/core assertion model, with source/identity links; not arbitrary custom RDF extensions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-001",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3d",
      "result": 1,
      "observed": "Domain/range declarations are machine-inspectable.",
      "source_ids": [
        "G01",
        "G02"
      ],
      "profile": "Mapping-based DBpedia ontology/core assertion model, with source/identity links; not arbitrary custom RDF extensions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-001",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4a",
      "result": 1,
      "observed": "An assertion is located through its native subject/property/object.",
      "source_ids": [
        "G01",
        "G02"
      ],
      "profile": "Mapping-based DBpedia ontology/core assertion model, with source/identity links; not arbitrary custom RDF extensions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-001",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4b",
      "result": 1,
      "observed": "wasDerivedFrom/source-page context traces extracted content beyond a general homepage.",
      "source_ids": [
        "G01",
        "G02"
      ],
      "profile": "Mapping-based DBpedia ontology/core assertion model, with source/identity links; not arbitrary custom RDF extensions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-001",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4c",
      "result": 0,
      "observed": "No fact rank or confidence is part of the credited core assertion schema.",
      "source_ids": [
        "G01",
        "G02"
      ],
      "profile": "Mapping-based DBpedia ontology/core assertion model, with source/identity links; not arbitrary custom RDF extensions",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-001",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4d",
      "result": 1,
      "observed": "Source/extraction contexts can be retained for provenance-aware inspection.",
      "source_ids": [
        "G01",
        "G02"
      ],
      "profile": "Mapping-based DBpedia ontology/core assertion model, with source/identity links; not arbitrary custom RDF extensions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-002",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1a",
      "result": 1,
      "observed": "Items, properties and statements preserve assertion identity.",
      "source_ids": [
        "G03",
        "G04"
      ],
      "profile": "Full statement model inspected 13 October 2026; not the truthy-only RDF view",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-002",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1b",
      "result": 1,
      "observed": "Qualifiers attach to an individual statement.",
      "source_ids": [
        "G03",
        "G04"
      ],
      "profile": "Full statement model inspected 13 October 2026; not the truthy-only RDF view",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-002",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1c",
      "result": 1,
      "observed": "A no-value snak records known absence; omission alone does not.",
      "source_ids": [
        "G03",
        "G04"
      ],
      "profile": "Full statement model inspected 13 October 2026; not the truthy-only RDF view",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-002",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1d",
      "result": 1,
      "observed": "Some-value/unknown and no-value are separate native value states.",
      "source_ids": [
        "G03",
        "G04"
      ],
      "profile": "Full statement model inspected 13 October 2026; not the truthy-only RDF view",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-002",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2a",
      "result": 1,
      "observed": "English labels support lookup.",
      "source_ids": [
        "G03"
      ],
      "profile": "Full statement model inspected 13 October 2026; not the truthy-only RDF view",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-002",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2b",
      "result": 1,
      "observed": "Aliases provide alternative expressions.",
      "source_ids": [
        "G03"
      ],
      "profile": "Full statement model inspected 13 October 2026; not the truthy-only RDF view",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-002",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2c",
      "result": 1,
      "observed": "Descriptions, item IDs and statement context preserve different referents.",
      "source_ids": [
        "G03"
      ],
      "profile": "Full statement model inspected 13 October 2026; not the truthy-only RDF view",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-002",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2d",
      "result": 1,
      "observed": "External-ID properties and sitelinks identify outside resources.",
      "source_ids": [
        "G03"
      ],
      "profile": "Full statement model inspected 13 October 2026; not the truthy-only RDF view",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-002",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3a",
      "result": 1,
      "observed": "Property direction is explicit.",
      "source_ids": [
        "G03",
        "G05"
      ],
      "profile": "Full statement model inspected 13 October 2026; not the truthy-only RDF view",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-002",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3b",
      "result": 1,
      "observed": "Statements can join through shared item IDs.",
      "source_ids": [
        "G03",
        "G05"
      ],
      "profile": "Full statement model inspected 13 October 2026; not the truthy-only RDF view",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-002",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3c",
      "result": 1,
      "observed": "Inverse/symmetric property constraints and relation definitions license specific reversals.",
      "source_ids": [
        "G03",
        "G05"
      ],
      "profile": "Full statement model inspected 13 October 2026; not the truthy-only RDF view",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-002",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3d",
      "result": 1,
      "observed": "Property-constraint statements provide typed restrictions.",
      "source_ids": [
        "G03",
        "G05"
      ],
      "profile": "Full statement model inspected 13 October 2026; not the truthy-only RDF view",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-002",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4a",
      "result": 1,
      "observed": "Statement IDs and item revisions identify content.",
      "source_ids": [
        "G03",
        "G04",
        "G06"
      ],
      "profile": "Full statement model inspected 13 October 2026; not the truthy-only RDF view",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-002",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4b",
      "result": 1,
      "observed": "References supply source items/URLs and dates where populated.",
      "source_ids": [
        "G03",
        "G04",
        "G06"
      ],
      "profile": "Full statement model inspected 13 October 2026; not the truthy-only RDF view",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-002",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4c",
      "result": 1,
      "observed": "Ranks distinguish preferred, normal and deprecated statements.",
      "source_ids": [
        "G03",
        "G04",
        "G06"
      ],
      "profile": "Full statement model inspected 13 October 2026; not the truthy-only RDF view",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-002",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4d",
      "result": 1,
      "observed": "Reference and rank information supports source/status-aware evidence inspection.",
      "source_ids": [
        "G03",
        "G04",
        "G06"
      ],
      "profile": "Full statement model inspected 13 October 2026; not the truthy-only RDF view",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-003",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1a",
      "result": 1,
      "observed": "Native typed facts are explicit.",
      "source_ids": [
        "G07",
        "G08",
        "G11"
      ],
      "profile": "YAGO 4.6 published schema/facts/labels/meta/logs; inspected release samples and contract",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-003",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1b",
      "result": 1,
      "observed": "RDF-star metadata attach dates to individual facts.",
      "source_ids": [
        "G07",
        "G08",
        "G11"
      ],
      "profile": "YAGO 4.6 published schema/facts/labels/meta/logs; inspected release samples and contract",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-003",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1c",
      "result": 0,
      "observed": "The accepted-fact profile does not define an explicit no-value/negative assertion service; rejected statements in logs are not accepted negations.",
      "source_ids": [
        "G07",
        "G08",
        "G11"
      ],
      "profile": "YAGO 4.6 published schema/facts/labels/meta/logs; inspected release samples and contract",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-003",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1d",
      "result": 0,
      "observed": "Unknown/no-value snak semantics are not part of the accepted YAGO value-state contract.",
      "source_ids": [
        "G07",
        "G08",
        "G11"
      ],
      "profile": "YAGO 4.6 published schema/facts/labels/meta/logs; inspected release samples and contract",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-003",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2a",
      "result": 1,
      "observed": "Readable identifiers and labels expose English entities.",
      "source_ids": [
        "G07",
        "G10"
      ],
      "profile": "YAGO 4.6 published schema/facts/labels/meta/logs; inspected release samples and contract",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-003",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2b",
      "result": 1,
      "observed": "alternateName supplies alternatives.",
      "source_ids": [
        "G07",
        "G10"
      ],
      "profile": "YAGO 4.6 published schema/facts/labels/meta/logs; inspected release samples and contract",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-003",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2c",
      "result": 1,
      "observed": "Descriptions and class/entity identities distinguish referents.",
      "source_ids": [
        "G07",
        "G10"
      ],
      "profile": "YAGO 4.6 published schema/facts/labels/meta/logs; inspected release samples and contract",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-003",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2d",
      "result": 1,
      "observed": "sameAs and Wikidata-based identities preserve cross-source references.",
      "source_ids": [
        "G07",
        "G10"
      ],
      "profile": "YAGO 4.6 published schema/facts/labels/meta/logs; inspected release samples and contract",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-003",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3a",
      "result": 1,
      "observed": "Schema properties retain direction.",
      "source_ids": [
        "G07",
        "G09"
      ],
      "profile": "YAGO 4.6 published schema/facts/labels/meta/logs; inspected release samples and contract",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-003",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3b",
      "result": 1,
      "observed": "The full taxonomy and fact identifiers support joined navigation.",
      "source_ids": [
        "G07",
        "G09"
      ],
      "profile": "YAGO 4.6 published schema/facts/labels/meta/logs; inspected release samples and contract",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-003",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3c",
      "result": 1,
      "observed": "Property definitions and hierarchy provide declared related/inverse-orientation conventions.",
      "source_ids": [
        "G07",
        "G09"
      ],
      "profile": "YAGO 4.6 published schema/facts/labels/meta/logs; inspected release samples and contract",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-003",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3d",
      "result": 1,
      "observed": "SHACL supplies machine-inspectable ranges and constraints.",
      "source_ids": [
        "G07",
        "G09"
      ],
      "profile": "YAGO 4.6 published schema/facts/labels/meta/logs; inspected release samples and contract",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-003",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4a",
      "result": 1,
      "observed": "A fact is inspectable and located in the released profile.",
      "source_ids": [
        "G07",
        "G08",
        "G11"
      ],
      "profile": "YAGO 4.6 published schema/facts/labels/meta/logs; inspected release samples and contract",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-003",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4b",
      "result": null,
      "observed": "Time annotations and source-origin descriptions were found; an upstream citation attached to a particular accepted assertion was not verified in the inspected sample.",
      "source_ids": [
        "G07",
        "G08",
        "G11"
      ],
      "profile": "YAGO 4.6 published schema/facts/labels/meta/logs; inspected release samples and contract",
      "evidence_kind": "unresolved_documentary_evidence",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-003",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4c",
      "result": 0,
      "observed": "The profile provides qualified facts and rejection logs but no general confidence/preferred-rank field for accepted facts.",
      "source_ids": [
        "G07",
        "G08",
        "G11"
      ],
      "profile": "YAGO 4.6 published schema/facts/labels/meta/logs; inspected release samples and contract",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-003",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4d",
      "result": 1,
      "observed": "Rejected-versus-accepted status and validation logs permit evidence-boundary inspection.",
      "source_ids": [
        "G07",
        "G08",
        "G11"
      ],
      "profile": "YAGO 4.6 published schema/facts/labels/meta/logs; inspected release samples and contract",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-006",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1a",
      "result": 1,
      "observed": "Typed textual triples constitute the native assertions.",
      "source_ids": [
        "G12",
        "G13"
      ],
      "profile": "ATOMIC 2020 released symbolic head/relation/tail profile, excluding neural-generated expansions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-006",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1b",
      "result": 0,
      "observed": "A flat tuple does not separately attach a qualifier bundle to the assertion.",
      "source_ids": [
        "G12",
        "G13"
      ],
      "profile": "ATOMIC 2020 released symbolic head/relation/tail profile, excluding neural-generated expansions",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-006",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1c",
      "result": 1,
      "observed": "NotDesires is a native explicitly negative relation.",
      "source_ids": [
        "G12",
        "G13"
      ],
      "profile": "ATOMIC 2020 released symbolic head/relation/tail profile, excluding neural-generated expansions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-006",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1d",
      "result": 0,
      "observed": "No separate unknown-value versus known-none snak type is defined.",
      "source_ids": [
        "G12",
        "G13"
      ],
      "profile": "ATOMIC 2020 released symbolic head/relation/tail profile, excluding neural-generated expansions",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-006",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2a",
      "result": 1,
      "observed": "English textual heads/tails provide lexical access.",
      "source_ids": [
        "G12",
        "G13"
      ],
      "profile": "ATOMIC 2020 released symbolic head/relation/tail profile, excluding neural-generated expansions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-006",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2b",
      "result": 0,
      "observed": "The release relation inventory is not an authorized alias/synonym layer.",
      "source_ids": [
        "G12",
        "G13"
      ],
      "profile": "ATOMIC 2020 released symbolic head/relation/tail profile, excluding neural-generated expansions",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-006",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2c",
      "result": 1,
      "observed": "Event descriptions and PersonX/PersonY context remain available.",
      "source_ids": [
        "G12",
        "G13"
      ],
      "profile": "ATOMIC 2020 released symbolic head/relation/tail profile, excluding neural-generated expansions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-006",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2d",
      "result": 0,
      "observed": "The released tuple has no native external-entity/sense-ID slot.",
      "source_ids": [
        "G12",
        "G13"
      ],
      "profile": "ATOMIC 2020 released symbolic head/relation/tail profile, excluding neural-generated expansions",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-006",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3a",
      "result": 1,
      "observed": "The relation inventory specifies subject/object direction.",
      "source_ids": [
        "G12",
        "G13"
      ],
      "profile": "ATOMIC 2020 released symbolic head/relation/tail profile, excluding neural-generated expansions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-006",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3b",
      "result": 1,
      "observed": "Shared textual node identities allow relation records to join; this does not assert global connectedness.",
      "source_ids": [
        "G12",
        "G13"
      ],
      "profile": "ATOMIC 2020 released symbolic head/relation/tail profile, excluding neural-generated expansions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-006",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3c",
      "result": 1,
      "observed": "isBefore/isAfter are source-defined converse temporal relations.",
      "source_ids": [
        "G12",
        "G13"
      ],
      "profile": "ATOMIC 2020 released symbolic head/relation/tail profile, excluding neural-generated expansions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-006",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3d",
      "result": 0,
      "observed": "The tuple schema supplies no separate machine-inspectable domain/range constraint record for each transition.",
      "source_ids": [
        "G12",
        "G13"
      ],
      "profile": "ATOMIC 2020 released symbolic head/relation/tail profile, excluding neural-generated expansions",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-006",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4a",
      "result": 1,
      "observed": "The tuple itself is inspectable evidence.",
      "source_ids": [
        "G12",
        "G13"
      ],
      "profile": "ATOMIC 2020 released symbolic head/relation/tail profile, excluding neural-generated expansions",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-006",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4b",
      "result": 0,
      "observed": "The credited record contains no assertion-specific citation/source identifier field.",
      "source_ids": [
        "G12",
        "G13"
      ],
      "profile": "ATOMIC 2020 released symbolic head/relation/tail profile, excluding neural-generated expansions",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-006",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4c",
      "result": 0,
      "observed": "The core tuple has no native rank/confidence field; collection-level verification statistics are not per-edge confidence.",
      "source_ids": [
        "G12",
        "G13"
      ],
      "profile": "ATOMIC 2020 released symbolic head/relation/tail profile, excluding neural-generated expansions",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-006",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4d",
      "result": 0,
      "observed": "No per-record source/status metadata selection service is defined by this tuple profile.",
      "source_ids": [
        "G12",
        "G13"
      ],
      "profile": "ATOMIC 2020 released symbolic head/relation/tail profile, excluding neural-generated expansions",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-009",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1a",
      "result": 1,
      "observed": "Typed assertion records identify endpoints and relation.",
      "source_ids": [
        "G14",
        "G15",
        "G16"
      ],
      "profile": "ConceptNet 5.7 assertion/API model with its documented relation vocabulary",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-009",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1b",
      "result": 0,
      "observed": "Source/sentence/weight metadata are not a general qualifier-role bundle for facts.",
      "source_ids": [
        "G14",
        "G15",
        "G16"
      ],
      "profile": "ConceptNet 5.7 assertion/API model with its documented relation vocabulary",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-009",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1c",
      "result": 1,
      "observed": "Negative relation names such as NotDesires are explicit.",
      "source_ids": [
        "G14",
        "G15",
        "G16"
      ],
      "profile": "ConceptNet 5.7 assertion/API model with its documented relation vocabulary",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-009",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1d",
      "result": 0,
      "observed": "No distinct unknown-versus-known-none value-state mechanism is defined in this assertion contract.",
      "source_ids": [
        "G14",
        "G15",
        "G16"
      ],
      "profile": "ConceptNet 5.7 assertion/API model with its documented relation vocabulary",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-009",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2a",
      "result": 1,
      "observed": "Term labels give English entry points.",
      "source_ids": [
        "G14",
        "G15",
        "G16"
      ],
      "profile": "ConceptNet 5.7 assertion/API model with its documented relation vocabulary",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-009",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2b",
      "result": 1,
      "observed": "Synonym relations provide a declared alternative-expression route.",
      "source_ids": [
        "G14",
        "G15",
        "G16"
      ],
      "profile": "ConceptNet 5.7 assertion/API model with its documented relation vocabulary",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-009",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2c",
      "result": 1,
      "observed": "Optional POS/sense-qualified URIs preserve distinctions where supplied; universal disambiguation is not claimed.",
      "source_ids": [
        "G14",
        "G15",
        "G16"
      ],
      "profile": "ConceptNet 5.7 assertion/API model with its documented relation vocabulary",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-009",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2d",
      "result": 1,
      "observed": "ExternalURL and source identifiers connect external resources.",
      "source_ids": [
        "G14",
        "G15",
        "G16"
      ],
      "profile": "ConceptNet 5.7 assertion/API model with its documented relation vocabulary",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-009",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3a",
      "result": 1,
      "observed": "Relations retain their intended orientation.",
      "source_ids": [
        "G14",
        "G15",
        "G16"
      ],
      "profile": "ConceptNet 5.7 assertion/API model with its documented relation vocabulary",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-009",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3b",
      "result": 1,
      "observed": "Shared term URIs support joining recorded links.",
      "source_ids": [
        "G14",
        "G15",
        "G16"
      ],
      "profile": "ConceptNet 5.7 assertion/API model with its documented relation vocabulary",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-009",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3c",
      "result": 1,
      "observed": "Symmetric relation declarations prevent arbitrary reversal.",
      "source_ids": [
        "G14",
        "G15",
        "G16"
      ],
      "profile": "ConceptNet 5.7 assertion/API model with its documented relation vocabulary",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-009",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3d",
      "result": 0,
      "observed": "The native term graph does not supply a machine-inspectable domain/range validation schema for these requests.",
      "source_ids": [
        "G14",
        "G15",
        "G16"
      ],
      "profile": "ConceptNet 5.7 assertion/API model with its documented relation vocabulary",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-009",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4a",
      "result": 1,
      "observed": "Assertion IDs locate native evidence.",
      "source_ids": [
        "G14",
        "G15",
        "G16"
      ],
      "profile": "ConceptNet 5.7 assertion/API model with its documented relation vocabulary",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-009",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4b",
      "result": 1,
      "observed": "Sources/dataset fields identify contributions beyond the project homepage.",
      "source_ids": [
        "G14",
        "G15",
        "G16"
      ],
      "profile": "ConceptNet 5.7 assertion/API model with its documented relation vocabulary",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-009",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4c",
      "result": 1,
      "observed": "Edge weight is exposed with its strength interpretation, not a truth probability.",
      "source_ids": [
        "G14",
        "G15",
        "G16"
      ],
      "profile": "ConceptNet 5.7 assertion/API model with its documented relation vocabulary",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-009",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4d",
      "result": 1,
      "observed": "Source filters and contribution metadata support source-aware evidence inspection.",
      "source_ids": [
        "G14",
        "G15",
        "G16"
      ],
      "profile": "ConceptNet 5.7 assertion/API model with its documented relation vocabulary",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-010",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1a",
      "result": 1,
      "observed": "Integrated node/relation/node rows identify assertions.",
      "source_ids": [
        "G17",
        "G18",
        "G15",
        "G16"
      ],
      "profile": "CSKG 1.0 cskg.tsv release and its published relation/source interpretation; no later confidence enrichment or embeddings credited",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-010",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1b",
      "result": 0,
      "observed": "The credited TSV lacks general fact-qualifier role bundles; sentence text does not supply them automatically.",
      "source_ids": [
        "G17",
        "G18",
        "G15",
        "G16"
      ],
      "profile": "CSKG 1.0 cskg.tsv release and its published relation/source interpretation; no later confidence enrichment or embeddings credited",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-010",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1c",
      "result": 1,
      "observed": "Imported negative ConceptNet-style relation types retain explicit polarity.",
      "source_ids": [
        "G17",
        "G18",
        "G15",
        "G16"
      ],
      "profile": "CSKG 1.0 cskg.tsv release and its published relation/source interpretation; no later confidence enrichment or embeddings credited",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-010",
      "family": "F4",
      "criterion": "C1",
      "test_id": "F4-C1d",
      "result": 0,
      "observed": "The core contract contains no separate unknown-value versus known-none state.",
      "source_ids": [
        "G17",
        "G18",
        "G15",
        "G16"
      ],
      "profile": "CSKG 1.0 cskg.tsv release and its published relation/source interpretation; no later confidence enrichment or embeddings credited",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-010",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2a",
      "result": 1,
      "observed": "Node labels expose lexical entry points.",
      "source_ids": [
        "G17",
        "G18",
        "G15",
        "G16"
      ],
      "profile": "CSKG 1.0 cskg.tsv release and its published relation/source interpretation; no later confidence enrichment or embeddings credited",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-010",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2b",
      "result": 1,
      "observed": "Alignment/equivalence links and merged identifiers supply alternatives.",
      "source_ids": [
        "G17",
        "G18",
        "G15",
        "G16"
      ],
      "profile": "CSKG 1.0 cskg.tsv release and its published relation/source interpretation; no later confidence enrichment or embeddings credited",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-010",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2c",
      "result": 1,
      "observed": "Source-qualified IDs and labels preserve supplied reference contexts.",
      "source_ids": [
        "G17",
        "G18",
        "G15",
        "G16"
      ],
      "profile": "CSKG 1.0 cskg.tsv release and its published relation/source interpretation; no later confidence enrichment or embeddings credited",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-010",
      "family": "F4",
      "criterion": "C2",
      "test_id": "F4-C2d",
      "result": 1,
      "observed": "Source identifiers and alignments retain external reference routes.",
      "source_ids": [
        "G17",
        "G18",
        "G15",
        "G16"
      ],
      "profile": "CSKG 1.0 cskg.tsv release and its published relation/source interpretation; no later confidence enrichment or embeddings credited",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-010",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3a",
      "result": 1,
      "observed": "Relation labels/URIs retain source orientation.",
      "source_ids": [
        "G17",
        "G18",
        "G15",
        "G16"
      ],
      "profile": "CSKG 1.0 cskg.tsv release and its published relation/source interpretation; no later confidence enrichment or embeddings credited",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-010",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3b",
      "result": 1,
      "observed": "The documented keys–piano–music records share a joinable node.",
      "source_ids": [
        "G17",
        "G18",
        "G15",
        "G16"
      ],
      "profile": "CSKG 1.0 cskg.tsv release and its published relation/source interpretation; no later confidence enrichment or embeddings credited",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-010",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3c",
      "result": 1,
      "observed": "Inherited source relation definitions govern symmetric/converse interpretations.",
      "source_ids": [
        "G17",
        "G18",
        "G15",
        "G16"
      ],
      "profile": "CSKG 1.0 cskg.tsv release and its published relation/source interpretation; no later confidence enrichment or embeddings credited",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-010",
      "family": "F4",
      "criterion": "C3",
      "test_id": "F4-C3d",
      "result": 0,
      "observed": "The core TSV does not supply a relation-level machine-inspectable domain/range validator.",
      "source_ids": [
        "G17",
        "G18",
        "G15",
        "G16"
      ],
      "profile": "CSKG 1.0 cskg.tsv release and its published relation/source interpretation; no later confidence enrichment or embeddings credited",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-010",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4a",
      "result": 1,
      "observed": "Each released row has a locator/ID.",
      "source_ids": [
        "G17",
        "G18",
        "G15",
        "G16"
      ],
      "profile": "CSKG 1.0 cskg.tsv release and its published relation/source interpretation; no later confidence enrichment or embeddings credited",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-010",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4b",
      "result": 1,
      "observed": "The source column preserves component attribution where populated.",
      "source_ids": [
        "G17",
        "G18",
        "G15",
        "G16"
      ],
      "profile": "CSKG 1.0 cskg.tsv release and its published relation/source interpretation; no later confidence enrichment or embeddings credited",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-010",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4c",
      "result": 0,
      "observed": "The declared cskg.tsv row contract contains identifiers, labels, sources and sentences but no rank/confidence/weight column. Embedding vectors and later enrichment files are outside this fixed release profile; their existence is not assertion-confidence evidence.",
      "source_ids": [
        "G17",
        "G18",
        "G19"
      ],
      "profile": "CSKG 1.0 cskg.tsv release and its published relation/source interpretation; no later confidence enrichment or embeddings credited",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F4-010",
      "family": "F4",
      "criterion": "C4",
      "test_id": "F4-C4d",
      "result": 1,
      "observed": "Source and relation metadata can be used to inspect/filter evidence.",
      "source_ids": [
        "G17",
        "G18",
        "G15",
        "G16"
      ],
      "profile": "CSKG 1.0 cskg.tsv release and its published relation/source interpretation; no later confidence enrichment or embeddings credited",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-001",
      "family": "F5",
      "criterion": "C1",
      "test_id": "F5-C1a",
      "result": 1,
      "observed": "Synset/sense IDs distinguish meanings from lexical forms.",
      "source_ids": [
        "L01",
        "L02"
      ],
      "profile": "Published API v9/V5_3 example model: synsets, sense sources, glosses, examples and edge pointers; no account execution",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-001",
      "family": "F5",
      "criterion": "C1",
      "test_id": "F5-C1b",
      "result": 0,
      "observed": "The credited synset schema is not a frame-element inventory of named semantic participants.",
      "source_ids": [
        "L01",
        "L02"
      ],
      "profile": "Published API v9/V5_3 example model: synsets, sense sources, glosses, examples and edge pointers; no account execution",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-001",
      "family": "F5",
      "criterion": "C1",
      "test_id": "F5-C1c",
      "result": 0,
      "observed": "A set of senses/glosses/edges is not a nested compositional definition inside one sense.",
      "source_ids": [
        "L01",
        "L02"
      ],
      "profile": "Published API v9/V5_3 example model: synsets, sense sources, glosses, examples and edge pointers; no account execution",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-001",
      "family": "F5",
      "criterion": "C1",
      "test_id": "F5-C1d",
      "result": 1,
      "observed": "The synset model distinguishes named-entity and concept types.",
      "source_ids": [
        "L01",
        "L02"
      ],
      "profile": "Published API v9/V5_3 example model: synsets, sense sources, glosses, examples and edge pointers; no account execution",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-001",
      "family": "F5",
      "criterion": "C2",
      "test_id": "F5-C2a",
      "result": 1,
      "observed": "English lemmas map to lists of synset IDs.",
      "source_ids": [
        "L01",
        "L02"
      ],
      "profile": "Published API v9/V5_3 example model: synsets, sense sources, glosses, examples and edge pointers; no account execution",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-001",
      "family": "F5",
      "criterion": "C2",
      "test_id": "F5-C2b",
      "result": 1,
      "observed": "Synonym senses are grouped, with source/quality labels retained rather than accepting every near-synonym as exact.",
      "source_ids": [
        "L01",
        "L02"
      ],
      "profile": "Published API v9/V5_3 example model: synsets, sense sources, glosses, examples and edge pointers; no account execution",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-001",
      "family": "F5",
      "criterion": "C2",
      "test_id": "F5-C2c",
      "result": 1,
      "observed": "Glosses and categories provide interpretation context.",
      "source_ids": [
        "L01",
        "L02"
      ],
      "profile": "Published API v9/V5_3 example model: synsets, sense sources, glosses, examples and edge pointers; no account execution",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-001",
      "family": "F5",
      "criterion": "C2",
      "test_id": "F5-C2d",
      "result": 1,
      "observed": "WordNet and encyclopedic source identifiers can resolve into the native network.",
      "source_ids": [
        "L01",
        "L02"
      ],
      "profile": "Published API v9/V5_3 example model: synsets, sense sources, glosses, examples and edge pointers; no account execution",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-001",
      "family": "F5",
      "criterion": "C3",
      "test_id": "F5-C3a",
      "result": 1,
      "observed": "Typed hypernym/semantic hierarchy links are supplied.",
      "source_ids": [
        "L01",
        "L02"
      ],
      "profile": "Published API v9/V5_3 example model: synsets, sense sources, glosses, examples and edge pointers; no account execution",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-001",
      "family": "F5",
      "criterion": "C3",
      "test_id": "F5-C3b",
      "result": 1,
      "observed": "Nonhierarchical semantic pointers are available.",
      "source_ids": [
        "L01",
        "L02"
      ],
      "profile": "Published API v9/V5_3 example model: synsets, sense sources, glosses, examples and edge pointers; no account execution",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-001",
      "family": "F5",
      "criterion": "C3",
      "test_id": "F5-C3c",
      "result": 1,
      "observed": "Pointer direction/type is defined rather than inferred from connectivity.",
      "source_ids": [
        "L01",
        "L02"
      ],
      "profile": "Published API v9/V5_3 example model: synsets, sense sources, glosses, examples and edge pointers; no account execution",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-001",
      "family": "F5",
      "criterion": "C3",
      "test_id": "F5-C3d",
      "result": 0,
      "observed": "The credited contract does not provide FrameNet-style inter-frame role alignment.",
      "source_ids": [
        "L01",
        "L02"
      ],
      "profile": "Published API v9/V5_3 example model: synsets, sense sources, glosses, examples and edge pointers; no account execution",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-001",
      "family": "F5",
      "criterion": "C4",
      "test_id": "F5-C4a",
      "result": 1,
      "observed": "Gloss/meaning content is tied to a synset.",
      "source_ids": [
        "L01",
        "L02"
      ],
      "profile": "Published API v9/V5_3 example model: synsets, sense sources, glosses, examples and edge pointers; no account execution",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-001",
      "family": "F5",
      "criterion": "C4",
      "test_id": "F5-C4b",
      "result": 1,
      "observed": "English examples are exposed by the documented response.",
      "source_ids": [
        "L01",
        "L02"
      ],
      "profile": "Published API v9/V5_3 example model: synsets, sense sources, glosses, examples and edge pointers; no account execution",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-001",
      "family": "F5",
      "criterion": "C4",
      "test_id": "F5-C4c",
      "result": 1,
      "observed": "Gloss/example source information identifies upstream contributions.",
      "source_ids": [
        "L01",
        "L02"
      ],
      "profile": "Published API v9/V5_3 example model: synsets, sense sources, glosses, examples and edge pointers; no account execution",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-001",
      "family": "F5",
      "criterion": "C4",
      "test_id": "F5-C4d",
      "result": 1,
      "observed": "The API distinguishes directed hypernym/is-a and instance-of pointers from generic relatedness; BabelPointer defines their types. Only the corresponding type inclusion is justified, not arbitrary reasoning from a relatedness edge.",
      "source_ids": [
        "L01",
        "L02",
        "L09"
      ],
      "profile": "Published API v9/V5_3 example model: synsets, sense sources, glosses, examples and edge pointers; no account execution",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-002",
      "family": "F5",
      "criterion": "C1",
      "test_id": "F5-C1a",
      "result": 1,
      "observed": "A lexical unit associates a word sense with a frame.",
      "source_ids": [
        "L03",
        "L04"
      ],
      "profile": "Berkeley FrameNet 1.7 native lexical-unit, frame, FE, relation and annotation model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-002",
      "family": "F5",
      "criterion": "C1",
      "test_id": "F5-C1b",
      "result": 1,
      "observed": "Named frame elements distinguish participants and circumstances.",
      "source_ids": [
        "L03",
        "L04"
      ],
      "profile": "Berkeley FrameNet 1.7 native lexical-unit, frame, FE, relation and annotation model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-002",
      "family": "F5",
      "criterion": "C1",
      "test_id": "F5-C1c",
      "result": 0,
      "observed": "Flat FE slots plus inter-frame relations are not a nested sememe-style compositional definition of one lexical sense.",
      "source_ids": [
        "L03",
        "L04"
      ],
      "profile": "Berkeley FrameNet 1.7 native lexical-unit, frame, FE, relation and annotation model",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-002",
      "family": "F5",
      "criterion": "C1",
      "test_id": "F5-C1d",
      "result": 0,
      "observed": "The native frame/LU model has no concept-versus-named-instance category corresponding to this request.",
      "source_ids": [
        "L03",
        "L04"
      ],
      "profile": "Berkeley FrameNet 1.7 native lexical-unit, frame, FE, relation and annotation model",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-002",
      "family": "F5",
      "criterion": "C2",
      "test_id": "F5-C2a",
      "result": 1,
      "observed": "English lexical units provide sense-to-frame entry.",
      "source_ids": [
        "L03",
        "L04"
      ],
      "profile": "Berkeley FrameNet 1.7 native lexical-unit, frame, FE, relation and annotation model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-002",
      "family": "F5",
      "criterion": "C2",
      "test_id": "F5-C2b",
      "result": 0,
      "observed": "Membership in the same frame does not assert lexical synonymy.",
      "source_ids": [
        "L03",
        "L04"
      ],
      "profile": "Berkeley FrameNet 1.7 native lexical-unit, frame, FE, relation and annotation model",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-002",
      "family": "F5",
      "criterion": "C2",
      "test_id": "F5-C2c",
      "result": 1,
      "observed": "Frame definitions and annotated examples supply disambiguating context.",
      "source_ids": [
        "L03",
        "L04"
      ],
      "profile": "Berkeley FrameNet 1.7 native lexical-unit, frame, FE, relation and annotation model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-002",
      "family": "F5",
      "criterion": "C2",
      "test_id": "F5-C2d",
      "result": 0,
      "observed": "An independent encyclopedic/lexical-ID mapping layer is not included in native 1.7 records.",
      "source_ids": [
        "L03",
        "L04"
      ],
      "profile": "Berkeley FrameNet 1.7 native lexical-unit, frame, FE, relation and annotation model",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-002",
      "family": "F5",
      "criterion": "C3",
      "test_id": "F5-C3a",
      "result": 1,
      "observed": "Frame inheritance is explicit.",
      "source_ids": [
        "L03",
        "L04"
      ],
      "profile": "Berkeley FrameNet 1.7 native lexical-unit, frame, FE, relation and annotation model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-002",
      "family": "F5",
      "criterion": "C3",
      "test_id": "F5-C3b",
      "result": 1,
      "observed": "Perspective, causative and other inter-frame relations are typed.",
      "source_ids": [
        "L03",
        "L04"
      ],
      "profile": "Berkeley FrameNet 1.7 native lexical-unit, frame, FE, relation and annotation model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-002",
      "family": "F5",
      "criterion": "C3",
      "test_id": "F5-C3c",
      "result": 1,
      "observed": "Super/subframe direction and relation types are defined.",
      "source_ids": [
        "L03",
        "L04"
      ],
      "profile": "Berkeley FrameNet 1.7 native lexical-unit, frame, FE, relation and annotation model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-002",
      "family": "F5",
      "criterion": "C3",
      "test_id": "F5-C3d",
      "result": 1,
      "observed": "FE correspondences align participant roles across related frames.",
      "source_ids": [
        "L03",
        "L04"
      ],
      "profile": "Berkeley FrameNet 1.7 native lexical-unit, frame, FE, relation and annotation model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-002",
      "family": "F5",
      "criterion": "C4",
      "test_id": "F5-C4a",
      "result": 1,
      "observed": "Frames and FEs have source definitions.",
      "source_ids": [
        "L03",
        "L04"
      ],
      "profile": "Berkeley FrameNet 1.7 native lexical-unit, frame, FE, relation and annotation model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-002",
      "family": "F5",
      "criterion": "C4",
      "test_id": "F5-C4b",
      "result": 1,
      "observed": "Annotated sentences provide contextual usage.",
      "source_ids": [
        "L03",
        "L04"
      ],
      "profile": "Berkeley FrameNet 1.7 native lexical-unit, frame, FE, relation and annotation model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-002",
      "family": "F5",
      "criterion": "C4",
      "test_id": "F5-C4c",
      "result": 1,
      "observed": "Sentence/annotation/document identities connect evidence to the supplying corpus records.",
      "source_ids": [
        "L03",
        "L04"
      ],
      "profile": "Berkeley FrameNet 1.7 native lexical-unit, frame, FE, relation and annotation model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-002",
      "family": "F5",
      "criterion": "C4",
      "test_id": "F5-C4d",
      "result": 1,
      "observed": "Declared inheritance and causative/perspective relations support their limited semantic implications.",
      "source_ids": [
        "L03",
        "L04"
      ],
      "profile": "Berkeley FrameNet 1.7 native lexical-unit, frame, FE, relation and annotation model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-003",
      "family": "F5",
      "criterion": "C1",
      "test_id": "F5-C1a",
      "result": 1,
      "observed": "Numbered senses are distinct from Chinese/English word forms.",
      "source_ids": [
        "L05"
      ],
      "profile": "OpenHowNet core dictionary and sememe relations; separate BabelNet-annotation extension is reported but not merged into the core profile",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-003",
      "family": "F5",
      "criterion": "C1",
      "test_id": "F5-C1b",
      "result": 1,
      "observed": "Roles such as agent and PatientProduct are explicit in sememe trees.",
      "source_ids": [
        "L05"
      ],
      "profile": "OpenHowNet core dictionary and sememe relations; separate BabelNet-annotation extension is reported but not merged into the core profile",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-003",
      "family": "F5",
      "criterion": "C1",
      "test_id": "F5-C1c",
      "result": 1,
      "observed": "No.244401 and the computer/SpeBrand examples contain nested compositional structure.",
      "source_ids": [
        "L05"
      ],
      "profile": "OpenHowNet core dictionary and sememe relations; separate BabelNet-annotation extension is reported but not merged into the core profile",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-003",
      "family": "F5",
      "criterion": "C1",
      "test_id": "F5-C1d",
      "result": 1,
      "observed": "SpeBrand marks a specific brand interpretation, distinguished from fruit/tree senses in the published examples.",
      "source_ids": [
        "L05"
      ],
      "profile": "OpenHowNet core dictionary and sememe relations; separate BabelNet-annotation extension is reported but not merged into the core profile",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-003",
      "family": "F5",
      "criterion": "C2",
      "test_id": "F5-C2a",
      "result": 1,
      "observed": "get_sense associates an English word with numbered meanings.",
      "source_ids": [
        "L05"
      ],
      "profile": "OpenHowNet core dictionary and sememe relations; separate BabelNet-annotation extension is reported but not merged into the core profile",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-003",
      "family": "F5",
      "criterion": "C2",
      "test_id": "F5-C2b",
      "result": 0,
      "observed": "The similarly named synonym method groups identical sememe descriptions; its apple-tree example also returns pear/hawthorn and is not exact lexical equivalence.",
      "source_ids": [
        "L05"
      ],
      "profile": "OpenHowNet core dictionary and sememe relations; separate BabelNet-annotation extension is reported but not merged into the core profile",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-003",
      "family": "F5",
      "criterion": "C2",
      "test_id": "F5-C2c",
      "result": 1,
      "observed": "English-named sememes and role trees provide meaning-bearing context.",
      "source_ids": [
        "L05"
      ],
      "profile": "OpenHowNet core dictionary and sememe relations; separate BabelNet-annotation extension is reported but not merged into the core profile",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-003",
      "family": "F5",
      "criterion": "C2",
      "test_id": "F5-C2d",
      "result": 0,
      "observed": "The basic core is not the separate BabelNet synset-alignment extension described under Advanced Features.",
      "source_ids": [
        "L05"
      ],
      "profile": "OpenHowNet core dictionary and sememe relations; separate BabelNet-annotation extension is reported but not merged into the core profile",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-003",
      "family": "F5",
      "criterion": "C3",
      "test_id": "F5-C3a",
      "result": 1,
      "observed": "The published FormValue/round example identifies sememe hyponymy.",
      "source_ids": [
        "L05"
      ],
      "profile": "OpenHowNet core dictionary and sememe relations; separate BabelNet-annotation extension is reported but not merged into the core profile",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-003",
      "family": "F5",
      "criterion": "C3",
      "test_id": "F5-C3b",
      "result": 1,
      "observed": "Role and other sememe relations add nonhierarchical links.",
      "source_ids": [
        "L05"
      ],
      "profile": "OpenHowNet core dictionary and sememe relations; separate BabelNet-annotation extension is reported but not merged into the core profile",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-003",
      "family": "F5",
      "criterion": "C3",
      "test_id": "F5-C3c",
      "result": 1,
      "observed": "Triples and explicit role orientation preserve direction.",
      "source_ids": [
        "L05"
      ],
      "profile": "OpenHowNet core dictionary and sememe relations; separate BabelNet-annotation extension is reported but not merged into the core profile",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-003",
      "family": "F5",
      "criterion": "C3",
      "test_id": "F5-C3d",
      "result": 0,
      "observed": "The core has no inter-frame participant-alignment table.",
      "source_ids": [
        "L05"
      ],
      "profile": "OpenHowNet core dictionary and sememe relations; separate BabelNet-annotation extension is reported but not merged into the core profile",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-003",
      "family": "F5",
      "criterion": "C4",
      "test_id": "F5-C4a",
      "result": 1,
      "observed": "Sense IDs locate their sememe definitions.",
      "source_ids": [
        "L05"
      ],
      "profile": "OpenHowNet core dictionary and sememe relations; separate BabelNet-annotation extension is reported but not merged into the core profile",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-003",
      "family": "F5",
      "criterion": "C4",
      "test_id": "F5-C4b",
      "result": null,
      "observed": "An E_E field is defined, but the inspected concrete example is empty; a populated English usage witness was not verified.",
      "source_ids": [
        "L05"
      ],
      "profile": "OpenHowNet core dictionary and sememe relations; separate BabelNet-annotation extension is reported but not merged into the core profile",
      "evidence_kind": "unresolved_documentary_evidence",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-003",
      "family": "F5",
      "criterion": "C4",
      "test_id": "F5-C4c",
      "result": 0,
      "observed": "Core word/DEF/example fields do not include an upstream corpus-document citation for each English example or definition.",
      "source_ids": [
        "L05"
      ],
      "profile": "OpenHowNet core dictionary and sememe relations; separate BabelNet-annotation extension is reported but not merged into the core profile",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-003",
      "family": "F5",
      "criterion": "C4",
      "test_id": "F5-C4d",
      "result": 1,
      "observed": "Sememe hyponymy licenses the corresponding narrow-to-broad interpretation, not arbitrary deductive reasoning.",
      "source_ids": [
        "L05"
      ],
      "profile": "OpenHowNet core dictionary and sememe relations; separate BabelNet-annotation extension is reported but not merged into the core profile",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-014",
      "family": "F5",
      "criterion": "C1",
      "test_id": "F5-C1a",
      "result": 1,
      "observed": "Sense keys and synsets distinguish lexical meanings from strings.",
      "source_ids": [
        "L06",
        "L07",
        "L08"
      ],
      "profile": "Princeton WordNet 3.0 native sense/synset, pointer and gloss model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-014",
      "family": "F5",
      "criterion": "C1",
      "test_id": "F5-C1b",
      "result": 0,
      "observed": "Verb sentence frames are syntactic patterns, not named semantic participants/FE roles.",
      "source_ids": [
        "L06",
        "L07",
        "L08"
      ],
      "profile": "Princeton WordNet 3.0 native sense/synset, pointer and gloss model",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-014",
      "family": "F5",
      "criterion": "C1",
      "test_id": "F5-C1c",
      "result": 0,
      "observed": "The native synset/gloss format does not supply nested compositional sememe trees.",
      "source_ids": [
        "L06",
        "L07",
        "L08"
      ],
      "profile": "Princeton WordNet 3.0 native sense/synset, pointer and gloss model",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-014",
      "family": "F5",
      "criterion": "C1",
      "test_id": "F5-C1d",
      "result": 1,
      "observed": "Instance-hypernym pointers distinguish named instances from kinds.",
      "source_ids": [
        "L06",
        "L07",
        "L08"
      ],
      "profile": "Princeton WordNet 3.0 native sense/synset, pointer and gloss model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-014",
      "family": "F5",
      "criterion": "C2",
      "test_id": "F5-C2a",
      "result": 1,
      "observed": "The lexical index maps words to synsets.",
      "source_ids": [
        "L06",
        "L07",
        "L08"
      ],
      "profile": "Princeton WordNet 3.0 native sense/synset, pointer and gloss model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-014",
      "family": "F5",
      "criterion": "C2",
      "test_id": "F5-C2b",
      "result": 1,
      "observed": "Synsets explicitly group synonymous lexical senses.",
      "source_ids": [
        "L06",
        "L07",
        "L08"
      ],
      "profile": "Princeton WordNet 3.0 native sense/synset, pointer and gloss model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-014",
      "family": "F5",
      "criterion": "C2",
      "test_id": "F5-C2c",
      "result": 1,
      "observed": "Definitions and example text supply context.",
      "source_ids": [
        "L06",
        "L07",
        "L08"
      ],
      "profile": "Princeton WordNet 3.0 native sense/synset, pointer and gloss model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-014",
      "family": "F5",
      "criterion": "C2",
      "test_id": "F5-C2d",
      "result": 0,
      "observed": "WordNet’s own sense keys are not an independent external lexical/encyclopedic alignment layer.",
      "source_ids": [
        "L06",
        "L07",
        "L08"
      ],
      "profile": "Princeton WordNet 3.0 native sense/synset, pointer and gloss model",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-014",
      "family": "F5",
      "criterion": "C3",
      "test_id": "F5-C3a",
      "result": 1,
      "observed": "Hypernym/hyponym relations are native.",
      "source_ids": [
        "L06",
        "L07",
        "L08"
      ],
      "profile": "Princeton WordNet 3.0 native sense/synset, pointer and gloss model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-014",
      "family": "F5",
      "criterion": "C3",
      "test_id": "F5-C3b",
      "result": 1,
      "observed": "Meronymy, antonymy and other typed pointers add nonhierarchical links.",
      "source_ids": [
        "L06",
        "L07",
        "L08"
      ],
      "profile": "Princeton WordNet 3.0 native sense/synset, pointer and gloss model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-014",
      "family": "F5",
      "criterion": "C3",
      "test_id": "F5-C3c",
      "result": 1,
      "observed": "Pointer types define direction and converse meanings.",
      "source_ids": [
        "L06",
        "L07",
        "L08"
      ],
      "profile": "Princeton WordNet 3.0 native sense/synset, pointer and gloss model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-014",
      "family": "F5",
      "criterion": "C3",
      "test_id": "F5-C3d",
      "result": 0,
      "observed": "There is no inter-frame participant correspondence inventory.",
      "source_ids": [
        "L06",
        "L07",
        "L08"
      ],
      "profile": "Princeton WordNet 3.0 native sense/synset, pointer and gloss model",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-014",
      "family": "F5",
      "criterion": "C4",
      "test_id": "F5-C4a",
      "result": 1,
      "observed": "A native synset returns a definition.",
      "source_ids": [
        "L06",
        "L07",
        "L08"
      ],
      "profile": "Princeton WordNet 3.0 native sense/synset, pointer and gloss model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-014",
      "family": "F5",
      "criterion": "C4",
      "test_id": "F5-C4b",
      "result": 1,
      "observed": "Many gloss fields include English usage examples.",
      "source_ids": [
        "L06",
        "L07",
        "L08"
      ],
      "profile": "Princeton WordNet 3.0 native sense/synset, pointer and gloss model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-014",
      "family": "F5",
      "criterion": "C4",
      "test_id": "F5-C4c",
      "result": 0,
      "observed": "The core database does not provide upstream source-document/corpus IDs for each gloss/example; its native offset is already credited as a locator.",
      "source_ids": [
        "L06",
        "L07",
        "L08"
      ],
      "profile": "Princeton WordNet 3.0 native sense/synset, pointer and gloss model",
      "evidence_kind": "bounded_profile_limitation",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    },
    {
      "candidate_id": "F5-014",
      "family": "F5",
      "criterion": "C4",
      "test_id": "F5-C4d",
      "result": 1,
      "observed": "Entailment and cause pointers have documented limited semantics.",
      "source_ids": [
        "L06",
        "L07",
        "L08"
      ],
      "profile": "Princeton WordNet 3.0 native sense/synset, pointer and gloss model",
      "evidence_kind": "source_specification_and_example",
      "reviewer": "single_assessor_source_review",
      "independent_review": false
    }
  ],
  "quality_review_note": "Quality review corrected UDC F1-C4c from supported to unresolved, clarified three request boundaries without changing their coded outcomes, removed a contradictory CSKG weight reference, and hardened validation and numerical-error accounting. Rankings remain exploratory single-assessor documentary results.",
  "quality_review_amendments": [
    {
      "candidate_id": "F1-003",
      "test_id": "F1-C4c",
      "previous_result": 1,
      "result": null,
      "reason": "General rules do not establish the specified Summary-specific redirection/exclusion witness."
    },
    {
      "test_id": "F1-C2d",
      "change": "Clarified incoming record-to-subject access; distinct from C4d outgoing evidence retrieval. No recoded outcomes."
    },
    {
      "test_id": "F2-C2d",
      "change": "Clarified complete qualified postcoordinate anchor service rather than an already established heading lookup. No recoded outcomes."
    },
    {
      "test_id": "F3-C1d",
      "change": "Clarified variable-clause versus fixed OWL template boundary, consistent with the recorded assessments. No recoded outcomes."
    },
    {
      "candidate_id": "F4-010",
      "change": "Removed the contradictory suggestion that the assessed TSV supplies assertion weights."
    }
  ]
}
''')

# --- Numerical implementation: generated scores, never hard-coded leaders. ---
import csv
import hashlib
import itertools
import math
import os
from pathlib import Path
import platform
import sys
import time
import numpy as np

# Edit only these settings for a different declared analysis. The shipped values
# reproduce the Word document. An edited audit must be supplied as a whole JSON bundle.
AUDIT_BUNDLE_PATH = None
BASELINE_DRAWS = 1_000_000
SENSITIVITY_DRAWS = 300_000
CHECK_SENSITIVITY_DRAWS = 100_000
CHALLENGE_DRAWS = 50_000
BATCH_SIZE = 20_000
SEED = 20261013
MC_FAMILYWISE_ERROR = 0.01
RUN_CHECK_SENSITIVITY = True
RUN_EVIDENCE_CHALLENGES = True
TIE_DECIMALS = 12
# The error guard concerns finite simulation, NOT source truth or model adequacy.
# Conservative floor. The run increases it if the actual stochastic mean count
# (baseline, sensitivities, completions and one-cell challenges) is larger.
MC_GUARD_MEANS = 10_000



def require_text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{label} must be nonempty text.')


def require_int(value, label, minimum=1):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, np.integer)) or value < minimum:
        raise ValueError(f'{label} must be an integer >= {minimum}.')
    return int(value)


def check_source_ids(value, sources, label):
    if not isinstance(value, list) or not value or any(not isinstance(s, str) or s not in sources for s in value):
        raise ValueError(f'{label} needs a nonempty list of known source IDs.')
    if len(set(value)) != len(value):
        raise ValueError(f'{label} contains duplicate source IDs.')


def checked_bits(bits, allow_unknown):
    b = np.asarray(bits, dtype=float)
    if b.ndim != 3 or b.shape[0] < 1 or b.shape[1:] != (4,4):
        raise ValueError('Request outcomes must have shape (candidates, 4, 4).')
    allowed = (b == 0) | (b == 1)
    if allow_unknown:
        allowed |= np.isnan(b)
    if not np.all(allowed):
        raise ValueError('Outcomes must be 0 or 1, with NaN only for explicitly unresolved cells.')
    return b


def checked_scores(scores):
    s = np.asarray(scores, dtype=float)
    if s.ndim == 1: s = s[None,:]
    if s.ndim != 2 or min(s.shape) < 1 or not np.all(np.isfinite(s)):
        raise ValueError('Ranking scores must be a nonempty finite 2-D matrix.')
    require_int(TIE_DECIMALS, 'TIE_DECIMALS', minimum=0)
    if TIE_DECIMALS > 15:
        raise ValueError('TIE_DECIMALS must not exceed 15 for float64 scoring.')
    with np.errstate(over='ignore', invalid='ignore'):
        rounded = np.round(s, TIE_DECIMALS)
    if not np.all(np.isfinite(rounded)):
        raise ValueError('Score magnitude is unsafe for the requested rounding precision.')
    return rounded


def load_json_strict(path):
    def pairs(items):
        out = {}
        for key, value in items:
            if key in out: raise ValueError(f'Duplicate JSON key: {key}.')
            out[key] = value
        return out
    def invalid_constant(value):
        raise ValueError(f'Nonfinite JSON constant is not allowed: {value}.')
    return json.loads(Path(path).read_text(encoding='utf-8-sig'),
                      object_pairs_hook=pairs, parse_constant=invalid_constant)


def guard_mean_count(bundle, scenarios):
    """Union-bound count for every reported stochastic first-rank estimate.

    Completions are possibilities, not independent samples; the union bound does
    not require independence between estimates. It does require independent
    weight draws within each simulation stream.
    """
    total = 0
    stochastic_scenarios = sum('fixed' not in opt for _,opt,_ in scenarios)
    for family in bundle['protocol']['family_names']:
        panel,bits = family_bits(bundle,family)
        unknown = int(np.isnan(bits).sum())
        if unknown > 12: raise ValueError('More than 12 unresolved cells in a family.')
        means = len(panel) * (2 ** unknown)
        total += means * stochastic_scenarios
        if RUN_EVIDENCE_CHALLENGES:
            total += means * int(np.isfinite(bits).sum())
    return total, max(require_int(MC_GUARD_MEANS, 'MC_GUARD_MEANS'), total)


def implementation_digest():
    """Hash the executed function source identically in a script or IPython cell."""
    import inspect
    funcs = [(name,obj) for name,obj in globals().items()
             if inspect.isfunction(obj) and getattr(obj, '__module__', None) == __name__]
    try:
        return digest({name: inspect.getsource(obj) for name,obj in sorted(funcs)})
    except (OSError, TypeError):
        return None  # Explicitly unavailable, never a fabricated code hash.


def validate_settings():
    for name in ('BASELINE_DRAWS','SENSITIVITY_DRAWS','CHECK_SENSITIVITY_DRAWS',
                 'CHALLENGE_DRAWS','BATCH_SIZE','MC_GUARD_MEANS'):
        require_int(globals()[name], name)
    require_int(SEED, 'SEED', minimum=0)
    for name in ('RUN_CHECK_SENSITIVITY','RUN_EVIDENCE_CHALLENGES'):
        if type(globals()[name]) is not bool:
            raise ValueError(f'{name} must be Boolean.')
    allowance(BASELINE_DRAWS)

def canonical(obj):
    """Stable JSON serialization of finite, JSON-compatible protocol data."""
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':'),
                      allow_nan=False).encode('utf-8')


def digest(obj):
    return hashlib.sha256(canonical(obj)).hexdigest()


def validate(bundle):
    """Reject internally inconsistent audit inputs before any score is calculated.

    Structural validation cannot establish that a citation supports a judgment.
    """
    if not isinstance(bundle, dict):
        raise ValueError('The assessment bundle must be a JSON object.')
    for key in ('panel', 'protocol', 'sources', 'audit'):
        if key not in bundle:
            raise ValueError(f'Missing bundle field: {key}.')
    panel, prot, sources, audit = (bundle['panel'], bundle['protocol'],
                                   bundle['sources'], bundle['audit'])
    if not isinstance(prot, dict) or not isinstance(sources, dict):
        raise ValueError('protocol and sources must be objects.')
    tests = prot.get('tests')
    if any(not isinstance(x, list) for x in (panel, tests, audit)):
        raise ValueError('panel, tests, and audit must be lists.')
    expected = {
        'F1': ['F1-001', 'F1-002', 'F1-003', 'F1-049'],
        'F2': ['F2-001', 'F2-002', 'F2-045'],
        'F3': ['F3-001', 'F3-009', 'F3-029'],
        'F4': ['F4-001', 'F4-002', 'F4-003', 'F4-006', 'F4-009', 'F4-010'],
        'F5': ['F5-001', 'F5-002', 'F5-003', 'F5-014'],
    }
    if type(prot.get('denominator')) is not int or prot['denominator'] != 4:
        raise ValueError('The four-request score requires denominator=4.')
    for flag in ('allow_name_override', 'allow_legacy_scores', 'cross_family_pooling'):
        if prot.get(flag) is not False:
            raise ValueError(f'{flag} must be explicitly false.')
    sv = prot.get('status_values')
    if not isinstance(sv, list) or len(sv) != 3 or type(sv[0]) is not int or type(sv[1]) is not int or sv != [0, 1, None]:
        raise ValueError('Protocol status_values must be [0, 1, null].')
    if not isinstance(prot.get('family_names'), dict) or set(prot['family_names']) != set(expected):
        raise ValueError('Exactly five named families are required.')
    for flag in ('independent_review_completed', 'source_adapters_executed',
                 'raw_source_snapshots_captured'):
        if type(bundle.get(flag)) is not bool:
            raise ValueError(f'{flag} must be an explicit Boolean.')
    for sid, s in sources.items():
        if not isinstance(s, dict) or s.get('source_id') != sid:
            raise ValueError(f'Inconsistent source identifier: {sid}.')
        for key in ('title', 'url', 'locator', 'access_date'):
            require_text(s.get(key), f'sources[{sid}].{key}')
        if not s['url'].startswith(('https://', 'http://', 'local:')):
            raise ValueError(f'Unsupported source locator: {sid}.')
    ids = []
    panel_by_id = {}
    for p in panel:
        if not isinstance(p, dict):
            raise ValueError('Each panel record must be an object.')
        for key in ('candidate_id', 'family', 'resource', 'profile', 'boundary'):
            require_text(p.get(key), f'panel.{key}')
        cid = p['candidate_id']; ids.append(cid); panel_by_id[cid] = p
        if p['family'] != cid[:2]:
            raise ValueError(f'Candidate family mismatch: {cid}.')
        check_source_ids(p.get('source_ids'), sources, f'panel[{cid}]')
    if len(ids) != 20 or len(set(ids)) != 20 or set(ids) != set(sum(expected.values(), [])):
        raise ValueError('The assessment must contain the confirmed 20 unique candidate IDs.')
    if len({p['resource'] for p in panel}) != 20:
        raise ValueError('Resource display names must be distinct.')
    req = {f'{f}-C{i}{j}' for f in expected for i in range(1, 5) for j in 'abcd'}
    test_ids = []
    for t in tests:
        if not isinstance(t, dict):
            raise ValueError('Each request must be an object.')
        tid = t.get('test_id'); test_ids.append(tid)
        if tid not in req or t.get('family') != tid[:2] or t.get('criterion') != tid[3:5]:
            raise ValueError(f'Inconsistent request family/criterion: {tid}.')
        for key in ('obligation', 'pass_rule', 'no_rule', 'unknown_rule'):
            require_text(t.get(key), f'test[{tid}].{key}')
        rs = t.get('requirements')
        if not isinstance(rs, list) or not rs or any(v not in ('R1','R2','R3','R4','R5') for v in rs):
            raise ValueError(f'Invalid requirement links: {tid}.')
    if len(tests) != 80 or len(set(test_ids)) != 80 or set(test_ids) != req:
        raise ValueError('Exactly 80 unique family-specific requests are required.')
    observed = set()
    for r in audit:
        if not isinstance(r, dict):
            raise ValueError('Each audit record must be an object.')
        cid, tid = r.get('candidate_id'), r.get('test_id')
        key = (cid, tid)
        if key in observed or cid not in panel_by_id:
            raise ValueError(f'Duplicate or unknown candidate audit row: {key}.')
        observed.add(key)
        if tid not in req or r.get('family') != cid[:2] or not tid.startswith(cid[:2]+'-') or r.get('criterion') != tid[3:5]:
            raise ValueError(f'Audit family/request mismatch: {key}.')
        if 'result' not in r or (r['result'] is not None and
                (type(r['result']) is not int or r['result'] not in (0, 1))):
            raise ValueError(f'Result must be integer 0, integer 1, or null: {key}.')
        for field in ('observed', 'profile', 'reviewer', 'evidence_kind'):
            require_text(r.get(field), f'audit[{key}].{field}')
        if r['profile'] != panel_by_id[cid]['profile']:
            raise ValueError(f'Audit/panel source-profile mismatch: {key}.')
        check_source_ids(r.get('source_ids'), sources, f'audit[{key}]')
        if type(r.get('independent_review')) is not bool:
            raise ValueError(f'Independent-review flag must be Boolean: {key}.')
    exp_rows = {(cid, f'{cid[:2]}-C{i}{j}') for cid in ids
                for i in range(1,5) for j in 'abcd'}
    if len(audit) != 320 or observed != exp_rows:
        raise ValueError('Exactly 320 complete candidate-by-request rows are required.')
    if bundle['independent_review_completed'] and not all(r['independent_review'] for r in audit):
        raise ValueError('Completed independent review conflicts with unreviewed audit rows.')
    canonical(bundle)  # Reject nonfinite metadata rather than emitting invalid JSON.
    return expected


def family_bits(bundle, family):
    panel = [p for p in bundle['panel'] if p['family'] == family]
    rows = {(r['candidate_id'], r['test_id']): r for r in bundle['audit']}
    b = np.full((len(panel), 4, 4), np.nan)
    for a, p in enumerate(panel):
        for i in range(4):
            for j, letter in enumerate('abcd'):
                val = rows[(p['candidate_id'],f'{family}-C{i+1}{letter}')]['result']
                b[a,i,j] = np.nan if val is None else val
    return panel, b


def completions(bits):
    bits = checked_bits(bits, allow_unknown=True)
    loc = list(zip(*np.where(np.isnan(bits))))
    if len(loc) > 12:
        raise ValueError('More than 12 unresolved cells: use an explicit interval optimizer; do not impute.')
    result = []
    for values in itertools.product((0., 1.), repeat=len(loc)):
        out = bits.copy()
        for idx, value in zip(loc, values):
            out[idx] = value
        label = 'resolved' if not loc else ';'.join(
            f'{a}:{i+1}{chr(97+j)}={int(v)}' for (a,i,j),v in zip(loc, values))
        result.append((label, out))
    return result


def utility(bits, check_weights=None, curve='linear'):
    bits = checked_bits(bits, allow_unknown=False)
    q = np.ones((4,4)) if check_weights is None else np.asarray(check_weights, dtype=float)
    if q.shape != (4,4) or not np.all(np.isfinite(q)) or np.any(q < 0):
        raise ValueError('Each capability needs four finite nonnegative request weights.')
    # Scaling first avoids overflow for otherwise valid very large weights.
    scale = q.max(axis=1, keepdims=True)
    if np.any(scale <= 0):
        raise ValueError('No capability may have all four request weights zero.')
    if np.any(scale > 1e300): q = q / scale
    z = (bits * q[None,:,:]).sum(axis=2) / q.sum(axis=1)[None,:]
    if curve == 'linear': return z
    if curve == 'sqrt': return np.sqrt(z)
    if curve == 'square': return z*z
    raise ValueError('Unsupported value curve.')


def rank_credits(scores):
    """Fractional credits (draw, candidate, rank), including all tied positions."""
    s = checked_scores(scores)
    gt = (s[:,None,:] > s[:,:,None]).sum(axis=2)
    eq = (s[:,None,:] == s[:,:,None]).sum(axis=2)
    rank = np.arange(s.shape[1])[None,None,:]
    return ((rank >= gt[:,:,None]) & (rank < (gt+eq)[:,:,None])) / eq[:,:,None]


def first_credits(scores):
    s = checked_scores(scores)
    top = s == s.max(axis=1, keepdims=True)
    return top / top.sum(axis=1, keepdims=True)


def smaa_many(matrices, n, seed, alpha=1., fixed=None, multiplier=None, full=True):
    """Evaluate all evidence completions with the SAME weights. No probability over completions."""
    if not isinstance(matrices, (list, tuple)) or len(matrices) == 0:
        raise ValueError('Supply a nonempty list or tuple of complete utility tables.')
    if type(full) is not bool:
        raise ValueError('full must be Boolean.')
    x=np.stack(matrices).astype(float)   # completion, candidate, criterion
    if x.ndim!=3 or x.shape[0]<1 or x.shape[1]<1 or x.shape[2]!=4 or not np.all(np.isfinite(x)) or np.any(x<0) or np.any(x>1):
        raise ValueError('Complete finite utility tables in [0,1] are required.')
    c,a,_=x.shape
    seed = require_int(seed, 'seed', minimum=0)
    requested_n = require_int(n, 'n')
    require_int(BATCH_SIZE, 'BATCH_SIZE')
    if isinstance(alpha, (bool, np.bool_)) or not isinstance(alpha, (int, float, np.integer, np.floating)) or not np.isfinite(alpha) or alpha <= 0:
        raise ValueError('alpha must be finite and strictly positive.')
    if fixed is not None:
        fw = np.asarray(fixed, dtype=float)
        if fw.shape != (4,) or not np.all(np.isfinite(fw)) or np.any(fw < 0) or not np.isclose(fw.sum(), 1., rtol=0, atol=1e-12):
            raise ValueError('Fixed weights must be four finite nonnegative values summing to one.')
    if multiplier is not None:
        mult = np.asarray(multiplier, dtype=float)
        if mult.shape != (4,) or not np.all(np.isfinite(mult)) or np.any(mult < 0) or mult.max() <= 0:
            raise ValueError('Weight multipliers must be finite, nonnegative and not all zero.')
    rng=np.random.Generator(np.random.PCG64(seed))
    n=1 if fixed is not None else requested_n
    sums=np.zeros((c,a,a)); sumsq=np.zeros((c,a)); cw=np.zeros((c,a,4))
    for start in range(0,n,BATCH_SIZE):
        size=min(BATCH_SIZE,n-start)
        if fixed is None:w=rng.dirichlet(np.full(4,float(alpha)),size=size)
        else:
            w=fw[None,:]
        if multiplier is not None:
            w=w*(mult / mult.max() if mult.max() > 1e300 else mult)
            if np.any(w.sum(axis=1)<=0):raise ValueError('All weighted criteria were removed.')
            w=w/w.sum(axis=1,keepdims=True)
        for k in range(c):
            s=w@x[k].T
            cr=rank_credits(s) if full else None
            fc=cr[:,:,0] if full else first_credits(s)
            if full:sums[k]+=cr.sum(axis=0)
            else:sums[k,:,0]+=fc.sum(axis=0)
            sumsq[k]+=(fc*fc).sum(axis=0)
            cw[k]+=fc.T@w
    mean=sums/n
    variance=np.maximum(sumsq/n-mean[:,:,0]**2,0)
    se=np.sqrt(variance/(n-1)) if n>1 else np.zeros((c,a))
    center=np.full((c,a,4),np.nan)
    np.divide(cw,sums[:,:,0,None],out=center,where=sums[:,:,0,None]>0)
    return {'rank':mean,'first':mean[:,:,0],'se':se,'center':center,'draws':n,
            'expected_rank':(mean*np.arange(1,a+1)[None,None,:]).sum(axis=2) if full else None}


def allowance(n, deterministic=False, guard_means=None):
    if type(deterministic) is not bool: raise ValueError('deterministic must be Boolean.')
    require_int(n, 'n')
    count = MC_GUARD_MEANS if guard_means is None else guard_means
    require_int(count, 'guard_means')
    if not np.isfinite(MC_FAMILYWISE_ERROR) or not 0 < MC_FAMILYWISE_ERROR < 1:
        raise ValueError('MC_FAMILYWISE_ERROR must lie strictly between zero and one.')
    return 0. if deterministic else math.sqrt(math.log(2*count/MC_FAMILYWISE_ERROR)/(2*n))


def identify(first, n, deterministic=False, guard_means=None):
    first = np.asarray(first, dtype=float)
    if first.ndim != 2 or min(first.shape) < 1 or not np.all(np.isfinite(first)):
        raise ValueError('First-rank shares must be a nonempty finite completion-by-candidate matrix.')
    if np.any(first < -1e-12) or np.any(first > 1+1e-12) or not np.allclose(first.sum(axis=1), 1, rtol=0, atol=1e-9):
        raise ValueError('First-rank shares must be in [0,1] and sum to one for each completion.')
    lo=first.min(axis=0); hi=first.max(axis=0)
    eps=allowance(n,deterministic,guard_means)
    separated=[a for a in range(len(lo)) if len(lo)==1 or
               lo[a]-eps > max(np.delete(hi,a))+eps]
    tol=1e-11 if deterministic else 2*eps
    top_sets=[np.flatnonzero(row >= row.max()-tol).tolist() for row in first]
    return {'winner_index':int(separated[0]) if len(separated)==1 else None,
            'min_first':lo.tolist(),'max_first':hi.tolist(),'epsilon':eps,
            'completion_top_sets':top_sets}


def csv_out(path, rows, fields=None):
    if not rows:
        path.write_text('',encoding='utf-8');return
    fields=fields or list(rows[0])
    with path.open('w',newline='',encoding='utf-8-sig') as f:
        wr=csv.DictWriter(f,fieldnames=fields);wr.writeheader()
        for r in rows:
            wr.writerow({k:(json.dumps(r.get(k),ensure_ascii=False) if isinstance(r.get(k),(dict,list,tuple)) else r.get(k)) for k in fields})


def json_out(path,obj):
    def conv(o):
        if isinstance(o,np.ndarray):return o.tolist()
        if isinstance(o,np.generic):return o.item()
        raise TypeError(type(o).__name__)
    path.write_text(json.dumps(obj,ensure_ascii=False,indent=2,default=conv,allow_nan=False),encoding='utf-8')


def self_tests(bundle):
    results=[]
    def test(name,condition):
        if not bool(condition):raise AssertionError(name)
        results.append({'test':name,'passed':True})
    validate(bundle); test('confirmed panel, 80 demands and 320 evidence rows',True)
    cr=rank_credits([[3,2,1],[1,1,1],[3,2,2]])
    test('each candidate occupies one rank in each draw',np.allclose(cr.sum(axis=2),1))
    test('each rank has total credit one',np.allclose(cr.sum(axis=1),1))
    test('strict order',np.allclose(cr[0],np.eye(3)))
    test('three-way tie fractional all ranks',np.allclose(cr[1],1/3))
    test('lower-rank tie remains below sole winner',np.allclose(cr[2,1],[0,.5,.5]))
    test('first-only matches full-rank credit',np.allclose(first_credits([[3,2,1],[1,1,1],[3,2,2]]),cr[:,:,0]))
    rng=np.random.default_rng(2); ss=rng.normal(size=(30,4)); perm=[2,0,3,1]
    test('candidate permutation invariance',np.allclose(rank_credits(ss[:,perm]),rank_credits(ss)[:,perm,:]))
    test('rounding produces transitive tie groups',np.allclose(rank_credits([[1,1+1e-14]])[0,:,0],.5))
    b=np.zeros((2,4,4));b[0]=1;b[1,:,0]=1
    test('fixed denominator gives 1 and 1/4',np.allclose(utility(b),[[1]*4,[.25]*4]))
    q=np.ones((4,4));q[0,0]=2
    test('check reweighting renormalizes within capability',np.isclose(utility(b,q)[1,0],.4))
    test('square value curve',np.allclose(utility(b,curve='square')[1],.0625))
    test('sqrt value curve',np.allclose(utility(b,curve='sqrt')[1],.5))
    b[1,0,1]=np.nan
    co=completions(b)
    test('unknown is enumerated, never imputed',len(co)==2 and co[0][1][1,0,1]==0 and co[1][1][1,0,1]==1)
    test('enumeration leaves original audit unchanged',np.isnan(b[1,0,1]))
    z=np.array([[1.,1,1,1],[.5,.5,.5,.5],[0,0,0,0]])
    r=smaa_many([z],1000,99)
    test('strict dominance',np.allclose(r['first'][0],[1,0,0]))
    test('expected rank',np.allclose(r['expected_rank'][0],[1,2,3]))
    test('central weights sum to one',np.isclose(r['center'][0,0].sum(),1))
    test('undefined central weights stay missing',np.isnan(r['center'][0,1]).all())
    r2=smaa_many([z],1000,99)
    test('same seed is reproducible',np.array_equal(r['rank'],r2['rank']))
    ztie=np.ones((3,4));r=smaa_many([ztie],1000,99)
    test('identical profiles cannot be separated',identify(r['first'],1000)['winner_index'] is None)
    test('ties have zero empirical variation',np.max(r['se'])<1e-8)
    test('one million draws maximum SE is .05 pp',np.isclose(100/(2*np.sqrt(1_000_000)),.05))
    r=smaa_many([np.array([[1,0,0,0],[0,1,0,0]])],1,1,fixed=[.25]*4)
    test('fixed equal weights exact tie',np.allclose(r['first'],.5))
    test('fixed calculation has no Monte Carlo allowance',allowance(1,True)==0)
    test('changing completion labels adds no probability',np.allclose(np.min([[.2,.8],[.3,.7]],axis=0),[.2,.7]))
    # Mutation checks: no silent zero-filling or forged panel is accepted.
    import copy
    bad=copy.deepcopy(bundle);bad['audit'][0]['result']=.5
    try:validate(bad);ok=False
    except ValueError:ok=True
    test('fractional documentary observations rejected',ok)
    bad=copy.deepcopy(bundle);bad['audit'].pop()
    try:validate(bad);ok=False
    except ValueError:ok=True
    test('missing observation rejected',ok)
    bad=copy.deepcopy(bundle);bad['protocol']['allow_name_override']=True
    try:validate(bad);ok=False
    except ValueError:ok=True
    test('preferred-name override rejected',ok)
    bad=copy.deepcopy(bundle);bad['audit'][0]['source_ids']=['INVENTED']
    try:validate(bad);ok=False
    except ValueError:ok=True
    test('dangling evidence reference rejected',ok)
    # Analytically solvable profiles check the implementation without prescribing a resource name.
    sym=np.array([[.75,1,.75,1],[1,.75,.75,1],[.5,1,1,1]])
    rr=smaa_many([sym],100_000,2026)
    test('analytic three-alternative rank-share regions',np.max(np.abs(rr['first'][0]-[1/6,7/18,4/9]))<.01)
    rr=smaa_many([sym],1,2026,fixed=[.25]*4)
    test('same profiles tie at equal weights',np.allclose(rr['first'],1/3))
    low=np.array([[.5,.5,.5,.25],[.75,.75,.75,.75],[1,.75,.75,.75],[.5,1,.5,.75]])
    high=low.copy();high[2,2]=1
    rr=smaa_many([low,high],100_000,2027)
    test('analytic two-completion rank-share regions',np.max(np.abs(rr['first'][:,2]-[5/6,8/9]))<.01)
    test('guard does not break exact exchangeable ties',identify(np.array([[.5,.5]]),1_000_000)['winner_index'] is None)
    rr=smaa_many([np.array([[1,0,0,0],[0,1,0,0]])],1000,7,multiplier=[0,1,1,1])
    test('omitted criterion is genuinely zero-weighted',np.isclose(rr['first'][0,1],1))

    def rejects(name, action):
        try:
            action()
        except (ValueError, TypeError):
            test(name, True)
        else:
            raise AssertionError(name + ': invalid input was accepted')
    for key,value in [('denominator',5), ('allow_legacy_scores',1), ('status_values',[0,1])]:
        bad=copy.deepcopy(bundle);bad['protocol'][key]=value
        rejects('reject incompatible protocol '+key, lambda bad=bad: validate(bad))
    for key,value in [('family','F5'),('criterion','C4'),('obligation','')]:
        bad=copy.deepcopy(bundle);bad['protocol']['tests'][0][key]=value
        rejects('reject inconsistent request '+key, lambda bad=bad: validate(bad))
    for key,value in [('profile','unmatched release'),('source_ids','D01'),('independent_review','yes')]:
        bad=copy.deepcopy(bundle);bad['audit'][0][key]=value
        rejects('reject inconsistent observation '+key, lambda bad=bad: validate(bad))
    bad=copy.deepcopy(bundle);bad['sources']['R01']['url']=''
    rejects('reject missing source location',lambda:validate(bad))
    bad=copy.deepcopy(bundle);bad['independent_review_completed']=True
    rejects('reject false aggregate independent-review status',lambda:validate(bad))
    for v in (True, 10.7, 0, -1):
        rejects('reject invalid draw count '+str(v),lambda v=v:smaa_many([z],v,1))
    for v in (float('nan'),float('inf'),0.,-1.):
        rejects('reject invalid Dirichlet alpha '+str(v),lambda v=v:smaa_many([z],5,1,alpha=v))
    for v in ([np.nan,1,1,1],[np.inf,1,1,1],[0,0,0,0],[-1,1,1,1]):
        rejects('reject invalid multiplier '+str(v),lambda v=v:smaa_many([z],5,1,multiplier=v))
    for v in ([np.nan,0,0,1],[np.inf,0,0,0],[.25,.25,.25,.250001],[-1,1,1,0]):
        rejects('reject invalid fixed weights '+str(v),lambda v=v:smaa_many([z],1,1,fixed=v))
    for v in (np.nan,np.inf,-1.):
        rejects('reject invalid request weight '+str(v),lambda v=v:utility(np.ones((2,4,4)),np.full((4,4),v)))
    rejects('reject unresolved utility input',lambda:utility(np.full((1,4,4),np.nan)))
    rejects('reject nonbinary utility input',lambda:utility(np.full((1,4,4),.5)))
    rejects('reject infinite completion',lambda:completions(np.full((1,4,4),np.inf)))
    rejects('reject nonfinite score input',lambda:rank_credits([[1.,np.nan]]))
    rejects('reject empty score input',lambda:first_credits([]))
    rejects('reject malformed score shape',lambda:rank_credits(np.ones((2,2,2))))
    rejects('reject invalid first-rank totals',lambda:identify([[.8,.8]],100))
    rejects('reject missing first-rank shares',lambda:identify([[np.nan,1.]],100))
    test('single-candidate comparison is handled',identify([[1.]],1000)['winner_index']==0)
    test('all-rank credits permutation independent in tied input',
         np.allclose(rank_credits([[2,2,1]])[:,[1,0,2]],rank_credits([[2,2,1]])))
    test('large finite request weights normalize safely',np.allclose(
         utility(np.ones((2,4,4)),np.full((4,4),1e308)),1.))
    # Cross-check with independent sort-and-group logic, including negative scores.
    s=np.array([[3.,3.,1.,-2.],[0.,0.,0.,0.],[1.,2.,3.,4.]])
    ref=np.zeros((3,4,4))
    for k,row in enumerate(s):
        start=0
        for value in sorted(set(row),reverse=True):
            same=np.flatnonzero(row==value);stop=start+len(same)
            ref[k,same,start:stop]=1./len(same);start=stop
    test('independent sorting agrees with pairwise rank implementation',np.allclose(rank_credits(s),ref))
    permuted=copy.deepcopy(bundle);permuted['panel'].reverse();permuted['audit'].reverse()
    validate(permuted)
    test('audit row order does not change scored records',all(
        np.array_equal(family_bits(bundle,f)[1],family_bits(permuted,f)[1][::-1],equal_nan=True)
        for f in ('F1','F2','F3','F4','F5')))
    planned,used=guard_mean_count(bundle,[('base',{},10),('fixed',{'fixed':[.25]*4},1)])
    test('dynamic error guard covers all planned stochastic means',used>=planned and used>=MC_GUARD_MEANS)
    test('expanding the simultaneous family makes the allowance no smaller',
         allowance(1000,guard_means=20000)>=allowance(1000,guard_means=10000))
    # The revised UDC uncertainty case is an analytical software fixture, not a hard-coded winner.
    more=np.array([[.5,.5,.5,.25],[.75,.75,.75,.75],[1,.75,.75,.5],[.5,1,.5,.75]])
    rr=smaa_many([more],100_000,2028)
    test('additional uncertainty profile matches its simplex region',
         np.max(np.abs(rr['first'][0]-[0,1/3,4/9,2/9]))<.01)
    import tempfile
    with tempfile.TemporaryDirectory() as temp:
        path=Path(temp)/'audit.json'
        path.write_text('{"a":1,"a":2}',encoding='utf-8')
        rejects('duplicate JSON keys rejected',lambda:load_json_strict(path))
        path.write_text('{"a":NaN}',encoding='utf-8')
        rejects('nonfinite JSON constants rejected',lambda:load_json_strict(path))
        path.write_text('\ufeff{"a":1}',encoding='utf-8')
        test('UTF-8 BOM input accepted',load_json_strict(path)=={'a':1})
    bad=copy.deepcopy(bundle);bad['protocol']['status_values']=[False,True,None]
    rejects('Boolean protocol outcomes rejected',lambda:validate(bad))
    rejects('Boolean Dirichlet concentration rejected',lambda:smaa_many([np.ones((2,4))],10,2,alpha=True))
    rejects('non-Boolean full-rank switch rejected',lambda:smaa_many([np.ones((2,4))],10,2,full='no'))
    rejects('non-Boolean deterministic switch rejected',lambda:allowance(100,deterministic='no'))
    rejects('unsafe extreme score rounding rejected',lambda:rank_credits([[1e308,1.]]))
    rejects('ambiguous utility-array container rejected',lambda:smaa_many(np.ones((2,2,4)),10,2))
    return results


def main():
    start=time.time()
    validate_settings()
    bundle=BUNDLE if AUDIT_BUNDLE_PATH is None else load_json_strict(AUDIT_BUNDLE_PATH)
    validate(bundle)
    if os.getenv('FAMILY_SELECTION_OUTPUT'):
        out=Path(os.environ['FAMILY_SELECTION_OUTPUT'])
    elif Path('/kaggle/working').exists():out=Path('/kaggle/working/family_leader_selection')
    else:out=Path.cwd()/'family_leader_selection_output'
    if AUDIT_BUNDLE_PATH is not None and Path(AUDIT_BUNDLE_PATH).resolve().parent == out.resolve():
        raise ValueError('Keep the reviewed input bundle outside the output directory to avoid overwriting it.')
    out.mkdir(parents=True,exist_ok=True)
    tests=self_tests(bundle)
    json_out(out/'assessment_used.json',bundle)
    json_out(out/'protocol.json',bundle['protocol'])
    json_out(out/'sources.json',bundle['sources'])
    csv_out(out/'panel.csv',bundle['panel'])
    csv_out(out/'evidence_audit.csv',bundle['audit'])
    csv_out(out/'test_definitions.csv',bundle['protocol']['tests'])
    baseline={};leaders=[];rankrows=[];scorerows=[];sensrows=[];challengerows=[]
    scenarios=[('baseline',{},BASELINE_DRAWS),('weights_alpha_0.5',{'alpha':.5},SENSITIVITY_DRAWS),
               ('weights_alpha_2',{'alpha':2.},SENSITIVITY_DRAWS),('equal_weights',{'fixed':[.25]*4},1),
               ('sqrt_values',{'curve':'sqrt'},SENSITIVITY_DRAWS),('square_values',{'curve':'square'},SENSITIVITY_DRAWS)]
    for i in range(4):
        m=np.ones(4);m[i]=2
        scenarios.append((f'double_C{i+1}_weight',{'multiplier':m},CHECK_SENSITIVITY_DRAWS))
        m=np.ones(4);m[i]=0
        scenarios.append((f'omit_C{i+1}_weight',{'multiplier':m},CHECK_SENSITIVITY_DRAWS))
    if RUN_CHECK_SENSITIVITY:
        for i in range(4):
            for j in range(4):
                q=np.ones((4,4));q[i,j]=2
                scenarios.append((f'double_C{i+1}{chr(97+j)}_value',{'check_weights':q},CHECK_SENSITIVITY_DRAWS))
    planned_means, guard_means = guard_mean_count(bundle, scenarios)
    for fi,f in enumerate(('F1','F2','F3','F4','F5')):
        panel,bits=family_bits(bundle,f);comp=completions(bits)
        print(f'{f}: {len(panel)} candidates, {len(comp)} evidence completion(s)',flush=True)
        for ai,p in enumerate(panel):
            row={'family':f,'candidate_id':p['candidate_id'],'resource':p['resource']}
            for i in range(4):
                low=int(np.nansum(bits[ai,i]));unk=int(np.isnan(bits[ai,i]).sum())
                row[f'C{i+1}_min']=low;row[f'C{i+1}_max']=low+unk
                row[f'C{i+1}_bits']=''.join('?' if np.isnan(v) else str(int(v)) for v in bits[ai,i])
            scorerows.append(row)
        for si,(name,opt,n) in enumerate(scenarios):
            opt=dict(opt);q=opt.pop('check_weights',None);curve=opt.pop('curve','linear')
            matrices=[utility(b,q,curve) for _,b in comp]
            rr=smaa_many(matrices,n,SEED+fi*100_003+si*1009,full=(si==0),**opt)
            decision=identify(rr['first'],rr['draws'],deterministic='fixed' in opt,guard_means=guard_means)
            win=decision['winner_index'];wins='' if win is None else panel[win]['resource']
            sets=[' / '.join(panel[x]['resource'] for x in ss) for ss in decision['completion_top_sets']]
            sr={'family':f,'scenario':name,'draws':rr['draws'],'selected':wins,
                'top_sets':' | '.join(sets),'epsilon':decision['epsilon'],
                'min_first':decision['min_first'],'max_first':decision['max_first']}
            sensrows.append(sr)
            if si==0:
                base={'panel':panel,'counts_min':np.nansum(bits,axis=2).tolist(),
                    'counts_max':(np.nansum(bits,axis=2)+np.isnan(bits).sum(axis=2)).tolist(),
                    'completions':[x[0] for x in comp],
                    'first':rr['first'].tolist(),'rank':rr['rank'].tolist(),
                    'se':rr['se'].tolist(),'expected_rank':rr['expected_rank'].tolist(),
                    'decision':decision,'selected':wins}
                baseline[f]=base
                if win is not None:
                    gap=decision['min_first'][win]-max(np.delete(decision['max_first'],win))
                    guarded=gap-2*decision['epsilon']
                else:gap=None;guarded=None
                leaders.append({'family':f,'family_name':bundle['protocol']['family_names'][f],
                    'selected_candidate':wins,'candidate_id':'' if win is None else panel[win]['candidate_id'],
                    'min_first':None if win is None else decision['min_first'][win],
                    'max_first':None if win is None else decision['max_first'][win],
                    'min_lead':gap,'guarded_min_lead':guarded,
                    'status':'CONDITIONAL_DOCUMENTARY_SELECTION' if win is not None else 'NO_SEPARATED_BASELINE_LEADER',
                    'basis':'documentary native-service evidence; fixed study requests and symmetric weight model',
                    'implementation_eligibility':'NOT_REASSESSED_BY_THIS_NUMERICAL_RUN'})
                for k,(lab,b) in enumerate(comp):
                    for ai,p in enumerate(panel):
                        rw={'family':f,'completion':lab,'candidate_id':p['candidate_id'],'resource':p['resource'],
                            'first_se':float(rr['se'][k,ai]),'expected_rank':float(rr['expected_rank'][k,ai])}
                        for rank in range(len(panel)):rw[f'rank_{rank+1}']=float(rr['rank'][k,ai,rank])
                        for i in range(4):
                            val=rr['center'][k,ai,i];rw[f'central_w{i+1}']=None if np.isnan(val) else float(val)
                        rankrows.append(rw)
        if RUN_EVIDENCE_CHALLENGES:
            # This is a fragility diagnostic, NOT permission to replace evidence after seeing results.
            # Flip each resolved 0/1 individually; keep all pre-existing Unknown completions.
            for ai,p in enumerate(panel):
                for i in range(4):
                    for j in range(4):
                        if np.isnan(bits[ai,i,j]):continue
                        altered=bits.copy();altered[ai,i,j]=1-altered[ai,i,j]
                        altcomp=completions(altered)
                        rr=smaa_many([utility(b) for _,b in altcomp],CHALLENGE_DRAWS,SEED+fi*100_003+70_001,full=False)
                        dc=identify(rr['first'],rr['draws'],guard_means=guard_means)
                        wi=dc['winner_index']; sel='' if wi is None else panel[wi]['resource']
                        challengerows.append({'family':f,'candidate_id':p['candidate_id'],'test_id':f'{f}-C{i+1}{chr(97+j)}',
                            'original':int(bits[ai,i,j]),'hypothetical':int(altered[ai,i,j]),'selected':sel,
                            'changed_or_unresolved':sel!=baseline[f]['selected'],
                            'top_sets':' | '.join(' / '.join(panel[x]['resource'] for x in ss) for ss in dc['completion_top_sets']),
                            'draws':rr['draws']})
    for lr in leaders:
        f=lr['family']; rows=[r for r in sensrows if r['family']==f and r['scenario']!='baseline']
        lr['sensitivity_changes_or_ties']=[r['scenario'] for r in rows if r['selected']!=lr['selected_candidate']]
        ch=[r for r in challengerows if r['family']==f]
        lr['one_cell_challenges']=len(ch)
        lr['one_cell_changes_or_unresolved']=sum(r['changed_or_unresolved'] for r in ch)
    # Merge all rank columns because families contain different candidate counts.
    rf=['family','completion','candidate_id','resource','first_se','expected_rank']+[f'rank_{i}' for i in range(1,7)]+[f'central_w{i}' for i in range(1,5)]
    csv_out(out/'rank_acceptability.csv',rankrows,rf)
    csv_out(out/'capability_scores.csv',scorerows)
    csv_out(out/'family_leaders.csv',leaders)
    csv_out(out/'sensitivity.csv',sensrows)
    csv_out(out/'evidence_challenges.csv',challengerows)
    json_out(out/'baseline_results.json',baseline)
    json_out(out/'family_leaders.json',leaders)
    json_out(out/'sensitivity.json',sensrows)
    json_out(out/'self_tests.json',tests)
    json_out(out/'quality_review_amendments.json',bundle.get('quality_review_amendments',[]))
    script_hash=None
    if '__file__' in globals() and Path(__file__).is_file():script_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    manifest={'assessment_sha256':digest(bundle),'protocol_sha256':digest(bundle['protocol']),
        'script_sha256':script_hash,'python':platform.python_version(),'numpy':np.__version__,
        'generator':'PCG64','seed':SEED,'batch_size':BATCH_SIZE,'baseline_draws':BASELINE_DRAWS,
        'sensitivity_draws':SENSITIVITY_DRAWS,'check_sensitivity_draws':CHECK_SENSITIVITY_DRAWS,
        'challenge_draws':CHALLENGE_DRAWS,'tie_decimals':TIE_DECIMALS,'mc_error_budget':MC_FAMILYWISE_ERROR,
        'mc_guard_means':guard_means,'mc_guard_floor':MC_GUARD_MEANS,
        'planned_stochastic_first_rank_means':planned_means,
        'run_check_sensitivity':RUN_CHECK_SENSITIVITY,'run_evidence_challenges':RUN_EVIDENCE_CHALLENGES,
        'scenario_names':[name for name,_,_ in scenarios],
        'implementation_sha256':implementation_digest(),
        'source_review_mode':bundle.get('review_mode'),
        'input_mode':'embedded' if AUDIT_BUNDLE_PATH is None else 'external','raw_source_snapshot_hashes':None,
        'raw_source_snapshots_declared':bundle['raw_source_snapshots_captured'],
        'source_snapshot_warning':('This run does not capture or validate raw source bytes. Assessment/protocol hashes secure judgments, not cited website content.'),
        'source_adapters_executed':bundle['source_adapters_executed'],
        'independent_review_completed':bundle['independent_review_completed'],
        'implementation_eligibility_reassessed':False,
        'kaggle_service_execution_claimed':False,'run_seconds':round(time.time()-start,3),
        'self_tests_passed':len(tests),'assessment_nature':bundle['basis']}
    json_out(out/'manifest.json',manifest)
    lines=['# Family selection results','',
        'Documentary conformance analysis, not a population benchmark, observed operational pass rate, or implementation-eligibility certification.',
        'Scores and leaders are regenerated from the supplied assessment. Unknowns are enumerated, not assigned probabilities.','',
        '|Family|Selected under baseline|First-rank share range|Guarded minimum lead|',
        '|---|---|---:|---:|']
    for r in leaders:
        pct='not separated' if r['min_first'] is None else f"{r['min_first']*100:.4f}–{r['max_first']*100:.4f}%"
        gap='' if r['guarded_min_lead'] is None else f"{100*r['guarded_min_lead']:.4f} pp"
        lines.append(f"|{r['family']}|{r['selected_candidate'] or 'Unresolved'}|{pct}|{gap}|")
    lines+=['','## Sensitivities']
    for r in leaders:
        changes=', '.join(r['sensitivity_changes_or_ties']) or 'none in the declared scenarios'
        lines.append(f"{r['family']}: reversals/ties: {changes}. One-cell challenges changing or removing the separated choice: {r['one_cell_changes_or_unresolved']}/{r['one_cell_challenges']}.")
    lines+=['','The first-rank percentages describe the stated source assessments, demands and preference model; they are not probabilities of universal superiority.',
        'DDC has no preferred-name override. Changing a source profile requires recoding the corresponding evidence and rerunning all affected comparisons.']
    (out/'results.md').write_text('\n'.join(lines),encoding='utf-8')
    print('\n'.join(lines));print(f'\nOutputs: {out}\nTests passed: {len(tests)}; elapsed {time.time()-start:.1f}s',flush=True)
    return out


if __name__ == '__main__':
    RESULT_DIRECTORY = main()
