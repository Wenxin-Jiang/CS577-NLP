Hugging Face's logo
---
language: lg
datasets:

---
# bert-base-multilingual-cased-finetuned-luganda
## Model description
**bert-base-multilingual-cased-finetuned-luganda** is a **Luganda BERT** model obtained by fine-tuning **bert-base-multilingual-cased** model on Luganda language texts.  It provides **better performance** than the multilingual BERT on text classification and named entity recognition datasets.  

Specifically, this model is a *bert-base-multilingual-cased* model that was fine-tuned on Luganda corpus. 
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for masked token prediction.
```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='Davlan/bert-base-multilingual-cased-finetuned-luganda')
>>> unmasker("Ffe tulwanyisa abo abaagala okutabangula [MASK], Kimuli bwe yategeezezza.")

```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains. 
## Training data
This model was fine-tuned on JW300 + [BUKKEDDE](https://github.com/masakhane-io/masakhane-ner/tree/main/text_by_language/luganda) +[Luganda CC-100](http://data.statmt.org/cc-100/)

## Training procedure
This model was trained on a single NVIDIA V100 GPU

## Eval results on Test set (F-score, average over 5 runs)
Dataset| mBERT F1 | lg_bert F1
-|-|-
[MasakhaNER](https://github.com/masakhane-io/masakhane-ner) | 80.36 | 84.70

### BibTeX entry and citation info
By David Adelani
```

```


