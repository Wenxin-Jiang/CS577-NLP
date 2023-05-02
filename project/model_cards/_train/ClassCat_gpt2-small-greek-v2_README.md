---
language: el
license: cc-by-sa-4.0
datasets:
- cc100
- oscar
- wikipedia
widget:
- text: "Αυτό είναι ένα"
- text: "Ανοιξα την"
- text: "Ευχαριστώ για το"
- text: "Έχει πολύ καιρό που δεν έχουμε"
---

## Greek GPT2 small model Version 2 (Uncased)

### Prerequisites

transformers==4.19.2

### Model architecture

This model uses approximately half the size of GPT2 base model parameters.

### Tokenizer

Using BPE tokenizer with vocabulary size 50,000.

### Training Data 

* Subset of [CC-100/el](https://data.statmt.org/cc-100/) : Monolingual Datasets from Web Crawl Data
* Subset of [oscar](https://huggingface.co/datasets/oscar)
* [wiki40b/el](https://www.tensorflow.org/datasets/catalog/wiki40b#wiki40bel) (Greek Wikipedia)

### Usage

```python
from transformers import pipeline
generator = pipeline('text-generation', model='ClassCat/gpt2-small-greek-v2')
generator("Αυτό είναι ένα", max_length=50, num_return_sequences=5)
```
