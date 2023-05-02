---
language: id
tags:
  - tiny-roberta-indonesia
license: mit
datasets:
  - wikipedia
widget:
  - text: "ikiryo adalah <mask> hantu dalam mitologi jepang."
---

# Indonesian tiny-RoBERTa
## How to Use

### As Masked Language Model
```python
from transformers import pipeline

pretrained_name = "akahana/tiny-roberta-indonesia"

fill_mask = pipeline(
    "fill-mask",
    model=pretrained_name,
    tokenizer=pretrained_name
)

fill_mask("ikiryo adalah <mask> hantu dalam mitologi jepang.")
```

### Feature Extraction in PyTorch
```python
from transformers import RobertaModel, RobertaTokenizerFast

pretrained_name = "akahana/tiny-roberta-indonesia"
model = RobertaModel.from_pretrained(pretrained_name)
tokenizer = RobertaTokenizerFast.from_pretrained(pretrained_name)

prompt = "ikiryo adalah <mask> hantu dalam mitologi jepang."
encoded_input = tokenizer(prompt, return_tensors='pt')
output = model(**encoded_input)
```