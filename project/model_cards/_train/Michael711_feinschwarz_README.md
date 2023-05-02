---
license: mit
tags:
- generated_from_trainer 
- de
model-index:
- name: feinesblack
  results: []
---

# feinschwarz

This model is a fine-tuned version of [dbmdz/german-gpt2](https://huggingface.co/dbmdz/german-gpt2). The dataset was compiled from all texts of https://www.feinschwarz.net (as of October 2021). The homepage gathers essayistic texts on theological topics.

The model will be used to explore the challenges of text-generating AI for theology with a hands on approach. Can an AI generate theological knowledge? Is a text by Karl Rahner of more value than an AI-generated text? Can we even distinguish a Rahner text from an AI-generated text in the future? And the crucial question: Would it be bad if not?

The model is a very first attempt and in its current version certainly not yet a danger for academic theology 🤓 

# Using the model

You can create text with the model using this code:

```python
from transformers import pipeline

pipe = pipeline('text-generation', model="Michael711/feinschwarz",
                 tokenizer="Michael711/feinschwarz")

text = pipe("Der Sinn des Lebens ist es", max_length=100)[0]["generated_text"]

print(text)
```

Have fun theologizing!