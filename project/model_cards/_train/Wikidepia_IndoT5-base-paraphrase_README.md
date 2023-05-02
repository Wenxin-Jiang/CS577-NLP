---
language:
- id
---
# Paraphrase Generation with IndoT5 Base

IndoT5-base trained on translated PAWS.

## Model in action

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Wikidepia/IndoT5-base-paraphrase")  
model = AutoModelForSeq2SeqLM.from_pretrained("Wikidepia/IndoT5-base-paraphrase")

sentence = "Anak anak melakukan piket kelas agar kebersihan kelas terjaga"
text =  "paraphrase: " + sentence + " </s>"

encoding = tokenizer(text, padding='longest', return_tensors="pt")
outputs = model.generate(
    input_ids=encoding["input_ids"], attention_mask=encoding["attention_mask"],
    max_length=512,
    do_sample=True,
    top_k=200,
    top_p=0.95,
    early_stopping=True,
    num_return_sequences=5
)
```

## Limitations

Sometimes paraphrase contain date which doesnt exists in the original text :/

## Acknowledgement

Thanks to Tensorflow Research Cloud for providing TPU v3-8s.