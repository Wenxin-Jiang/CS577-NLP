Hugging Face's logo
---
language: wo
datasets:

---
# bert-base-multilingual-cased-finetuned-wolof
## Model description
**bert-base-multilingual-cased-finetuned-wolof** is a **Wolof BERT** model obtained by fine-tuning **bert-base-multilingual-cased** model on Wolof language texts.  It provides **better performance** than the multilingual BERT on named entity recognition datasets.  

Specifically, this model is a *bert-base-multilingual-cased* model that was fine-tuned on Wolof corpus. 
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for masked token prediction.
```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='Davlan/bert-base-multilingual-cased-finetuned-wolof')
>>> unmasker("Màkki Sàll feeñal na ay xalaatam ci mbir yu am solo yu soxal [MASK] ak Afrik.")

```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains. 
## Training data
This model was fine-tuned on [Bible OT](http://biblewolof.com/) + [OPUS](https://opus.nlpl.eu/) + News Corpora (Lu Defu Waxu, Saabal, and Wolof Online)

## Training procedure
This model was trained on a single NVIDIA V100 GPU

## Eval results on Test set (F-score, average over 5 runs)
Dataset| mBERT F1 | wo_bert F1
-|-|-
[MasakhaNER](https://github.com/masakhane-io/masakhane-ner) | 64.52 | 69.43

### BibTeX entry and citation info
By David Adelani
```

```


