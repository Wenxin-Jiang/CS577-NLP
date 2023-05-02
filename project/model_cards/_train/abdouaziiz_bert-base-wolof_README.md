---
language: wo
tags:
- bert
- language-model
- wo
- wolof 
---

# Soraberta: Unsupervised Language Model Pre-training for Wolof

**bert-base-wolof** is pretrained bert-base model on wolof language  .

## Soraberta models

| Model name | Number of layers | Attention Heads | Embedding Dimension | Total Parameters |
| :------:       |   :---: | :---: | :---: | :---: |
| `bert-base` | 6    | 12   | 514   | 56931622 M |
 



## Using Soraberta with Hugging Face's Transformers


```python
>>> from transformers import pipeline
>>> unmasker = pipeline('fill-mask', model='abdouaziiz/bert-base-wolof')
>>> unmasker("kuy yoot du [MASK].")

[{'sequence': '[CLS] kuy yoot du seqet. [SEP]',
  'score': 0.09505125880241394,
  'token': 13578},
 {'sequence': '[CLS] kuy yoot du daw. [SEP]',
  'score': 0.08882280439138412,
  'token': 679},
 {'sequence': '[CLS] kuy yoot du yoot. [SEP]',
  'score': 0.057790059596300125,
  'token': 5117},
 {'sequence': '[CLS] kuy yoot du seqat. [SEP]',
  'score': 0.05671025067567825,
  'token': 4992},
 {'sequence': '[CLS] kuy yoot du yaqu. [SEP]',
  'score': 0.0469999685883522,
  'token': 1735}]
```

## Training data
The data sources are [Bible OT](http://biblewolof.com/) , [WOLOF-ONLINE](http://www.wolof-online.com/) 
[ALFFA_PUBLIC](https://github.com/getalp/ALFFA_PUBLIC/tree/master/ASR/WOLOF)



## Contact

Please contact abdouaziz@gmail.com for any question, feedback or request.