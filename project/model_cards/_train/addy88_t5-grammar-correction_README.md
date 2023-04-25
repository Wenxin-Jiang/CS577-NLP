### How to use
Here is how to use this model in PyTorch:
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("addy88/t5-grammar-correction")

model = AutoModelForSeq2SeqLM.from_pretrained("addy88/t5-grammar-correction")

input_ids = tokenizer('grammar: This sentences has has bads grammar.', return_tensors='pt').input_ids

outputs = model.generate(input_ids)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))

```