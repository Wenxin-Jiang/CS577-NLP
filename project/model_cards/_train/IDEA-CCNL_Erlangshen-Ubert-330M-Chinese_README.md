---
language: 
  - zh
license: apache-2.0

tags:
- bert
- NLU
- Sentiment
- Chinese

inference: false

---

# Erlangshen-Ubert-330M-Chinese

- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM)
- Docs: [Fengshenbang-Docs](https://fengshenbang-doc.readthedocs.io/)

## 简介 Brief Introduction

采用统一的框架处理多种抽取任务，AIWIN2022的冠军方案，3.3亿参数量的中文UBERT-Large。

Adopting a unified framework to handle multiple information extraction tasks, AIWIN2022's champion solution, Chinese UBERT-Large (330M).

## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 通用 General | 自然语言理解 NLU | 二郎神 Erlangshen | UBERT |      330M      |    中文 Chinese    |

## 模型信息 Model Information

参考论文：[Unified BERT for Few-shot Natural Language Understanding](https://arxiv.org/abs/2206.12094)

UBERT是[2022年AIWIN世界人工智能创新大赛：中文保险小样本多任务竞赛](http://ailab.aiwin.org.cn/competitions/68#results)的冠军解决方案。我们开发了一个基于类似BERT的骨干的多任务、多目标、统一的抽取任务框架。我们的UBERT在比赛A榜和B榜上均取得了第一名。因为比赛中的数据集在比赛结束后不再可用，我们开源的UBERT从多个任务中收集了70多个数据集（共1,065,069个样本）来进行预训练，并且我们选择了[MacBERT-Large](https://huggingface.co/hfl/chinese-macbert-large)作为骨干网络。除了支持开箱即用之外，我们的UBERT还可以用于各种场景，如NLI、实体识别和阅读理解。示例代码可以在[Github](https://github.com/IDEA-CCNL/Fengshenbang-LM/tree/dev/yangping/fengshen/examples/ubert)中找到。

UBERT was the winner solution in the [2022 AIWIN ARTIFICIAL INTELLIGENCE WORLD INNOVATIONS: Chinese Insurance Small Sample Multi-Task](http://ailab.aiwin.org.cn/competitions/68#results). We developed a unified framework based on BERT-like backbone for multiple tasks and objectives. Our UBERT owns first place, as described in leaderboards A and B. In addition to the unavailable datasets in the challenge, we carefully collect over 70 datasets (1,065,069 samples in total) from a variety of tasks for open-source UBERT. Moreover, we apply [MacBERT-Large](https://huggingface.co/hfl/chinese-macbert-large) as the backbone. Besides out-of-the-box functionality, our UBERT can be employed in various scenarios such as NLI, entity recognition, and reading comprehension. The example codes can be found in [Github](https://github.com/IDEA-CCNL/Fengshenbang-LM/tree/dev/yangping/fengshen/examples/ubert).

## 使用 Usage

Pip install fengshen

```python
git clone https://github.com/IDEA-CCNL/Fengshenbang-LM.git
cd Fengshenbang-LM
pip install --editable ./
```

Run the code

```python
import argparse
from fengshen import UbertPiplines

total_parser = argparse.ArgumentParser("TASK NAME")
total_parser = UbertPiplines.piplines_args(total_parser)
args = total_parser.parse_args()

args.pretrained_model_path = "IDEA-CCNL/Erlangshen-Ubert-330M-Chinese"

test_data=[
    {
        "task_type": "抽取任务", 
        "subtask_type": "实体识别", 
        "text": "这也让很多业主据此认为，雅清苑是政府公务员挤对了国家的经适房政策。", 
        "choices": [ 
            {"entity_type": "小区名字"}, 
            {"entity_type": "岗位职责"}
            ],
        "id": 0}
]

model = UbertPiplines(args)
result = model.predict(test_data)
for line in result:
    print(line)
```

## 引用 Citation

如果您在您的工作中使用了我们的模型，可以引用我们的对该模型的论文：

If you are using the resource for your work, please cite the our paper for this model:

```text
@article{fengshenbang/ubert,
  author    = {JunYu Lu and
               Ping Yang and
               Jiaxing Zhang and
               Ruyi Gan and
               Jing Yang},
  title     = {Unified {BERT} for Few-shot Natural Language Understanding},
  journal   = {CoRR},
  volume    = {abs/2206.12094},
  year      = {2022}
}
```

如果您在您的工作中使用了我们的模型，也可以引用我们的[总论文](https://arxiv.org/abs/2209.02970)：

If you are using the resource for your work, please cite the our [overview paper](https://arxiv.org/abs/2209.02970):

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
