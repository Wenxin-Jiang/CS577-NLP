---
language: id
tags:
  - roberta-base-indonesia
license: mit
datasets:
  - wikipedia
widget:
  - text: "Gajah <mask> sedang makan di kebun binatang."
---

# Indonesian RoBERTa Base
## How to Use

### As Masked Language Model
```python
from transformers import pipeline

pretrained_name = "akahana/roberta-base-indonesia"

fill_mask = pipeline(
    "fill-mask",
    model=pretrained_name,
    tokenizer=pretrained_name
)

fill_mask("Gajah <mask> sedang makan di kebun binatang.")
```

### Feature Extraction in PyTorch
```python
from transformers import RobertaModel, RobertaTokenizerFast

pretrained_name = "akahana/roberta-base-indonesia"
model = RobertaModel.from_pretrained(pretrained_name)
tokenizer = RobertaTokenizerFast.from_pretrained(pretrained_name)

prompt = "Gajah <mask> sedang makan di kebun binatang."
encoded_input = tokenizer(prompt, return_tensors='pt')
output = model(**encoded_input)
```