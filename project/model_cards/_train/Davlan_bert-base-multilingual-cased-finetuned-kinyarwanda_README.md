Hugging Face's logo
---
language: rw
datasets:

---
# bert-base-multilingual-cased-finetuned-kinyarwanda
## Model description
**bert-base-multilingual-cased-finetuned-kinyarwanda** is a **Kinyarwanda BERT** model obtained by fine-tuning **bert-base-multilingual-cased** model on Kinyarwanda language texts.  It provides **better performance** than the multilingual BERT on named entity recognition datasets.  

Specifically, this model is a *bert-base-multilingual-cased* model that was fine-tuned on Kinyarwanda corpus. 
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for masked token prediction.
```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='Davlan/bert-base-multilingual-cased-finetuned-kinyarwanda')
>>> unmasker("Twabonye ko igihe mu [MASK] hazaba hari ikirango abantu bakunze")

```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains. 
## Training data
This model was fine-tuned on JW300 + [KIRNEWS](https://github.com/Andrews2017/KINNEWS-and-KIRNEWS-Corpus) + [BBC Gahuza](https://www.bbc.com/gahuza)

## Training procedure
This model was trained on a single NVIDIA V100 GPU

## Eval results on Test set (F-score, average over 5 runs)
Dataset| mBERT F1 | rw_bert F1
-|-|-
[MasakhaNER](https://github.com/masakhane-io/masakhane-ner) | 72.20 | 77.57

### BibTeX entry and citation info
By David Adelani
```

```


