---
language: zh
tags:
- summarization
inference: False
---

# Randeng-Pegasus-523M-Summary-Chinese

- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM/blob/main/fengshen/examples/summary/randeng_pegasus_523M_summary.sh)
- Docs: [Fengshenbang-Docs](https://fengshenbang-doc.readthedocs.io/zh/latest/docs/%E7%87%83%E7%81%AF%E7%B3%BB%E5%88%97/Randeng-Pegasus-523M-Summary-Chinese.html)

## 简介 Brief Introduction

善于处理摘要任务，在数个中文摘要数据集上微调后的，中文版的PAGASUS-large。

Good at solving text summarization tasks, after fine-tuning on multiple Chinese text summarization datasets, Chinese PAGASUS-large.

## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 通用 General | 自然语言转换 NLT | 燃灯 Randeng | PEFASUS |      523M      |    文本摘要任务-中文 Summary-Chinese    |


## 模型信息 Model Information

参考论文：[PEGASUS: Pre-training with Extracted Gap-sentences for Abstractive Summarization](https://arxiv.org/pdf/1912.08777.pdf)

基于[Randeng-Pegasus-523M-Chinese](https://huggingface.co/IDEA-CCNL/Randeng-Pegasus-523M-Chinese)，我们在收集的7个中文领域的文本摘要数据集（约4M个样本）上微调了它，得到了summary版本。这7个数据集为：education, new2016zh, nlpcc, shence, sohu, thucnews和weibo。

Based on [Randeng-Pegasus-523M-Chinese](https://huggingface.co/IDEA-CCNL/Randeng-Pegasus-523M-Chinese), we fine-tuned a text summarization version (summary) on 7 Chinese text summarization datasets, with totaling around 4M samples. The datasets include: education, new2016zh, nlpcc, shence, sohu, thucnews and weibo.

### 下游效果 Performance

| datasets | rouge-1 | rouge-2 | rouge-L |
| ---- | ---- | ---- | ---- |
| LCSTS | 48.00 | 35.24 | 44.70 |

## 使用 Usage

```python

from transformers import PegasusForConditionalGeneration
# Need to download tokenizers_pegasus.py and other Python script from Fengshenbang-LM github repo in advance,
# or you can download tokenizers_pegasus.py and data_utils.py in https://huggingface.co/IDEA-CCNL/Randeng_Pegasus_523M/tree/main
# Strongly recommend you git clone the Fengshenbang-LM repo:
# 1. git clone https://github.com/IDEA-CCNL/Fengshenbang-LM
# 2. cd Fengshenbang-LM/fengshen/examples/pegasus/
# and then you will see the tokenizers_pegasus.py and data_utils.py which are needed by pegasus model
from tokenizers_pegasus import PegasusTokenizer

model = PegasusForConditionalGeneration.from_pretrained("IDEA-CCNL/Randeng-Pegasus-523M-Summary-Chinese")
tokenizer = PegasusTokenizer.from_pretrained("IDEA-CCNL/Randeng-Pegasus-523M-Summary-Chinese")

text = "据微信公众号“界面”报道，4日上午10点左右，中国发改委反垄断调查小组突击查访奔驰上海办事处，调取数据材料，并对多名奔驰高管进行了约谈。截止昨日晚9点，包括北京梅赛德斯-奔驰销售服务有限公司东区总经理在内的多名管理人员仍留在上海办公室内"
inputs = tokenizer(text, max_length=1024, return_tensors="pt")

# Generate Summary
summary_ids = model.generate(inputs["input_ids"])
tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]

# model Output: 反垄断调查小组突击查访奔驰上海办事处，对多名奔驰高管进行约谈
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