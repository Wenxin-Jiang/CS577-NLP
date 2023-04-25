---
language: es
datasets:
- large_spanish_corpus
license: mit
---

# ConvBERT base pre-trained on large_spanish_corpus

The ConvBERT architecture is presented in the ["ConvBERT: Improving BERT with Span-based Dynamic Convolution"](https://arxiv.org/abs/2008.02496) paper.

## Metrics on evaluation set

```
disc_accuracy = 0.9488542
disc_auc = 0.8833056
disc_loss = 0.15933733
disc_precision = 0.79224133
disc_recall = 0.27443287
global_step = 1000000
loss = 9.658503
masked_lm_accuracy = 0.6177698
masked_lm_loss = 1.7050561
sampled_masked_lm_accuracy = 0.5379228
```

## Usage

```python
from transformers import AutoModel, AutoTokenizer
model_name = "mrm8488/convbert-base-spanish"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)
```

> Created by [Manuel Romero/@mrm8488](https://twitter.com/mrm8488) with the support of [Narrativa](https://www.narrativa.com/)

> Made with <span style="color: #e25555;">&hearts;</span> in Spain