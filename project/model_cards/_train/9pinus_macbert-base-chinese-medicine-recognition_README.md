---
license: apache-2.0
tags:
- Token Classification
language:
- zh

---


## Model description
This model is a fine-tuned version of bert-base-chinese for the purpose of medicine name recognition. We fine-tuned bert-base-chinese on a 500M dataset including 100K+ authorized medical articles on which we labeled all the medicine names. The model achieves 92% accuracy on our test dataset.

## Intended use
```python
>>> from transformers import (AutoModelForTokenClassification, AutoTokenizer)
>>> from transformers import pipeline

>>> hub_model_id = "9pinus/macbert-base-chinese-medicine-recognition"

>>> model = AutoModelForTokenClassification.from_pretrained(hub_model_id)
>>> tokenizer = AutoTokenizer.from_pretrained(hub_model_id)
>>> classifier = pipeline('ner', model=model, tokenizer=tokenizer)
>>> result = classifier("如果病情较重，可适当口服甲硝唑片、环酯红霉素片、吲哚美辛片等药物进行抗感染镇痛。")

>>> for item in result:
>>>     if item['entity'] == 1 or item['entity'] == 2:
>>>         print(item)

{'entity': 1, 'score': 0.99999595, 'index': 13, 'word': '甲', 'start': 12, 'end': 13}
{'entity': 2, 'score': 0.9999957, 'index': 14, 'word': '硝', 'start': 13, 'end': 14}
{'entity': 2, 'score': 0.99999166, 'index': 15, 'word': '唑', 'start': 14, 'end': 15}
{'entity': 2, 'score': 0.99898833, 'index': 16, 'word': '片', 'start': 15, 'end': 16}
{'entity': 1, 'score': 0.9999864, 'index': 18, 'word': '环', 'start': 17, 'end': 18}
{'entity': 2, 'score': 0.99999404, 'index': 19, 'word': '酯', 'start': 18, 'end': 19}
{'entity': 2, 'score': 0.99999475, 'index': 20, 'word': '红', 'start': 19, 'end': 20}
{'entity': 2, 'score': 0.9999964, 'index': 21, 'word': '霉', 'start': 20, 'end': 21}
{'entity': 2, 'score': 0.9999951, 'index': 22, 'word': '素', 'start': 21, 'end': 22}
{'entity': 2, 'score': 0.9990088, 'index': 23, 'word': '片', 'start': 22, 'end': 23}
{'entity': 1, 'score': 0.9999975, 'index': 25, 'word': '吲', 'start': 24, 'end': 25}
{'entity': 2, 'score': 0.9999957, 'index': 26, 'word': '哚', 'start': 25, 'end': 26}
{'entity': 2, 'score': 0.9999945, 'index': 27, 'word': '美', 'start': 26, 'end': 27}
{'entity': 2, 'score': 0.9999933, 'index': 28, 'word': '辛', 'start': 27, 'end': 28}
{'entity': 2, 'score': 0.99949837, 'index': 29, 'word': '片', 'start': 28, 'end': 29}
```

## Training and evaluation data

### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.17.0
- Tokenizers 0.10.3
