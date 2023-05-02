---
language: ca
license: cc-by-sa-4.0
datasets:
- cc100
- oscar
- wikipedia
widget:
- text: "Vas jugar a"
- text: "M'agrada el clima i el menjar"
- text: "Ell està una mica"
---

## GPT2 Catalan small model Version 2 (Uncased)

### Prerequisites

transformers==4.19.2

### Model architecture

This model uses GPT2 base model settings, but the size of embedding dimensions are half the size of them.

### Tokenizer

Using BPE tokenizer with vocabulary size 50,000.

### Training Data 

* [wiki40b/ca](https://www.tensorflow.org/datasets/catalog/wiki40b#wiki40bca) (Catalan Wikipedia)
* Subset of [oscar](https://huggingface.co/datasets/oscar)
* Subset of [CC-100/ca](https://data.statmt.org/cc-100/) : Monolingual Datasets from Web Crawl Data

### Usage

```python
from transformers import pipeline

unmasker = pipeline('fill-mask', model='ClassCat/gpt2-small-catalan-v2')
unmasker("Ell està una mica")
```