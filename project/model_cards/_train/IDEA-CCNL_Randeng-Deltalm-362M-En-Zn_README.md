---
language: 
- zh
- en

tags:
- translation
inference: False
---

# Randeng-Deltalm-362M-En-Zh

- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM/blob/main/fengshen/examples/)
- Docs: [Fengshenbang-Docs](https://fengshenbang-doc.readthedocs.io/zh/latest/docs/%E7%87%83%E7%81%AF%E7%B3%BB%E5%88%97/)

## 简介 Brief Introduction

使用封神框架基于 Detalm base 进行finetune ，搜集的中英数据集（共3千万条）以及 iwslt的中英平行数据（20万），得到 英-> 中方向的翻译模型

Using the Fengshen-LM framework and finetuning based on detalm , get a translation model in the English -> Chinese direction

## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 通用 General | 自然语言转换 NLT | 燃灯 Randeng | Deltalm |      362M      |    翻译任务 En-Zh    |

## 模型信息 Model Information

参考论文：[DeltaLM: Encoder-Decoder Pre-training for Language Generation and Translation by Augmenting Pretrained Multilingual Encoders](https://arxiv.org/pdf/2106.13736v2.pdf)

### 下游效果 Performance

| datasets | bleu|
| ---- | ---- |
| florse101-en-zh | 40.22 |

## 使用 Usage

```python

# Need to download modeling_deltalm.py from Fengshenbang-LM github repo in advance,
# or you can download modeling_deltalm.py use wget https://huggingface.co/IDEA-CCNL/Randeng-Deltalm-362M-En-Zn/resolve/main/modeling_deltalm.py
# Strongly recommend you git clone the Fengshenbang-LM repo:
# 1. git clone https://github.com/IDEA-CCNL/Fengshenbang-LM
# 2. cd Fengshenbang-LM/fengshen/

from models.deltalm.modeling_deltalm import DeltalmForConditionalGeneration
from transformers import AutoTokenizer

model = DeltalmForConditionalGeneration.from_pretrained("IDEA-CCNL/Randeng-Deltalm-362M-En-Zn")
tokenizer = AutoTokenizer.from_pretrained("microsoft/infoxlm-base")

text = "In summer, especially, you'll need to watch out for mosquitoes if you decide to hike through the rainforest."
inputs = tokenizer(text, max_length=512, return_tensors="pt")

generate_ids = model.generate(inputs["input_ids"], max_length=512)
tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]

# model Output:
# 如果你决定徒步穿越热带雨林,你需要小心蚊子,尤其是在夏天。
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
