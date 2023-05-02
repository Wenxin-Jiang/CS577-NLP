---
language: de
widget:
- text: My name is Karl and I live in Aachen.
tags:
- translation 
datasets:
- wmt19
license: gpl
---

<h2> English to German Translation </h2>


Model Name: Tanhim/translation-En2De <br />
language: German or Deutsch  <br />
thumbnail: https://huggingface.co/Tanhim/translation-En2De <br />

### How to use
You can use this model directly with a pipeline for machine translation. Since the generation relies on some randomness, I
set a seed for reproducibility:
```python
>>> from transformers import pipeline, set_seed
>>> text_En2De= pipeline('translation', model='Tanhim/translation-En2De', tokenizer='Tanhim/translation-En2De')
>>> set_seed(42)
>>> text_En2De("My name is Karl and I live in Aachen")

```
### beta version