---
tags:

- text2text-generation

- Trinidadian Creole

- Caribbean dialect

license: apache-2.0

---

# Standard English to Trinidad English Creole Translator
This model utilises T5-base pre-trained model. It was fine tuned using a custom dataset for translation of English to Trinidad English Creole. This model will be updated periodically as more data is compiled. For more on the Caribbean English Creole checkout the library [Caribe](https://pypi.org/project/Caribe/).



___
# Usage with Transformers
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("KES/ENG-TEC")
model = AutoModelForSeq2SeqLM.from_pretrained("KES/ENG-TEC")
text = "Where are you going now?"
inputs = tokenizer("eng:"+text, truncation=True, return_tensors='pt')
output = model.generate(inputs['input_ids'], num_beams=4, max_length=512, early_stopping=True)
translation=tokenizer.batch_decode(output, skip_special_tokens=True)
print("".join(translation)) #translation: Weh yuh going now.
```
___
