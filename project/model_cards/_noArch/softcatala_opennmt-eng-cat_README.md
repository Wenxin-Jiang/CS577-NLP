---
language: 
- ca
- en

tags:
- translation

library_name: opennmt
license: mit
metrics:
- bleu

inference: false
---

### Introduction

English - Catalan translation model based on OpenNMT. These are the same models that we have in production at https://www.softcatala.org/traductor/.


### Usage


```bash
pip3 install ctranslate2 pyonmttok
```

Simple translation using Python:

```python

import ctranslate2
from huggingface_hub import snapshot_download
model_dir = snapshot_download(repo_id="softcatala/opennmt-eng-cat", revision="main")

translator = ctranslate2.Translator(model_dir)
print(translator.translate_batch([["▁Hello", "▁world", "!"]]))
[[{'tokens': ['▁Hola', '▁món', '!']}]]

```

Simple tokenization & translation using Python:


```python
import ctranslate2
import pyonmttok
from huggingface_hub import snapshot_download
model_dir = snapshot_download(repo_id="softcatala/opennmt-eng-cat", revision="main")

tokenizer=pyonmttok.Tokenizer(mode="none", sp_model_path = model_dir + "/sp_m.model")
tokenized=tokenizer.tokenize("Hello world!")

import ctranslate2
translator = ctranslate2.Translator(model_dir)
translated = translator.translate_batch([tokenized[0]])
print(tokenizer.detokenize(translated[0][0]['tokens']))
Hola món!
```

## Benchmarks

| testset                               | BLEU  |
|---------------------------------------|-------|
| test dataset (from train/dev/test)   	| 45.2	|
| Flores101 dataset  					| 40.7	|

