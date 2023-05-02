---
language: en
tags:
- spanbert
datasets:
- ade_corpus_v2
widget:
- text: "Having fever after taking paracetamol."
  example_title: "NER"
- text: "Birth defects associated with thalidomide."
  example_title: "NER"
- text: "Deafness and kidney failure associated with gentamicin (an antibiotic)."
  example_title: "NER"
- text: "Bleeding of the intestine associated with aspirin therapy."
  example_title: "NER"
---

spanbert-large-cased fine-tuned for <b>"Adverse drug reaction"</b> and <b>"Drug"</b> span Extraction.

<b>Details of spanbert-large-cased:</b>
https://huggingface.co/SpanBERT/spanbert-large-cased

<b>Details of the downstream task (Adverse drug reaction and Drug Extraction) - Dataset</b>
https://huggingface.co/datasets/ade_corpus_v2