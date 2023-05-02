---
tags:

#- translation

- text2text-generation

- Trinidadian Creole

- Caribbean dialect

license: apache-2.0

---

# Trinidad English Creole to English Translator 
This model utilises T5-base pre-trained model. It was fine tuned using a custom dataset for translation of Trinidad English Creole to English. This model will be updated periodically as more data is compiled. For more on the Caribbean English Creole checkout the library [Caribe](https://pypi.org/project/Caribe/).



___

# Usage with Transformers
```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("KES/TEC-English")

model = AutoModelForSeq2SeqLM.from_pretrained("KES/TEC-English")
text = "Dem men doh kno wat dey doing wid d money"
inputs = tokenizer("tec:"+text, truncation=True, return_tensors='pt')

output = model.generate(inputs['input_ids'], num_beams=4, max_length=512, early_stopping=True)
translation=tokenizer.batch_decode(output, skip_special_tokens=True)
print("".join(translation)) #translation: These men do not know what they are doing with the money.
```
___

