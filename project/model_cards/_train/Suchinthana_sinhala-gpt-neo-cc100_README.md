---
license: mit
widget:
- text: බාහිර බැටරි
- text: පිරිසිදු පානීය ජලය
language:
- si
pipeline_tag: text-generation
---

### Fine tuned GPT Neo 125M with CC100 Dataset

This model is fine tuned with more than 170,000 lines from [CC100 Sinhala data set](https://metatext.io/datasets/cc100-sinhala) for Sinhala text generation.

### How to use

You can use this model directly with a pipeline for text generation. This example generates a different sequence each time it's run:

```py
>>> from transformers import pipeline
>>> generator = pipeline('text-generation', model='Suchinthana/sinhala-gpt-neo-cc100')
>>> generator("අද මට ඊළඟ ", do_sample=True, max_length=500)
```
