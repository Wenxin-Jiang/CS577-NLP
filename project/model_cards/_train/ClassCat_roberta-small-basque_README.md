---
language: eu
license: cc-by-sa-4.0
datasets:
- cc100
- oscar
widget:
- text: "Euria egingo <mask> gaur ?"
- text: "<mask> umeari liburua eman dio."
- text: "Zein da zure <mask> ?"
---

## RoBERTa Basque small model (Uncased)

### Prerequisites

transformers==4.19.2

### Model architecture

This model uses approximately half the size of RoBERTa base model parameters.

### Tokenizer

Using BPE tokenizer with vocabulary size 50,000.

### Training Data 

* Subset of [CC-100/eu](https://data.statmt.org/cc-100/) : Monolingual Datasets from Web Crawl Data
* Subset of [oscar](https://huggingface.co/datasets/oscar)

### Usage

```python
from transformers import pipeline

unmasker = pipeline('fill-mask', model='ClassCat/roberta-small-basque')
unmasker("Zein da zure <mask> ?")
```