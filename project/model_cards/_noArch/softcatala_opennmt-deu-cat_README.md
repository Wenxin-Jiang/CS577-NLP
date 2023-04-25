---
language: 
- de
- ca

tags:
- translation

library_name: opennmt
license: mit
metrics:
- bleu

inference: false
---

### Introduction

German - Catalan translation model for OpenNMT. These are the same models that we have in production at https://www.softcatala.org/traductor/.
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
model_dir = snapshot_download(repo_id="softcatala/opennmt-deu-cat", revision="main")

tokenizer=pyonmttok.Tokenizer(mode="none", sp_model_path = model_dir + "/sp_m.model")
tokenized=tokenizer.tokenize("Hallo Freunde")

translator = ctranslate2.Translator(model_dir)
translated = translator.translate_batch([tokenized[0]])
print(tokenizer.detokenize(translated[0][0]['tokens']))
```

## Benchmarks

| testset                               | BLEU  |
|---------------------------------------|-------|
| test dataset (from train/dev/test)   	| 37.2	|
| Flores101 dataset                     | 24.8	|

## Additional information
* https://github.com/Softcatala/nmt-models
* https://github.com/Softcatala/parallel-catalan-corpus
