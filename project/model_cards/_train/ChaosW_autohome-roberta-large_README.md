---
language: 
  - zh

license: mit

tags:
  - RoBERTa

inference: true

widget:
- text: "生活的真谛是[MASK]"
---

# autohome-roberta-large

## 简介 Brief Introduction

善于处理NLU任务，采用全词掩码的，中文版的1.1亿参数RoBERTa-large。


## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 通用 General  | 自然语言理解 NLU | RoBERTa | RoBERTa |      390M      |    中文 Chinese     |


## 模型信息 Model Information

参考论文：[RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692)

为了得到一个中文版的autohome-roberta-large（390M），我们用autohome口碑板块语料库(1.2G)进行二次预训练。模型初始化参数采用hfl/chinese-bert-wwm-ext-large的参数进行初始化，我们在MLM中使用了全词掩码(wwm)的方式。具体地，我们在二次预训练阶段中使用了[transformers框架](https://github.com/huggingface/transformers)大概花费了4张A100约11小时。


## 使用 Usage

```python
from transformers import AutoModelForMaskedLM, AutoTokenizer, FillMaskPipeline
import torch

tokenizer=AutoTokenizer.from_pretrained('ChaosW/autohome-roberta-large')
model=AutoModelForMaskedLM.from_pretrained('ChaosW/autohome-roberta-large')
text = '生活的真谛是[MASK]。'
fillmask_pipe = FillMaskPipeline(model, tokenizer, device=0)
print(fillmask_pipe(text, top_k=10))
```
## 参考 Reference
本readme参考 https://huggingface.co/IDEA-CCNL/Erlangshen-DeBERTa-v2-97M-Chinese

## 下一步计划 Feature Work
下一步将推出基于汽车论坛数据的定制化预训练模型