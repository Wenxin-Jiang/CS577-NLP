---
license: mit
widget:
language:
- en

datasets:
- pytorrent
---

#  🔥 RoBERTa-MLM-based PyTorrent 1M 🔥
Pretrained weights based on [PyTorrent Dataset](https://github.com/fla-sil/PyTorrent) which is a curated data from a large official Python packages.
We use PyTorrent dataset to train a preliminary DistilBERT-Masked Language Modeling(MLM) model from scratch. The trained model, along with the dataset, aims to help researchers to easily and efficiently work on a large dataset of Python packages using only 5 lines of codes to load the transformer-based model. We use 1M raw Python scripts of PyTorrent that includes 12,350,000 LOC to train the model. We also train a byte-level Byte-pair encoding (BPE) tokenizer that includes 56,000 tokens, which is truncated LOC with the length of 50 to save computation resources. 

### Training Objective
This model is trained with a Masked Language Model (MLM) objective.

## How to use the model?
```python
from transformers import AutoTokenizer, AutoModel


tokenizer = AutoTokenizer.from_pretrained("Fujitsu/pytorrent")
model = AutoModel.from_pretrained("Fujitsu/pytorrent")
```
## Citation
Preprint: [https://arxiv.org/pdf/2110.01710.pdf](https://arxiv.org/pdf/2110.01710.pdf)
```
@misc{bahrami2021pytorrent,
      title={PyTorrent: A Python Library Corpus for Large-scale Language Models}, 
      author={Mehdi Bahrami and N. C. Shrikanth and Shade Ruangwan and Lei Liu and Yuji Mizobuchi and Masahiro Fukuyori and Wei-Peng Chen and Kazuki Munakata and Tim Menzies},
      year={2021},
      eprint={2110.01710},
      archivePrefix={arXiv},
      primaryClass={cs.SE},
      howpublished={https://arxiv.org/pdf/2110.01710},
}
```
