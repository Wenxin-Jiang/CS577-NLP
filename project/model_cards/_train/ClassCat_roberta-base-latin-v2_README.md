---
language: la
license: cc-by-sa-4.0
datasets:
- cc100
widget:
- text: quod est tibi <mask> ?"
- text: vita brevis, ars <mask>.
- text: errare <mask> est.
- text: usus est magister <mask>.
---

## RoBERTa Latin base model Version 2 (Uncased)

### Prerequisites

transformers==4.19.2

### Model architecture

This model uses RoBERTa base setttings except vocabulary size.

### Tokenizer

Using BPE tokenizer with a vocabulary size 50,000.

### Training Data 

* Subset of [CC-100/la](https://data.statmt.org/cc-100/) : Monolingual Datasets from Web Crawl Data

### Usage

```python
from transformers import pipeline

unmasker = pipeline('fill-mask', model='ClassCat/roberta-base-latin-v2')
unmasker("vita brevis, ars <mask>")
```