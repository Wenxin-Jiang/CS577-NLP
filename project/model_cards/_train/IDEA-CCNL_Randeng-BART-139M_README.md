---
language: 
  - zh
license: apache-2.0

inference: true

widget:
- text: "桂林市是世界闻名<mask> ，它有悠久的<mask>"

---

# Randeng-BART-139M

- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM)
- Docs: [Fengshenbang-Docs](https://fengshenbang-doc.readthedocs.io/)

## 简介 Brief Introduction

善于处理NLT任务，中文版的BART-base。

Good at solving NLT tasks, Chinese BART-base.

## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 通用 General | 自然语言转换 NLT | 燃灯 Randeng | BART |      139M      |     中文-Chinese    |

## 模型信息 Model Information

参考论文：[BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension](https://arxiv.org/pdf/1910.13461.pdf)

为了得到一个中文版的BART-base，我们用悟道语料库(180G版本)进行预训练。具体地，我们在预训练阶段中使用了[封神框架](https://github.com/IDEA-CCNL/Fengshenbang-LM/tree/main/fengshen)大概花费了8张A100约3天。

To get a Chinese BART-base, we use WuDao Corpora (180 GB version) for pre-training. Specifically, we use the [fengshen framework](https://github.com/IDEA-CCNL/Fengshenbang-LM/tree/main/fengshen) in the pre-training phase which cost about 3 days with 8 A100 GPUs.

## 使用 Usage

```python
from transformers import BartForConditionalGeneration, AutoTokenizer, Text2TextGenerationPipeline
import torch

tokenizer=AutoTokenizer.from_pretrained('IDEA-CCNL/Randeng-BART-139M', use_fast=false)
model=BartForConditionalGeneration.from_pretrained('IDEA-CCNL/Randeng-BART-139M')
text = '桂林市是世界闻名<mask> ，它有悠久的<mask>'
text2text_generator = Text2TextGenerationPipeline(model, tokenizer)
print(text2text_generator(text, max_length=50, do_sample=False))
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
