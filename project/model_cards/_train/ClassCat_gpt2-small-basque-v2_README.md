---
language: eu
license: cc-by-sa-4.0
datasets:
- cc100
- oscar
widget:
- text: "Zein da zure"
- text: "Euria egingo"
- text: "Nola dakizu ?"
---

## GPT2 Basque small model Version 2 (Uncased)

### Prerequisites

transformers==4.19.2

### Model architecture

This model uses approximately half the size of GPT2 base model parameters.


### Tokenizer

Using BPE tokenizer with vocabulary size 50,000.

### Training Data 

* Subset of [CC-100/eu](https://data.statmt.org/cc-100/) : Monolingual Datasets from Web Crawl Data
* Subset of [oscar](https://huggingface.co/datasets/oscar)

### Usage

```python
from transformers import pipeline

generator = pipeline('text-generation', model='ClassCat/gpt2-small-basque-v2')
generator("Zein da zure ", max_length=50, num_return_sequences=5)
```