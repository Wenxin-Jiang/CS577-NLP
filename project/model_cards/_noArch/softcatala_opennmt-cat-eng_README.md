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

Catalan - English translation model for OpenNMT. These are the same models that we have in production at https://www.softcatala.org/traductor/.
The models are quantified for low latency.

### Usage

Install the necessary dependencies:


```bash
pip3 install ctranslate2 pyonmttok
```


Simple tokenization & translation using Python:


```python
import ctranslate2
import pyonmttok
from huggingface_hub import snapshot_download
model_dir = snapshot_download(repo_id="softcatala/opennmt-cat-eng", revision="main")

tokenizer=pyonmttok.Tokenizer(mode="none", sp_model_path = model_dir + "/sp_m.model")
tokenized=tokenizer.tokenize("Hola món")

translator = ctranslate2.Translator(model_dir)
translated = translator.translate_batch([tokenized[0]])
print(tokenizer.detokenize(translated[0][0]['tokens']))
```

## Benchmarks

| testset                               | BLEU  |
|---------------------------------------|-------|
| test dataset (from train/dev/test)   	| 46.9	|
| Flores101 dataset                     | 41.2	|

## Additional information
* https://github.com/Softcatala/nmt-models
* https://github.com/Softcatala/parallel-catalan-corpus
