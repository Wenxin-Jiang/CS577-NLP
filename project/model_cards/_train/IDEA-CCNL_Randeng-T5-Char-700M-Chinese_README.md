---
license: apache-2.0
language: zh

tags:
- T5
- chinese

inference: true

widget:
- text: "北京有悠久的 <extra_id_0>和 <extra_id_1>。"
- type: "text-generation"

---
# Randeng-T5-Char-700M-Chinese

- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM)
- Docs: [Fengshenbang-Docs](https://fengshenbang-doc.readthedocs.io/)

## 简介 Brief Introduction

善于处理NLT任务，中文版的T5-large，采用了BertTokenizer和中文字级别词典。

Good at handling NLT tasks, Chinese T5-large， use BertTokenizer and chinese vocab.

## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 通用 General | 自然语言转换 NLT | 燃灯 Randeng | T5 |      700M      |     中文-Chinese    |

## 模型信息 Model Information

对比T5-small，训练了它的中文版。为了更好适用于中文任务，我们仅使用BertTokenzier，和支持中英文的词表，并且使用了语料库自适应预训练(Corpus-Adaptive Pre-Training, CAPT)技术在悟道语料库(180G版本)继续预训练。预训练目标为破坏span。具体地，我们在预训练阶段中使用了[封神框架](https://github.com/IDEA-CCNL/Fengshenbang-LM/tree/main/fengshen)大概花费了16张A100约96小时。

Compared with T5-large, we implement its Chinese version. In order to use for chinese tasks, we use BertTokenizer and Chinese vocabulary, and Corpus-Adaptive Pre-Training (CAPT) on the WuDao Corpora (180 GB version). The pretraining objective is span corruption. Specifically, we use the [fengshen framework](https://github.com/IDEA-CCNL/Fengshenbang-LM/tree/main/fengshen) in the pre-training phase which cost about 96 hours with 16 A100 GPUs.

## 使用 Usage

```python
from transformers import T5ForConditionalGeneration, BertTokenizer
import torch

tokenizer=BertTokenizer.from_pretrained('IDEA-CCNL/Randeng-T5-Char-700M-Chinese', add_special_tokens=False)
model=T5ForConditionalGeneration.from_pretrained('IDEA-CCNL/Randeng-T5-Char-700M-Chinese')
```

## 引用 Citation

如果您在您的工作中使用了我们的模型，可以引用我们的[论文](https://arxiv.org/abs/2209.02970)：

If you are using the resource for your work, please cite the our [paper](https://arxiv.org/abs/2209.02970):

```text
@article{fengshenbang,
  author    = {Jiaxing Zhang and Ruyi Gan and Junjie Wang and Yuxiang Zhang and Lin Zhang and Ping Yang and Xinyu Gao and Ziwei Wu and Xiaoqun Dong and Junqing He and Jianheng Zhuo and Qi Yang and Yongfeng Huang and Xiayu Li and Yanghan Wu and Junyu Lu and Xinyu Zhu and Weifeng Chen and Ting Han and Kunhao Pan and Rui Wang and Hao Wang and Xiaojun Wu and Zhongshen Zeng and Chongpei Chen},
  title     = {Fengshenbang 1.0: Being the Foundation of Chinese Cognitive Intelligence},
  journal   = {CoRR},
  volume    = {abs/2209.02970},
  year      = {2022}
}
```

也可以引用我们的[网站](https://github.com/IDEA-CCNL/Fengshenbang-LM/):

You can also cite our [website](https://github.com/IDEA-CCNL/Fengshenbang-LM/):

```text
@misc{Fengshenbang-LM,
  title={Fengshenbang-LM},
  author={IDEA-CCNL},
  year={2021},
  howpublished={\url{https://github.com/IDEA-CCNL/Fengshenbang-LM}},
}
```
