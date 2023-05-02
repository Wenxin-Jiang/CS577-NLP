---
language: fr
license: cc-by-sa-4.0
datasets:
- wikipedia
- cc100
widget:
- text: "Je vais à la <mask>."
- text: "J'aime le <mask>."
- text: "J'ai ouvert la <mask>."
- text: "Je m'appelle <mask>."
- text: "J'ai beaucoup d'<mask>."

---

## RoBERTa French base model (Uncased)

### Prerequisites

transformers==4.19.2

### Model architecture

This model uses RoBERTa base setttings except vocabulary size.

### Tokenizer

Using BPE tokenizer with vocabulary size 50,000.

### Training Data 

* [wiki40b/fr](https://www.tensorflow.org/datasets/catalog/wiki40b#wiki40bfr) (French Wikipedia)
* Subset of [CC-100/fr](https://data.statmt.org/cc-100/) : Monolingual Datasets from Web Crawl Data

### Usage

```python
from transformers import pipeline

unmasker = pipeline('fill-mask', model='ClassCat/roberta-base-french')
unmasker("Je vais à la <mask>.")
```