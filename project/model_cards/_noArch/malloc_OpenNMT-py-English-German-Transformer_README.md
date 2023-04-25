---
language:
- de
- en
tags:
- translation
- pytorch
license: mit
datasets:
- WMT
metrics:
- bleu
---
# OpenNMT-py-English-German-Transformer
[OpenNMT-py](https://github.com/OpenNMT/OpenNMT-py) is the PyTorch version of the OpenNMT project, an open-source (MIT) neural machine translation framework.
OpenNMT has several [pretrained models](https://opennmt.net/Models-py/). This one is trained particularly for English to German translation.

- Configuration: Base Transformer configuration with [standard training options](http://opennmt.net/OpenNMT-py/FAQ.html#how-do-i-use-the-transformer-model-do-you-support-multi-gpu)
- Data: WMT with shared SentencePiece model
- BLEU: 
    - newstest2014 = 26.89
    - newstest2017 = 28.09