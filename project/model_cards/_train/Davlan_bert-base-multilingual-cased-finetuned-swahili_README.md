Hugging Face's logo
---
language: ha
datasets:

---
# bert-base-multilingual-cased-finetuned-swahili
## Model description
**bert-base-multilingual-cased-finetuned-swahili** is a **Swahili BERT** model obtained by fine-tuning **bert-base-multilingual-cased** model on Swahili language texts.  It provides **better performance** than the multilingual BERT on text classification and named entity recognition datasets.  

Specifically, this model is a *bert-base-multilingual-cased* model that was fine-tuned on Swahili corpus. 
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for masked token prediction.
```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='Davlan/bert-base-multilingual-cased-finetuned-swahili')
>>> unmasker("Jumatatu, Bwana Kagame alielezea shirika la France24 huko [MASK] kwamba "hakuna uhalifu ulitendwa")
                    
[{'sequence': 'Jumatatu, Bwana Kagame alielezea shirika la France24 huko Paris kwamba hakuna uhalifu ulitendwa', 
'score': 0.31642526388168335, 
'token': 10728, 
'token_str': 'Paris'}, 
{'sequence': 'Jumatatu, Bwana Kagame alielezea shirika la France24 huko Rwanda kwamba hakuna uhalifu ulitendwa', 
'score': 0.15753623843193054, 
'token': 57557, 
'token_str': 'Rwanda'}, 
{'sequence': 'Jumatatu, Bwana Kagame alielezea shirika la France24 huko Burundi kwamba hakuna uhalifu ulitendwa', 
'score': 0.07211585342884064, 
'token': 57824, 
'token_str': 'Burundi'}, 
{'sequence': 'Jumatatu, Bwana Kagame alielezea shirika la France24 huko France kwamba hakuna uhalifu ulitendwa', 
'score': 0.029844321310520172, 
'token': 10688, 
'token_str': 'France'}, 
{'sequence': 'Jumatatu, Bwana Kagame alielezea shirika la France24 huko Senegal kwamba hakuna uhalifu ulitendwa', 
'score': 0.0265930388122797, 
'token': 38052, 
'token_str': 'Senegal'}]

```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains. 
## Training data
This model was fine-tuned on [Swahili CC-100](http://data.statmt.org/cc-100/)

## Training procedure
This model was trained on a single NVIDIA V100 GPU

## Eval results on Test set (F-score, average over 5 runs)
Dataset| mBERT F1 | sw_bert F1
-|-|-
[MasakhaNER](https://github.com/masakhane-io/masakhane-ner) | 86.80 | 89.36 

### BibTeX entry and citation info
By David Adelani
```

```


