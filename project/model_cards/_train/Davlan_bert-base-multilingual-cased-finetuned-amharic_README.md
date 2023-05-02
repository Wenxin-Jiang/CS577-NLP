Hugging Face's logo
---
language: am
datasets:

---
# bert-base-multilingual-cased-finetuned-amharic
## Model description
**bert-base-multilingual-cased-finetuned-amharic** is a **Amharic BERT** model obtained by replacing mBERT vocabulary by amharic vocabulary because the language was not supported, and fine-tuning **bert-base-multilingual-cased** model on Amharic language texts.  It provides **better performance** than the multilingual Amharic on named entity recognition datasets.  

Specifically, this model is a *bert-base-multilingual-cased* model that was fine-tuned on Amharic corpus using Amharic vocabulary. 
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for masked token prediction.
```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='Davlan/bert-base-multilingual-cased-finetuned-amharic')
>>> unmasker("የአሜሪካ የአፍሪካ ቀንድ ልዩ መልዕክተኛ ጄፈሪ ፌልትማን በአራት አገራት የሚያደጉትን [MASK] መጀመራቸውን የአሜሪካ የውጪ ጉዳይ ሚንስቴር አስታወቀ።")
                    

```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains. 
## Training data
This model was fine-tuned on [Amharic CC-100](http://data.statmt.org/cc-100/)

## Training procedure
This model was trained on a single NVIDIA V100 GPU

## Eval results on Test set (F-score, average over 5 runs)
Dataset| mBERT F1 | am_bert F1
-|-|-
[MasakhaNER](https://github.com/masakhane-io/masakhane-ner) | 0.0 | 60.89

### BibTeX entry and citation info
By David Adelani
```

```


