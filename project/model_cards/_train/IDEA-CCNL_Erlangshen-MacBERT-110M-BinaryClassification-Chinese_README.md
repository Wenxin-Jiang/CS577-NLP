---
language: 
  - zh

license: apache-2.0

tags:
  - classification

inference: false

---

# Erlangshen- MacBERT-110M-BinaryClassification-Chinese   

- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM)
- Docs: [Fengshenbang-Docs](https://fengshenbang-doc.readthedocs.io/)

## 简介 Brief Introduction

1.1亿参数的MacBERT，在大规模二分类数据上预训练

The MacBERT with 110M parameters is pre-trained on large-scale binary classification data.

## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 通用 General  | 自然语言理解 NLU | 二郎神 Erlangshen | MacBERT      |      110M     |   Chinese     |

## 模型信息 Model Information


为了提高模型在二分类任务上效果，我们收集了大量开源二分类数据并使用meta- learning方法对其增量预训练。

To improve the model performance on the binary classification task, we collected numerous binary classification datasets for incremental pre-training based on meta-learning methods.

### 下游效果 Performance

在EPRSTMT任务上的效果：

The results on EPRSTMT:

| Model                                         | EPRSTMT  | 
| --------------------------------------------- | ------ | 
| MacBERT    |  74.96 |
| **Erlangshen- MacBERT-110M-BinaryClassification-Chinese** | 88.56  | 

## 使用 Usage

```python3
from transformers import AutoTokenizer, AutoModelForMaskedLM
tokenizer = AutoTokenizer.from_pretrained("IDEA-CCNL/Erlangshen-MacBERT-110M-BinaryClassification-Chinese")
model = AutoModelForMaskedLM.from_pretrained("IDEA-CCNL/Erlangshen-MacBERT-110M-BinaryClassification-Chinese")
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