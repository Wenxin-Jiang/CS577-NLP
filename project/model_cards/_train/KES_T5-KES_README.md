---

language: en

tags:

- sentence correction

- text2text-generation

license: cc-by-nc-sa-4.0

datasets:

- jfleg

---

# Model
This model utilises T5-base pre-trained model. It was fine tuned using a modified version of the [JFLEG](https://arxiv.org/abs/1702.04066) dataset and [Happy Transformer framework](https://github.com/EricFillion/happy-transformer). This model was fine-tuned for sentence correction on normal English translations and positional English translations of local Caribbean English Creole. This model will be updated periodically as more data is compiled. For more on the Caribbean English Creole checkout the library [Caribe](https://pypi.org/project/Caribe/).

___


# Re-training/Fine Tuning

The results of fine-tuning resulted in a final accuracy of 92%


# Usage 



```python

from happytransformer import HappyTextToText, TTSettings

pre_trained_model="T5"
model = HappyTextToText(pre_trained_model, "KES/T5-KES")

arguments = TTSettings(num_beams=4, min_length=1)
sentence = "Wat iz your nam"

correction = model.generate_text("grammar: "+sentence, args=arguments)
if(correction.text.find(" .")):
    correction.text=correction.text.replace(" .", ".")

print(correction.text) # Correction: "What is your name?".

```
___
# Usage with Transformers

```python

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("KES/T5-KES")

model = AutoModelForSeq2SeqLM.from_pretrained("KES/T5-KES")

text = "I am lived with my parenmts "
inputs = tokenizer("grammar:"+text, truncation=True, return_tensors='pt')

output = model.generate(inputs['input_ids'], num_beams=4, max_length=512, early_stopping=True)
correction=tokenizer.batch_decode(output, skip_special_tokens=True)
print("".join(correction)) #Correction: I am living with my parents.

```
___
