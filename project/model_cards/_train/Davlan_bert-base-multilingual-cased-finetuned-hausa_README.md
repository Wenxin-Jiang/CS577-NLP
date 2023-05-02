Hugging Face's logo
---
language: ha
datasets:

---
# bert-base-multilingual-cased-finetuned-hausa
## Model description
**bert-base-multilingual-cased-finetuned-hausa** is a **Hausa BERT** model obtained by fine-tuning **bert-base-multilingual-cased** model on Hausa language texts.  It provides **better performance** than the multilingual BERT on text classification and named entity recognition datasets.  

Specifically, this model is a *bert-base-multilingual-cased* model that was fine-tuned on Hausa corpus. 
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for masked token prediction.
```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='Davlan/bert-base-multilingual-cased-finetuned-hausa')
>>> unmasker("Shugaban [MASK] Muhammadu Buhari ya amince da shawarar da ma’aikatar sufuri karkashin jagoranci")
                    
[{'sequence': 
'[CLS] Shugaban Nigeria Muhammadu Buhari ya amince da shawarar da ma [UNK] aikatar sufuri karkashin jagoranci [SEP]', 
'score': 0.9762618541717529, 
'token': 22045, 
'token_str': 'Nigeria'}, 
{'sequence': '[CLS] Shugaban Ka Muhammadu Buhari ya amince da shawarar da ma [UNK] aikatar sufuri karkashin jagoranci [SEP]', 'score': 0.007239189930260181, 
'token': 25444, 
'token_str': 'Ka'}, 
{'sequence': '[CLS] Shugaban, Muhammadu Buhari ya amince da shawarar da ma [UNK] aikatar sufuri karkashin jagoranci [SEP]', 'score': 0.001990817254409194, 
'token': 117, 
'token_str': ','}, 
{'sequence': '[CLS] Shugaban Ghana Muhammadu Buhari ya amince da shawarar da ma [UNK] aikatar sufuri karkashin jagoranci [SEP]', 'score': 0.001566368737258017, 
'token': 28682, 
'token_str': 'Ghana'}, 
{'sequence': '[CLS] Shugabanmu Muhammadu Buhari ya amince da shawarar da ma [UNK] aikatar sufuri karkashin jagoranci [SEP]', 'score': 0.0009375187801197171, 
'token': 11717, 
'token_str': '##mu'}]

```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains. 
## Training data
This model was fine-tuned on [Hausa CC-100](http://data.statmt.org/cc-100/)

## Training procedure
This model was trained on a single NVIDIA V100 GPU

## Eval results on Test set (F-score, average over 5 runs)
Dataset| mBERT F1 | ha_bert F1
-|-|-
[MasakhaNER](https://github.com/masakhane-io/masakhane-ner) | 86.65 | 91.31
[VOA Hausa Textclass](https://huggingface.co/datasets/hausa_voa_topics) | 84.76 | 90.98 

### BibTeX entry and citation info
By David Adelani
```

```


