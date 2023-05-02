Hugging Face's logo
---
language: pcm
datasets:

---
# xlm-roberta-base-finetuned-naija
## Model description
**xlm-roberta-base-finetuned-naija** is a **Nigerian Pidgin RoBERTa** model obtained by fine-tuning **xlm-roberta-base** model on Nigerian Pidgin language texts.  It provides **better performance** than the XLM-RoBERTa on named entity recognition datasets.  

Specifically, this model is a *xlm-roberta-base* model that was fine-tuned on Nigerian Pidgin  corpus. 
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for masked token prediction.
```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='Davlan/xlm-roberta-base-finetuned-naija')
>>> unmasker("Another attack on ambulance happen for Koforidua in March <mask> year where robbers kill Ambulance driver")



```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains. 
## Training data
This model was fine-tuned on JW300 + [BBC Pidgin](https://www.bbc.com/pidgin)

## Training procedure
This model was trained on a single NVIDIA V100 GPU

## Eval results on Test set (F-score, average over 5 runs)
Dataset| XLM-R F1 | pcm_roberta F1
-|-|-
[MasakhaNER](https://github.com/masakhane-io/masakhane-ner) | 87.26 | 90.00

### BibTeX entry and citation info
By David Adelani
```

```


