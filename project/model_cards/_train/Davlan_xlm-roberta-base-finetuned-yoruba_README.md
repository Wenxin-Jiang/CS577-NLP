Hugging Face's logo
---
language: yo
datasets:

---
# xlm-roberta-base-finetuned-yoruba
## Model description
**xlm-roberta-base-finetuned-yoruba** is a **Yoruba RoBERTa** model obtained by fine-tuning **xlm-roberta-base** model on Yorùbá language texts.  It provides **better performance** than the XLM-RoBERTa on text classification and named entity recognition datasets.  

Specifically, this model is a *xlm-roberta-base* model that was fine-tuned on Yorùbá corpus. 
## Intended uses & limitations
#### How to use
You can use this model with Transformers *pipeline* for masked token prediction.
```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='Davlan/xlm-roberta-base-finetuned-yoruba')
>>> unmasker("Arẹmọ Phillip to jẹ ọkọ <mask> Elizabeth to ti wa lori aisan ti dagbere faye lẹni ọdun mọkandilọgọrun")
                    
[{'sequence': '<s> Arẹmọ Phillip to jẹ ọkọ Queen Elizabeth to ti wa lori aisan ti dagbere faye lẹni ọdun mọkandilọgọrun</s>', 'score': 0.24844281375408173, 
'token': 44109, 
'token_str': '▁Queen'}, 
{'sequence': '<s> Arẹmọ Phillip to jẹ ọkọ ile Elizabeth to ti wa lori aisan ti dagbere faye lẹni ọdun mọkandilọgọrun</s>', 'score': 0.1665010154247284, 
'token': 1350, 
'token_str': '▁ile'}, 
{'sequence': '<s> Arẹmọ Phillip to jẹ ọkọ ti Elizabeth to ti wa lori aisan ti dagbere faye lẹni ọdun mọkandilọgọrun</s>', 'score': 0.07604238390922546, 
'token': 1053, 
'token_str': '▁ti'}, 
{'sequence': '<s> Arẹmọ Phillip to jẹ ọkọ baba Elizabeth to ti wa lori aisan ti dagbere faye lẹni ọdun mọkandilọgọrun</s>', 'score': 0.06353845447301865, 
'token': 12878, 
'token_str': '▁baba'}, 
{'sequence': '<s> Arẹmọ Phillip to jẹ ọkọ Oba Elizabeth to ti wa lori aisan ti dagbere faye lẹni ọdun mọkandilọgọrun</s>', 'score': 0.03836742788553238, 
'token': 82879, 
'token_str': '▁Oba'}]



```
#### Limitations and bias
This model is limited by its training dataset of entity-annotated news articles from a specific span of time. This may not generalize well for all use cases in different domains. 
## Training data
This model was fine-tuned on Bible, JW300, [Menyo-20k](https://huggingface.co/datasets/menyo20k_mt), [Yoruba Embedding corpus](https://huggingface.co/datasets/yoruba_text_c3) and [CC-Aligned](https://opus.nlpl.eu/), Wikipedia, news corpora (BBC Yoruba, VON Yoruba, Asejere, Alaroye), and other small datasets curated from friends.

## Training procedure
This model was trained on a single NVIDIA V100 GPU

## Eval results on Test set (F-score, average over 5 runs)
Dataset| XLM-R F1 | yo_roberta F1
-|-|-
[MasakhaNER](https://github.com/masakhane-io/masakhane-ner) | 77.58 | 83.66 
[BBC Yorùbá Textclass](https://huggingface.co/datasets/yoruba_bbc_topics) |  | 

### BibTeX entry and citation info
By David Adelani
```

```


