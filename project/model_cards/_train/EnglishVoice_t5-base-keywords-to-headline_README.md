
---
language:
- en
tags:
- text2text-generation
- paraphrase-generation
license: apache-2.0
widget:
 - text: "headline: weight loss"
---

### About the model

The model has been trained on [a dataset containing 138927 article titles](https://www.englishvoice.ai/p/keywords-and-titles/ "a dataset containing 138927 article titles") along with their keywords.

The purpose of the model is to generate suggestions of article headlines, given a keyword or multiple keywords.

### Generation examples

| Input | Output |
| :------------ | :------------ |
| weight loss  | The Last Weight Loss Plan: Lose Weight, Feel Great, and Get in Shape <br/>How to Lose Weight Without Giving Up Your Favorite Foods <br/> I Lost Weight and Finally Feel Good About My Body |
| property rental, property management | Property rental: The new way to make money <br/> We take the hassle out of property rental <br/> Is property management your new best friend? |
| diabetic diet plan | A diabetic diet plan that actually works! <br/> Lose weight, feel great, and live better with our diabetic diet plan! <br/> Diet has never been so tasty: Our diabetic diet plan puts you to the test! |

You can supply multiple keywords by separating them with commas. Higher temperature settings result in more creative headlines; we recommend testing first with the temperature set to 1.5.


### The dataset

The dataset was developed by English Voice AI Labs. You can download it from our website:
[https://www.EnglishVoice.ai/](https://www.EnglishVoice.ai/ "https://www.EnglishVoice.ai/")

### Sample code

Python code for generating headlines:

```python
import torch
from transformers import T5ForConditionalGeneration,T5Tokenizer

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = T5ForConditionalGeneration.from_pretrained("EnglishVoice/t5-base-keywords-to-headline")
tokenizer = T5Tokenizer.from_pretrained("EnglishVoice/t5-base-keywords-to-headline")
model = model.to(device)

keywords = "weight loss, weight pills"

text =  "headline: " + keywords
encoding = tokenizer.encode_plus(text, return_tensors = "pt")
input_ids = encoding["input_ids"].to(device)
attention_masks = encoding["attention_mask"].to(device)
beam_outputs = model.generate(
    input_ids = input_ids,
    attention_mask = attention_masks,
    do_sample = True,
    num_return_sequences = 5,
    temperature = 0.95,
    early_stopping = True,
    top_k = 50,
    top_p = 0.95,
)

for i in range(len(beam_outputs)):
    result = tokenizer.decode(beam_outputs[i], skip_special_tokens=True)
    print(result)
```

Sample result:

    I Am Losing Weight and I Love It!
    New Weight Loss Pill Helps You Get the Body You Want!
    I Lost Weight By Taking Pills!
    The Truth About Weight Loss Pills!
    The Best Weight Loss Pills Money Can Buy!
