---
tags:

#- translation

- text2text-generation

- Guyanese Creole

- Caribbean dialect

license: apache-2.0

---

# Guyanese English Creole to English Translator 
This model utilises T5-base pre-trained model. It was fine tuned using a custom dataset for translation of Guyanese English Creole to English. This model will be updated periodically as more data is compiled. For more on the Caribbean English Creoles checkout the library [Caribe](https://pypi.org/project/Caribe/).



___
# Usage with Transformers
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("KES/GEC-English")
model = AutoModelForSeq2SeqLM.from_pretrained("KES/GEC-English")
text = "Ah waan ah phone"
inputs = tokenizer("guy:"+text, truncation=True, return_tensors='pt')
output = model.generate(inputs['input_ids'], num_beams=4, max_length=512, early_stopping=True)
translation=tokenizer.batch_decode(output, skip_special_tokens=True)
print("".join(translation)) #translation: I want a phone.
```
___
