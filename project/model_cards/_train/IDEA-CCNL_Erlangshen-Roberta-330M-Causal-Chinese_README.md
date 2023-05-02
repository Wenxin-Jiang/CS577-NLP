---
language: 
  - zh
license: apache-2.0

tags:
- roberta
- NLU
- NLI
- Chinese

inference: true

widget:
- text: "鲸鱼是哺乳动物，所有哺乳动物都是恒温动物[SEP]鲸鱼也是恒温动物"
- text: "葡萄树是阔叶植物，所有阔叶植物都不会落叶[SEP]葡萄树是落叶植物"
- text: "玉米价格持续上涨，饲料主要的来源是玉米[SEP]饲料价格可能会上涨"

---
# Erlangshen-Roberta-330M-Causal-Chinese

- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM)
- Docs: [Fengshenbang-Docs](https://fengshenbang-doc.readthedocs.io/)

## 简介 Brief Introduction

基于[chinese-roberta-wwm-ext-large](https://huggingface.co/hfl/chinese-roberta-wwm-ext-large)模型继续训练得到的中文因果关系判别模型。

This is a Chinese causality discriminative model trained from [chinese-roberta-wwm-ext-large](https://huggingface.co/hfl/chinese-roberta-wwm-ext-large).

## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 通用 General  | 自然语言理解 NLU | 二郎神 Erlangshen | Roberta |      330M      |    中文-因果关系推断 Chinese-Causal     |

## 模型信息 Model Information

### 数据准备 Corpus Preparation

* 因果语料库：同[Randeng-TransformerXL-5B-Deduction-Chinese](https://huggingface.co/IDEA-CCNL/Randeng-TransformerXL-5B-Deduction-Chinese)，基于悟道语料库（280G版本），通过关联词匹配、人工标注 + [GTSFactory](https://gtsfactory.com/)筛选、数据清洗等步骤获取的具有因果关系的句子对
* 重构NLI数据：对CMNLI、OCNLI数据集进行数据清洗，并将“蕴含”类别作为正例、其余类别作为负例转换为二分类数据集
* 预热数据集：以重构后的CMNLI数据集为基础，引入因果语料库样本平衡正负例数量


* Wudao Causal Corpus: Based on the Wudao corpus (280G version), sentence pairs with causality were obtained through logic indicator matching, manual annotation + [GTSFactory](https://gtsfactory.com/), and data cleaning.
* Reconstructed NLI data: After cleaning cmnli and ocnli dataset, we converted them into binary datasets by taking the "Entail" category as positive category and others as the negative.
* Warm-up dataset: Based on the reconstructed cmnli dataset, the number of each category is balanced using data from the Wudao Causal Corpus.



### 模型训练 Model Training

1. 基于[chinese-roberta-wwm-ext-large](https://huggingface.co/hfl/chinese-roberta-wwm-ext-large)模型，在预热数据集上微调预热
2. 作为判别模型与[Randeng-TransformerXL-5B-Deduction-Chinese](https://huggingface.co/IDEA-CCNL/Randeng-TransformerXL-5B-Deduction-Chinese)模型和[Randeng-TransformerXL-5B-Abduction-Chinese](https://huggingface.co/IDEA-CCNL/Randeng-TransformerXL-5B-Abduction-Chinese)模型进行自洽（Self-consistent）闭环训练：
    * 将预热数据集中样本的句子对拆散，分别作为原因和结果输入至[Randeng-TransformerXL-5B-Deduction-Chinese](https://huggingface.co/IDEA-CCNL/Randeng-TransformerXL-5B-Deduction-Chinese)模型和[Randeng-TransformerXL-5B-Abduction-Chinese](https://huggingface.co/IDEA-CCNL/Randeng-TransformerXL-5B-Abduction-Chinese)模型。两个生成模型基于核采样和贪心的方式进行因果推理和反绎推理，产生大量伪样本；
    * 本模型对伪样本句子对的因果关系进行打分，筛选供自身以及生成模型训练的样本

First, we fine-tuned [chinese-roberta-wwm-ext-large](https://huggingface.co/hfl/chinese-roberta-wwm-ext-large) model on our warm-up dataset.
Then, we conducted self-consistent learning on this model, cooperating with [Randeng-TransformerXL-5B-Deduction-Chinese](https://huggingface.co/IDEA-CCNL/Randeng-TransformerXL-5B-Deduction-Chinese) model and [Randeng-TransformerXL-5B-Abduction-Chinese](https://huggingface.co/IDEA-CCNL/Randeng-TransformerXL-5B-Abduction-Chinese) model.
Specifically, sentence pairs in the warm-up dataset were split and feed into [Randeng-TransformerXL-5B-Deduction-Chinese](https://huggingface.co/IDEA-CCNL/Randeng-TransformerXL-5B-Deduction-Chinese) model and [Randeng-TransformerXL-5B-Abduction-Chinese](https://huggingface.co/IDEA-CCNL/Randeng-TransformerXL-5B-Abduction-Chinese) model as premise and result respectively.
Two generative models performed deductive reasoning and abductive reasoning based on each sample respectively, generating a large number of pseudo-samples; [Erlangshen-Roberta-330M-Causal-Chinese](https://huggingface.co/IDEA-CCNL/Erlangshen-Roberta-330M-Causal-Chinese) scored the causality of the pseudo-samples and selected the training data for itself and the generative models in the next iteration.


### 模型效果 Performance for reference

|       | Warmup dataset (dev) |  Warmup dataset (test)    |  ocnli (Zero-shot) |
| :--------:    | :-----:  | :----:  |  :----:  |
| F1-score | 84.06  |  84.04    |   78.43    |
| Precision | 79.95  |  79.71    |   81.51    |
| Recall | 88.63  |  88.88    |   75.57    |

## 使用 Usage

``` python
from transformers import BertForSequenceClassification
from transformers import BertTokenizer
import torch
tokenizer=BertTokenizer.from_pretrained('Erlangshen-Roberta-330M-Causal-Chinese')
model=BertForSequenceClassification.from_pretrained('Erlangshen-Roberta-330M-Causal-Chinese')
texta='鲸鱼是哺乳动物，所有哺乳动物都是恒温动物'
textb='鲸鱼也是恒温动物'
output=model(torch.tensor([tokenizer.encode(texta,textb)]))
print(torch.nn.functional.softmax(output.logits,dim=-1))
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