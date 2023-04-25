Hugging Face's logo
---
language: ig
datasets:

---
# bert-base-multilingual-cased-finetuned-igbo
## Model description
**bert-base-multilingual-cased-finetuned-igbo** is a **Igbo BERT** model obtained by fine-tuning **bert-base-multilingual-cased** model on Igbo language texts.  It provides **better performance** than the multilingual BERT on text classification and named entity recognition datasets.  

Specifically, this model is a *bert-base-multilingual-cased* model that was fine-tuned on Igbo corpus. 
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for masked token prediction.
```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='Davlan/bert-base-multilingual-cased-finetuned-igbo')
>>> unmasker("Reno Omokri na Gọọmentị [MASK] enweghị ihe ha ga-eji hiwe ya bụ mmachi.")

```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains. 
## Training data
This model was fine-tuned on JW300 + OPUS CC-Align + [IGBO NLP Corpus](https://github.com/IgnatiusEzeani/IGBONLP) +[Igbo CC-100](http://data.statmt.org/cc-100/)

## Training procedure
This model was trained on a single NVIDIA V100 GPU

## Eval results on Test set (F-score, average over 5 runs)
Dataset| mBERT F1 | ig_bert F1
-|-|-
[MasakhaNER](https://github.com/masakhane-io/masakhane-ner) | 85.11 | 86.75

### BibTeX entry and citation info
By David Adelani
```

```


