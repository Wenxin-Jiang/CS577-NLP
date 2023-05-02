Hugging Face's logo
---
language: yo
datasets:

---
# bert-base-multilingual-cased-finetuned-yoruba
## Model description
**bert-base-multilingual-cased-finetuned-yoruba** is a **Yoruba BERT** model obtained by fine-tuning **bert-base-multilingual-cased** model on Yorùbá language texts.  It provides **better performance** than the multilingual BERT on text classification and named entity recognition datasets.  

Specifically, this model is a *bert-base-multilingual-cased* model that was fine-tuned on Yorùbá corpus. 
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for masked token prediction.
```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='Davlan/bert-base-multilingual-cased-finetuned-yoruba')
>>> unmasker("Arẹmọ Phillip to jẹ ọkọ [MASK] Elizabeth to ti wa lori aisan ti dagbere faye lẹni ọdun mọkandilọgọrun")

[{'sequence': '[CLS] Arẹmọ Phillip to jẹ ọkọ Mary Elizabeth to ti wa lori aisan ti dagbere faye lẹni ọdun mọkandilọgọrun [SEP]', 'score': 0.1738305538892746, 
'token': 12176, 
'token_str': 'Mary'}, 
{'sequence': '[CLS] Arẹmọ Phillip to jẹ ọkọ Queen Elizabeth to ti wa lori aisan ti dagbere faye lẹni ọdun mọkandilọgọrun [SEP]', 'score': 0.16382873058319092, 
'token': 13704, 
'token_str': 'Queen'}, 
{'sequence': '[CLS] Arẹmọ Phillip to jẹ ọkọ ti Elizabeth to ti wa lori aisan ti dagbere faye lẹni ọdun mọkandilọgọrun [SEP]', 'score': 0.13272495567798615, 
'token': 14382, 
'token_str': 'ti'}, 
{'sequence': '[CLS] Arẹmọ Phillip to jẹ ọkọ King Elizabeth to ti wa lori aisan ti dagbere faye lẹni ọdun mọkandilọgọrun [SEP]', 'score': 0.12823280692100525, 
'token': 11515, 
'token_str': 'King'}, 
{'sequence': '[CLS] Arẹmọ Phillip to jẹ ọkọ Lady Elizabeth to ti wa lori aisan ti dagbere faye lẹni ọdun mọkandilọgọrun [SEP]', 'score': 0.07841219753026962, 
'token': 14005, 
'token_str': 'Lady'}]

```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains. 
## Training data
This model was fine-tuned on Bible, JW300, [Menyo-20k](https://huggingface.co/datasets/menyo20k_mt), [Yoruba Embedding corpus](https://huggingface.co/datasets/yoruba_text_c3) and [CC-Aligned](https://opus.nlpl.eu/), Wikipedia, news corpora (BBC Yoruba, VON Yoruba, Asejere, Alaroye), and other small datasets curated from friends.

## Training procedure
This model was trained on a single NVIDIA V100 GPU

## Eval results on Test set (F-score, average over 5 runs)
Dataset| mBERT F1 | yo_bert F1
-|-|-
[MasakhaNER](https://github.com/masakhane-io/masakhane-ner) | 78.97 | 82.58
[BBC Yorùbá Textclass](https://huggingface.co/datasets/yoruba_bbc_topics) | 75.13 | 79.11 

### BibTeX entry and citation info
By David Adelani
```

```


