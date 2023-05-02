---
language: es
license: cc-by-sa-4.0
datasets:
- wikipedia
- cc100
widget:
- text: "Yo vivo en <mask>."
- text: "Quiero <mask> contigo ?"
- text: "Es clima es <mask>."
- text: "Me llamo <mask>."
- text: "Las negociaciones están <mask>."
---

## RoBERTa Spanish base model (Uncased)

### Prerequisites

transformers==4.19.2

### Model architecture

This model uses RoBERTa base setttings except vocabulary size.

### Tokenizer

Using BPE tokenizer with vocabulary size 50,000.

### Training Data 

* [wiki40b/es](https://www.tensorflow.org/datasets/catalog/wiki40b#wiki40bes) (Spanish Wikipedia)
* Subset of [CC-100/es](https://data.statmt.org/cc-100/) : Monolingual Datasets from Web Crawl Data

### Usage

```python
from transformers import pipeline

unmasker = pipeline('fill-mask', model='ClassCat/roberta-base-spanish')
unmasker("Yo soy <mask>.")
```