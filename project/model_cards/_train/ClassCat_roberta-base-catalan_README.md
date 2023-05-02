---
language: ca
license: cc-by-sa-4.0
datasets:
- wikipedia
- cc100
widget:
- text: "És molt <mask> per a mi."
- text: "Vas jugar a <mask>."
- text: "Ell està una mica <mask>."
- text: "És un bon <mask>."
- text: "M'agradaria menjar una <mask>."
---

## RoBERTa Catalan base model (Uncased)

### Prerequisites

transformers==4.19.2

### Model architecture

This model uses RoBERTa base setttings except vocabulary size.

### Tokenizer

Using BPE tokenizer with vocabulary size 50,000.

### Training Data 

* [wiki40b/ca](https://www.tensorflow.org/datasets/catalog/wiki40b#wiki40bca) (Catalan Wikipedia)
* Subset of [CC-100/ca](https://data.statmt.org/cc-100/) : Monolingual Datasets from Web Crawl Data

### Usage

```python
from transformers import pipeline

unmasker = pipeline('fill-mask', model='ClassCat/roberta-base-catalan')
unmasker("Jo <mask> japonès.")
```