Hugging Face's logo
---
language: wo
datasets:

---
# xlm-roberta-base-finetuned-wolof
## Model description
**xlm-roberta-base-finetuned-luganda** is a **Wolof RoBERTa** model obtained by fine-tuning **xlm-roberta-base** model on Wolof language texts.  It provides **better performance** than the XLM-RoBERTa on named entity recognition datasets.  

Specifically, this model is a *xlm-roberta-base* model that was fine-tuned on Wolof corpus. 
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for masked token prediction.
```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='Davlan/xlm-roberta-base-finetuned-wolof')
>>> unmasker("Màkki Sàll feeñal na ay xalaatam ci mbir yu am solo yu soxal <mask> ak Afrik.")



```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains. 
## Training data
This model was fine-tuned on [Bible OT](http://biblewolof.com/) + [OPUS](https://opus.nlpl.eu/) + News Corpora (Lu Defu Waxu, Saabal, and Wolof Online)

## Training procedure
This model was trained on a single NVIDIA V100 GPU

## Eval results on Test set (F-score, average over 5 runs)
Dataset| XLM-R F1 | wo_roberta F1
-|-|-
[MasakhaNER](https://github.com/masakhane-io/masakhane-ner) | 63.86 | 68.31

### BibTeX entry and citation info
By David Adelani
```

```


