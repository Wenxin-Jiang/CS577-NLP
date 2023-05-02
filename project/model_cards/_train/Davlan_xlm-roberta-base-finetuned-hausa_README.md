Hugging Face's logo
---
language: ha
datasets:

---
# xlm-roberta-base-finetuned-hausa
## Model description
**xlm-roberta-base-finetuned-hausa** is a **Hausa RoBERTa** model obtained by fine-tuning **xlm-roberta-base** model on Hausa language texts.  It provides **better performance** than the XLM-RoBERTa on text classification and named entity recognition datasets.  

Specifically, this model is a *xlm-roberta-base* model that was fine-tuned on Hausa corpus. 
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for masked token prediction.
```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='Davlan/xlm-roberta-base-finetuned-hausa')
>>> unmasker("Shugaban <mask> Muhammadu Buhari ya amince da shawarar da ma’aikatar sufuri karkashin jagoranci")
                    
[{'sequence': '<s> Shugaban kasa Muhammadu Buhari ya amince da shawarar da ma’aikatar sufuri karkashin jagoranci</s>', 
'score': 0.8104371428489685, 
'token': 29762, 
'token_str': '▁kasa'}, 
{'sequence': '<s> Shugaban Najeriya Muhammadu Buhari ya amince da shawarar da ma’aikatar sufuri karkashin jagoranci</s>', 'score': 0.17371904850006104, 
'token': 49173, 
'token_str': '▁Najeriya'}, 
{'sequence': '<s> Shugaban kasar Muhammadu Buhari ya amince da shawarar da ma’aikatar sufuri karkashin jagoranci</s>', 'score': 0.006917025428265333, 
'token': 21221, 
'token_str': '▁kasar'}, 
{'sequence': '<s> Shugaban Nigeria Muhammadu Buhari ya amince da shawarar da ma’aikatar sufuri karkashin jagoranci</s>', 'score': 0.005785710643976927, 
'token': 72620, 
'token_str': '▁Nigeria'}, 
{'sequence': '<s> Shugaban Kasar Muhammadu Buhari ya amince da shawarar da ma’aikatar sufuri karkashin jagoranci</s>', 'score': 0.0010596115607768297, 
'token': 170255, 
'token_str': '▁Kasar'}]



```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains. 
## Training data
This model was fine-tuned on [Hausa CC-100](http://data.statmt.org/cc-100/)

## Training procedure
This model was trained on a single NVIDIA V100 GPU

## Eval results on Test set (F-score, average over 5 runs)
Dataset| XLM-R F1 | ha_roberta F1
-|-|-
[MasakhaNER](https://github.com/masakhane-io/masakhane-ner) | 86.10 | 91.47
[VOA Hausa Textclass](https://huggingface.co/datasets/hausa_voa_topics) | | 

### BibTeX entry and citation info
By David Adelani
```

```


