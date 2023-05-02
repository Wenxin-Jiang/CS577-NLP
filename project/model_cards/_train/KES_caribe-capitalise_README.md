---
license: mit

language: en

tags:

- sentence capitalization

- text2text-generation

---

This model utilises T5-base pre-trained model. It was fine tuned using a custom dataset This model was fine-tuned for capitalisation on text that includes multiple sentences or questions.  

Interested in Caribbean Creole? Checkout the library [Caribe](https://pypi.org/project/Caribe/) for more info and future updates.

___
# Usage with Transformers

```python

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("KES/caribe-capitalise")

model = AutoModelForSeq2SeqLM.from_pretrained("KES/caribe-capitalise")

text = "john is a boy. he is 12 years old. his sister's name is Joy."
inputs = tokenizer("text:"+text, truncation=True, return_tensors='pt')

output = model.generate(inputs['input_ids'], num_beams=4, max_length=512, early_stopping=True)
capitalised_text=tokenizer.batch_decode(output, skip_special_tokens=True)
print("".join(capitalised_text)) #Capitalised Output: John is a boy. He is 12 years old. His sister's name is Joy.

```
___