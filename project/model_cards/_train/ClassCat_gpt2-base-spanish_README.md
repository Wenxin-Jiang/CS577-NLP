---
language: es
license: cc-by-sa-4.0
datasets:
- wikipedia
- cc100
widget:
- text: "¿Hablas español?"
- text: "Es clima es"
- text: "Las negociaciones están paradas, pero"
---

## GPT2 Spanish base model (Uncased)

### Prerequisites

transformers==4.19.2

### Model architecture

This model uses GPT2 base setttings except vocabulary size.

### Tokenizer

Using BPE tokenizer with vocabulary size 50,000.

### Training Data 

* [wiki40b/es](https://www.tensorflow.org/datasets/catalog/wiki40b#wiki40bes) (Spanish Wikipedia)
* Subset of [CC-100/es](https://data.statmt.org/cc-100/) : Monolingual Datasets from Web Crawl Data

### Usage

```python
from transformers import pipeline

generator = pipeline('text-generation', model='ClassCat/gpt2-base-spanish')
generator("Yo soy ", max_length=50, num_return_sequences=5)
```