---
language: 
  - zh
license: apache-2.0
widget:
- text: "生活的真谛是[MASK]。"
---


# Mengzi-BERT base model (Chinese)

Pretrained model on 300G Chinese corpus. Masked language modeling(MLM), part-of-speech(POS) tagging and sentence order prediction(SOP) are used as training task.

[Mengzi: A lightweight yet Powerful Chinese Pre-trained Language Model](https://arxiv.org/abs/2110.06696)

## Usage

```python
from transformers import BertTokenizer, BertModel
tokenizer = BertTokenizer.from_pretrained("Langboat/mengzi-bert-base")
model = BertModel.from_pretrained("Langboat/mengzi-bert-base")
```

## Scores on nine chinese tasks (without any data augmentation)
| Model | AFQMC | TNEWS | IFLYTEK | CMNLI | WSC | CSL | CMRC2018 | C3 | CHID |
|-|-|-|-|-|-|-|-|-|-|
|RoBERTa-wwm-ext| 74.30 | 57.51 | 60.80 | 80.70 | 67.20 | 80.67 | 77.59 | 67.06 | 83.78 |
|Mengzi-BERT-base| 74.58 | 57.97 | 60.68 | 82.12 | 87.50 | 85.40 | 78.54 | 71.70 | 84.16 |

RoBERTa-wwm-ext scores are from CLUE baseline


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