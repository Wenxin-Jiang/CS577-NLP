---
language: el
license: cc-by-sa-4.0
datasets:
- cc100
- oscar
- wikipedia
widget:
- text: "Δεν την έχω <mask> ποτέ."
- text: "Έχει πολύ καιρό που δεν έχουμε <mask>."
- text: "Ευχαριστώ για το <mask> σου."
- text: "Αυτό είναι <mask>."
- text: "Ανοιξα <mask>."
- text: "Ευχαριστώ για <mask>."
- text: "Έχει πολύ καιρό που δεν <mask>."
---

## RoBERTa Greek small model (Uncased)

### Prerequisites

transformers==4.19.2

### Model architecture

This model uses approximately half the size of RoBERTa base model parameters.

### Tokenizer

Using BPE tokenizer with vocabulary size 50,000.

### Training Data

* Subset of [CC-100/el](https://data.statmt.org/cc-100/) : Monolingual Datasets from Web Crawl Data
* Subset of [oscar](https://huggingface.co/datasets/oscar)
* [wiki40b/el](https://www.tensorflow.org/datasets/catalog/wiki40b#wiki40bel) (Greek Wikipedia)

### Usage

```python
from transformers import pipeline

unmasker = pipeline('fill-mask', model='ClassCat/roberta-small-greek')
unmasker("Έχει πολύ καιρό που δεν <mask>.")
```