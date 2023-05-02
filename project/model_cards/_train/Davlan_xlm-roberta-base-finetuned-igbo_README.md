Hugging Face's logo
---
language: ig
datasets:

---
# xlm-roberta-base-finetuned-igbo
## Model description
**xlm-roberta-base-finetuned-igbo** is a **Igbo RoBERTa** model obtained by fine-tuning **xlm-roberta-base** model on Hausa language texts.  It provides **better performance** than the XLM-RoBERTa on named entity recognition datasets.  

Specifically, this model is a *xlm-roberta-base* model that was fine-tuned on Igbo corpus. 
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for masked token prediction.
```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='Davlan/xlm-roberta-base-finetuned-igbo')
>>> unmasker("Reno Omokri na Gọọmentị <mask> enweghị ihe ha ga-eji hiwe ya bụ mmachi.")



```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains. 
## Training data
This model was fine-tuned on JW300 + OPUS CC-Align + [IGBO NLP Corpus](https://github.com/IgnatiusEzeani/IGBONLP) +[Igbo CC-100](http://data.statmt.org/cc-100/)

## Training procedure
This model was trained on a single NVIDIA V100 GPU

## Eval results on Test set (F-score, average over 5 runs)
Dataset| XLM-R F1 | ig_roberta F1
-|-|-
[MasakhaNER](https://github.com/masakhane-io/masakhane-ner) | 84.51 | 87.74

### BibTeX entry and citation info
By David Adelani
```

```


