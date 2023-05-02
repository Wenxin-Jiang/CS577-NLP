---

language: en

tags:

- Trinidad and Tobago English Parser

- text2text-generation

- Caribe

license: cc-by-nc-sa-4.0

datasets:

- Custom dataset
- Creolised JFLEG

---
# Trinidad English Creole Parser
This model was trained as a parser to Trinidad  English Creole.

---

# Model
This model utilises T5-base pre-trained model. It was fine tuned using a combination of a custom dataset and creolised [JFLEG](https://arxiv.org/abs/1702.04066) dataset. JFLEG dataset was creolised using the file encoding feature of the Caribe library. For more on Caribbean Creole checkout the library [Caribe](https://pypi.org/project/Caribe/).

___


# Usage with Transformers

```python

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("KES/T5-TTParser")

model = AutoModelForSeq2SeqLM.from_pretrained("KES/T5-TTParser")

txt = "Ah have live with mi paremnts en London"
inputs = tokenizer("grammar:"+txt, truncation=True, return_tensors='pt')

output = model.generate(inputs['input_ids'], num_beams=4, max_length=512, early_stopping=True)
correction=tokenizer.batch_decode(output, skip_special_tokens=True)
print("".join(correction)) #Correction: Ah live with meh parents in London.

```