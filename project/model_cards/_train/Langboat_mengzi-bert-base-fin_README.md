---
language: 
  - zh
license: apache-2.0
---
# Mengzi-BERT base fin model (Chinese)
Continue trained mengzi-bert-base with 20G financial news and research reports. Masked language modeling(MLM), part-of-speech(POS) tagging and sentence order prediction(SOP) are used as training task.

[Mengzi: Towards Lightweight yet Ingenious Pre-trained Models for Chinese](https://arxiv.org/abs/2110.06696)

## Usage
```python
from transformers import BertTokenizer, BertModel
tokenizer = BertTokenizer.from_pretrained("Langboat/mengzi-bert-base-fin")
model = BertModel.from_pretrained("Langboat/mengzi-bert-base-fin")
```

## Citation
If you find the technical report or resource is useful, please cite the following technical report in your paper.
```
@misc{zhang2021mengzi,
      title={Mengzi: Towards Lightweight yet Ingenious Pre-trained Models for Chinese}, 
      author={Zhuosheng Zhang and Hanqing Zhang and Keming Chen and Yuhang Guo and Jingyun Hua and Yulong Wang and Ming Zhou},
      year={2021},
      eprint={2110.06696},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}

```