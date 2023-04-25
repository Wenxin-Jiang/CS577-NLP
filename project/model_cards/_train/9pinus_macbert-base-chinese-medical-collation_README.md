---
license: apache-2.0
language: zh
tags:
- Token Classification
metrics:
- precision
- recall
- f1
- accuracy
---

## Model description

This model is a fine-tuned version of macbert for the purpose of spell checking in medical application scenarios. We fine-tuned macbert Chinese base version on a 300M dataset including 60K+ authorized medical articles. We proposed to randomly confuse 30% sentences of these articles by adding noise with a either visually or phonologically resembled characters. Consequently, the fine-tuned model can achieve 96% accuracy on our test dataset. 

## Intended uses & limitations

You can use this model directly with a pipeline for token classification:
```python
>>> from transformers import (AutoModelForTokenClassification, AutoTokenizer)
>>> from transformers import pipeline

>>> hub_model_id = "9pinus/macbert-base-chinese-medical-collation"

>>> model = AutoModelForTokenClassification.from_pretrained(hub_model_id)
>>> tokenizer = AutoTokenizer.from_pretrained(hub_model_id)
>>> classifier = pipeline('ner', model=model, tokenizer=tokenizer)
>>> result = classifier("如果病情较重，可适当口服甲肖唑片、环酯红霉素片等药物进行抗感染镇痛。")

>>> for item in result:
>>>     if item['entity'] == 1:
>>>         print(item)

{'entity': 1, 'score': 0.58127016, 'index': 14, 'word': '肖', 'start': 13, 'end': 14}

```

### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.17.0
- Tokenizers 0.10.3
