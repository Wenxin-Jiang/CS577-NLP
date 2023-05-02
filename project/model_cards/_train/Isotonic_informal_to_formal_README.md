---
language: "en"
tags:
- style-transfer
- text2text-generation
- seq2seq
inference: true
---
​
# Formality Style Transfer
## Model description​
T5 Model for Formality Style Transfer. Trained on the GYAFC dataset.​

## How to use
​PyTorch model available​.
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
​
tokenizer = AutoTokenizer.from_pretrained("Isotonic/informal_to_formal")  
model = AutoModelForSeq2SeqLM.from_pretrained("Isotonic/informal_to_formal")
​
sentence = "will you look into these two deals and let me know"

text =  "Make the following sentence Formal: " + sentence + " </s>"

encoding = tokenizer.encode_plus(text,pad_to_max_length=True, return_tensors="pt")
input_ids, attention_masks = encoding["input_ids"].to("cuda"), encoding["attention_mask"].to("cuda")


outputs = model.generate(
    input_ids=input_ids, attention_mask=attention_masks,
    max_length=256,
    do_sample=True,
    top_k=120,
    top_p=0.95,
    early_stopping=True,
    num_return_sequences=5
)

for output in outputs:
    line = tokenizer.decode(output, skip_special_tokens=True,clean_up_tokenization_spaces=True)
    print(line)

​Output: "Would you look into the two deals in question, then let me know?"
```