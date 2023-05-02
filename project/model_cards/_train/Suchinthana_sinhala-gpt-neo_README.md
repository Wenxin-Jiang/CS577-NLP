---
license: mit
widget:
- text: කවියා නුමුහු කළ නුවණ
- text: පිරිසිදු පානීය ජලය
language:
- si
pipeline_tag: text-generation
---

### Fine tuned GPT Neo 125M 

This model is fine tuned with a [Sinhala data set](https://github.com/TharukaCkasthuri/plagiarism_detection_dataset_sinhala) for Sinhala text generation.

### How to use

You can use this model directly with a pipeline for text generation. This example generates a different sequence each time it's run:

```py
>>> from transformers import pipeline
>>> generator = pipeline('text-generation', model='Suchinthana/sinhala-gpt-neo')
>>> generator("කවියා නුමුහු කළ නුවණ ", do_sample=True, max_length=500)

```