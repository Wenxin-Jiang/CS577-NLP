Hugging Face's logo
---
language: sw
datasets:

---
# xlm-roberta-base-finetuned-swahili
## Model description
**xlm-roberta-base-finetuned-swahili** is a **Swahili RoBERTa** model obtained by fine-tuning **xlm-roberta-base** model on Swahili language texts.  It provides **better performance** than the XLM-RoBERTa on text classification and named entity recognition datasets.  

Specifically, this model is a *xlm-roberta-base* model that was fine-tuned on Swahili corpus. 
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for masked token prediction.
```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='Davlan/xlm-roberta-base-finetuned-swahili')
>>> unmasker("Jumatatu, Bwana Kagame alielezea shirika la France24 huko <mask> kwamba hakuna uhalifu ulitendwa")
                    
[{'sequence': 'Jumatatu, Bwana Kagame alielezea shirika la France24 huko Ufaransa kwamba hakuna uhalifu ulitendwa', 
'score': 0.5077782273292542, 
'token': 190096, 
'token_str': 'Ufaransa'}, 
{'sequence': 'Jumatatu, Bwana Kagame alielezea shirika la France24 huko Paris kwamba hakuna uhalifu ulitendwa', 
'score': 0.3657738268375397, 
'token': 7270, 
'token_str': 'Paris'}, 
{'sequence': 'Jumatatu, Bwana Kagame alielezea shirika la France24 huko Gabon kwamba hakuna uhalifu ulitendwa', 
'score': 0.01592041552066803, 
'token': 176392, 
'token_str': 'Gabon'}, 
{'sequence': 'Jumatatu, Bwana Kagame alielezea shirika la France24 huko France kwamba hakuna uhalifu ulitendwa', 
'score': 0.010881908237934113, 
'token': 9942, 
'token_str': 'France'}, 
{'sequence': 'Jumatatu, Bwana Kagame alielezea shirika la France24 huko Marseille kwamba hakuna uhalifu ulitendwa', 
'score': 0.009554869495332241, 
'token': 185918, 
'token_str': 'Marseille'}]


```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains. 
## Training data
This model was fine-tuned on [Swahili CC-100](http://data.statmt.org/cc-100/)

## Training procedure
This model was trained on a single NVIDIA V100 GPU

## Eval results on Test set (F-score, average over 5 runs)
Dataset| XLM-R F1 | sw_roberta F1
-|-|-
[MasakhaNER](https://github.com/masakhane-io/masakhane-ner) | 87.55 | 89.46

### BibTeX entry and citation info
By David Adelani
```

```


