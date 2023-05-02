Hugging Face's logo
---
language: am
datasets:

---
# xlm-roberta-base-finetuned-amharic
## Model description
**xlm-roberta-base-finetuned-amharic** is a **Amharic RoBERTa** model obtained by fine-tuning **xlm-roberta-base** model on Amharic language texts.  It provides **better performance** than the XLM-RoBERTa on named entity recognition datasets.  

Specifically, this model is a *xlm-roberta-base* model that was fine-tuned on Amharic corpus. 
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for masked token prediction.
```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='Davlan/xlm-roberta-base-finetuned-hausa')
>>> unmasker("የአሜሪካ የአፍሪካ ቀንድ ልዩ መልዕክተኛ ጄፈሪ ፌልትማን በአራት አገራት የሚያደጉትን <mask> መጀመራቸውን የአሜሪካ የውጪ ጉዳይ ሚንስቴር አስታወቀ።")


```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains. 
## Training data
This model was fine-tuned on [Amharic CC-100](http://data.statmt.org/cc-100/)

## Training procedure
This model was trained on a single NVIDIA V100 GPU

## Eval results on Test set (F-score, average over 5 runs)
Dataset| XLM-R F1 | am_roberta F1
-|-|-
[MasakhaNER](https://github.com/masakhane-io/masakhane-ner) | 70.96 | 77.97

### BibTeX entry and citation info
By David Adelani
```

```


