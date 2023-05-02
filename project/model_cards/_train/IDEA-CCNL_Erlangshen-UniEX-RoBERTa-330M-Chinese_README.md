---
license: apache-2.0
inference: false

tags:
- ner
- zero-shot
- information extruction

---

# Erlangshen-UniEX-RoBERTa-330M-Chinese

- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM/tree/main/fengshen/examples/UniEX/)
- Docs: [Fengshenbang-Docs](https://fengshenbang-doc.readthedocs.io/)

## 简介 Brief Introduction

UniEX 核心思想是将信息抽取转化为 token-pair 任务，为了将实体识别、关系抽取、事件抽取等抽取任务统一起来。我们使用一张表来识别实体的位置，其他表用来识别实体的类型或者关系的类型。此外，我们将标签信息和要抽取的文本拼接在一起，通过transformer进行编码。然后得到label的表示和文本的表示。最后通过Triaffine注意力机制使得所有任务可以共享一套参数。

The core idea of UniEX is to transform information extraction into token-pair tasks, in order to unify extraction tasks such as entity recognition, relationship extraction, and event extraction. We use one table to identify the location of the entity and other tables to identify the type of entity or the type of relationship. In addition, we stitch together the label information and the text to be extracted, and encode it through a transformer. Then get the representation of the label and the representation of the text. Finally, through the Triaffine attention mechanism, all tasks can share a set of parameters.


## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 抽取 Extraction | 自然语言理解 NLU | 二郎神 Erlangshen | RoBERTa |     110M    |     Chinese     |

## 模型信息 Model Information

由于 UniEX 可以统一所有抽取任务，且经过预训练之后，UniEX拥有着不错的 Few-Shot 和 Zero-shot 性能。为了方便社区做中文领域的抽取任务，我们使用百度百科这种结构化的数据构建弱监督数据集，通过清洗过后得到大概600M的数据，此外也收集了 16 个实体识别，7个关系抽取，6个事件抽取，11个阅读理解数据集。我们将收集得到的数据同时输入模型进行预训练。

Because UniEX can unify all extraction tasks, and after pre-training, UniEX has strong Few-Shot and Zero-shot performance. We use the structured data of Baidu Encyclopedia to build a weakly supervised data set. After cleaning, we get about 600M data. In addition, we also collected 16 entity recognition, 7 relationship extraction, 6 event extraction, and 11 reading comprehension data sets. . We mix this data and feed it to the model for pre-training


### 下游效果 Performance


## 使用 Usage
```shell
git clone https://github.com/IDEA-CCNL/Fengshenbang-LM.git
cd Fengshenbang-LM
pip install --editable .
```


```python3
import argparse
from fengshen import ...

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