---
language: 
  - zh
license: apache-2.0
---


# Mengzi-BERT L6-H768 model (Chinese)

This model is a distilled version of mengzi-bert-large.

## Usage

```python
from transformers import BertTokenizer, BertModel
tokenizer = BertTokenizer.from_pretrained("Langboat/mengzi-bert-L6-H768")
model = BertModel.from_pretrained("Langboat/mengzi-bert-L6-H768")
```

## Scores on nine chinese tasks (without any data augmentation)
| Model | AFQMC | TNEWS | IFLYTEK | CMNLI | WSC | CSL | CMRC2018 | C3 | CHID |
|-|-|-|-|-|-|-|-|-|-|
|**Mengzi-BERT-L6-H768**| 74.75 | 56.68 | 60.22 | 81.10 | 84.87 | 85.77 | 78.06 | 65.49 | 80.59 |
|Mengzi-BERT-base| 74.58 | 57.97 | 60.68 | 82.12 | 87.50 | 85.40 | 78.54 | 71.70 | 84.16 |
|RoBERTa-wwm-ext| 74.30 | 57.51 | 60.80 | 80.70 | 67.20 | 80.67 | 77.59 | 67.06 | 83.78 |

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
