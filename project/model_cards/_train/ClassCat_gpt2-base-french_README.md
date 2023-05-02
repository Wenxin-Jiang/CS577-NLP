---
language: fr
license: cc-by-sa-4.0
datasets:
- wikipedia
- cc100
widget:
- text: "Je vais à la gare, et"
- text: "J'aime le café, donc"
- text: "Nous avons parlé"
- text: "Je m'appelle"
---

## GPT2 French base model (Uncased)

### Prerequisites

transformers==4.19.2

### Model architecture

This model uses GPT2 base setttings except vocabulary size.

### Tokenizer

Using BPE tokenizer with vocabulary size 50,000.

### Training Data 

* [wiki40b/fr](https://www.tensorflow.org/datasets/catalog/wiki40b#wiki40bfr) (French Wikipedia)
* Subset of [CC-100/fr](https://data.statmt.org/cc-100/) : Monolingual Datasets from Web Crawl Data

### Usage

```python
from transformers import pipeline

generator = pipeline('text-generation', model='ClassCat/gpt2-base-french')
generator("Je vais à la", max_length=50, num_return_sequences=5)
```