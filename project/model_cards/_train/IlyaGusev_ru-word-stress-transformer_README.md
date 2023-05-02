---
language: 
- ru
tags:
- token-classification
license: apache-2.0
inference: false

---

# RuWordStressTransformer

## Model description

Transformer encoder for predicting word stress in Russian.

## Intended uses & limitations

#### How to use

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

model_name = "IlyaGusev/ru-word-stress-transformer"
tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    trust_remote_code=True,
    revision="bae83dd"
)
model = AutoModelForTokenClassification.from_pretrained(model_name)
pipe = pipeline(
    "token-classification",
    model=model,
    tokenizer=tokenizer,
    device=-1,
    aggregation_strategy="none",
    ignore_labels=("NO",)
)
text = "щеколда"
print(text)
index = pipe(text)[0]["index"]
print(text[:index] + "'" + text[index:])
```

Colab: [link](https://colab.research.google.com/drive/1I61aDezhxMVZzHQQfpn7Wqn-ydbndO6i)