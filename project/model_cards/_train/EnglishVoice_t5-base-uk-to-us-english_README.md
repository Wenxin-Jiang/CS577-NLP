---
language:
- en
tags:
- text2text-generation
- paraphrase-generation
license: apache-2.0
widget:
 - text: "UK to US: My favourite colour is yellow."
---

### About the model

The model has been trained on a dataset containing [264519 sentences with UK English spelling](https://www.englishvoice.ai/p/uk-to-us/ "264519 sentences with UK English spelling"), along with their US English equivalent.

The purpose of the model is to rewrite sentences from UK English to US English. It is capable not only of changing the spelling of words (such as "colour" to "color") but also changes the vocabulary appropriately (for example, "underground" to "subway", "solicitor" to "lawyer" and so on).

### Generation examples

| Input | Output |
| :------------ | :------------ |
| My favourite colour is yellow. | My favorite color is yellow. |
| I saw a bloke in yellow trainers at the underground station. | I saw a guy in yellow sneakers at the subway station. |
| You could have got hurt! | You could have gotten hurt! |

### The dataset

The dataset was developed by English Voice AI Labs. You can download it from our website:
[https://www.EnglishVoice.ai/](https://www.EnglishVoice.ai/ "https://www.EnglishVoice.ai/")

### Sample code

Sample Python code:

```python
import torch
from transformers import T5ForConditionalGeneration,T5Tokenizer

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = T5ForConditionalGeneration.from_pretrained("EnglishVoice/t5-base-uk-to-us-english")
tokenizer = T5Tokenizer.from_pretrained("EnglishVoice/t5-base-uk-to-us-english")
model = model.to(device)

input = "My favourite colour is yellow."

text =  "UK to US: " + input
encoding = tokenizer.encode_plus(text, return_tensors = "pt")
input_ids = encoding["input_ids"].to(device)
attention_masks = encoding["attention_mask"].to(device)
beam_outputs = model.generate(
    input_ids = input_ids,
    attention_mask = attention_masks,
    early_stopping = True,
)

result = tokenizer.decode(beam_outputs[0], skip_special_tokens=True)
print(result)

```

Output:

```My favorite color is yellow.```
