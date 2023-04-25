---
language:
- de
- en
tags:
- translation
- pytorch
license: mit
datasets:
- IWSLT ‘14 DE-EN
metrics:
- bleu
---
# OpenNMT-py-English-German-Transformer
[OpenNMT-py](https://github.com/OpenNMT/OpenNMT-py) is the PyTorch version of the OpenNMT project, an open-source (MIT) neural machine translation framework.
OpenNMT has several [pretrained models](https://opennmt.net/Models-py/). This one is trained particularly for German to English translation.

- Configuration: 2-layer BiLSTM with hidden size 500 trained for 20 epochs
- Data: IWSLT ‘14 DE-EN
- BLEU: 30.33