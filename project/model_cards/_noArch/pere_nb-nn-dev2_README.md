---
language: no
license: cc-by-4.0
tags:
- translation
datasets:
- oscar
widget:
- text: Skriv inn en tekst som du ønsker å oversette til en annen målform.
---
# Norwegian T5 - Translation Bokmål Nynorsk - Development

## Description

This is the development version of the Bokmål-Nynorsk translator. If you want something that is stable, Please do run [this version](https://huggingface.co/pere/nb-nn-translation/) instead.


Here is an example of how to use the model from Python
```python
# Import libraries
from transformers import T5ForConditionalGeneration, AutoTokenizer
model = T5ForConditionalGeneration.from_pretrained('pere/nb-nn-dev',from_flax=True)
tokenizer = AutoTokenizer.from_pretrained('pere/nb-nn-dev')

#Encode the text
text = "Hun vil ikke gi bort sine personlige data."
inputs = tokenizer.encode(text, return_tensors="pt")
outputs = model.generate(inputs, max_length=255, num_beams=4, early_stopping=True)

#Decode and print the result
print(tokenizer.decode(outputs[0]))

```

Or if you like to use the pipeline instead

```python
# Set up the pipeline
from transformers import pipeline
translator = pipeline("translation", model='pere/nb-nn-dev')

# Do the translation
text = "Hun vil ikke gi bort sine personlige data."
print(translator(text, max_length=255))

```
