---
language: 
  - zh

inference: false

license: apache-2.0
---

# Erlangshen-SimCSE-110M-Chinese

- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM)
- Docs: [Fengshenbang-Docs](https://fengshenbang-doc.readthedocs.io/)

## 简介 Brief Introduction

基于simcse无监督版本，用搜集整理的中文NLI数据进行simcse有监督任务的训练。在中文句子对任务上有良好的效果。

**Erlangshen-SimCSE-110M-Chinese** is based on the unsupervised version of simcse, And training simcse supervised task with collected and sorted chinese NLI data for. It has good effect on the task in Chinese sentences pair.

## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 通用 General  | 自然语言生成 NLU | 二郎神 Erlangshen | Bert |      110M      |    中文 Chinese     |

## 模型信息 Model Information

为了获得一个通用句子向量表征的模型，我们基于bert-base模型用了大量的无监督数据和有监督数据进行对比学习，最终获得了一个无需微调就能够利用模型输出的[CLS]进行相似度判断的模型。与用bert模型在针对任务微调后，再进行句子相似度任务不同，我们的模型在预训练完成后直接具备提取句子向量的能力。在一些任务上有如下的测评效果：

In order to obtain a general sentence-embedding-model, we use a large number of unsupervised data and supervised data for comparative learning based on the Bert-base model, and finally obtained a model that can use the [CLS] output from the model to judge the similarity without fine-tuning. Different from the sentence similarity task after fine tuning the task with the bert model, our model has the ability to extract sentence vectors directly after pre training. In some tasks, the evaluation results are as follows:

|模型 | LCQMC | BQ | PAWSX | ATEC | STS-B |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
|Bert |	62	|38.62	|17.38	|28.98	|68.27|
|Bert-large|	63.78|	37.51|	18.63|	30.24|	68.87|
|RoBerta|	67.3|	39.89|	16.79|	30.57|	69.|36
|RoBerta large	|67.25	|38.39	|19.09	|30.85	|69.36|
|RoFormer|	63.58|	39.9	|17.52|	29.37	|67.32|
|SimBERT|	73.43|	40.98|	15.87|	31.24|	72|
|Erlangshen-SimCSE-110M-Chinese|74.94|	56.97|	21.84|	34.12|	70.5|

*备注:我们的模型是直接用[cls]，无whitening；其余模型是last avg + whitening*

*ps:Our model use [cls] directly，and no whitening；Other model use last avg and do whitening*

## 使用 Usage

### 加载模型 Loading Models

```python 
from transformers import AutoTokenizer,AutoModelForMaskedLM
model =AutoModelForMaskedLM.from_pretrained('IDEA-CCNL/Erlangshen-SimCSE-110M-Chinese')
tokenizer = AutoTokenizer.from_pretrained('IDEA-CCNL/Erlangshen-SimCSE-110M-Chinese')
```

### 使用示例 Usage Examples

```python
import torch
from sklearn.metrics.pairwise import cosine_similarity

texta = '今天天气真不错，我们去散步吧！'
textb = '今天天气真糟糕，还是在宅家里写bug吧！'
inputs_a = tokenizer(texta,return_tensors="pt")
inputs_b = tokenizer(textb,return_tensors="pt")

outputs_a = model(**inputs_a ,output_hidden_states=True)
texta_embedding = outputs_a.hidden_states[-1][:,0,:].squeeze()

outputs_b = model(**inputs_b ,output_hidden_states=True)
textb_embedding = outputs_b.hidden_states[-1][:,0,:].squeeze()

# if you use cuda, the text_embedding should be textb_embedding.cpu().numpy()
# 或者用torch.no_grad():
with torch.no_grad():
    silimarity_soce = cosine_similarity(texta_embedding.reshape(1,-1),textb_embedding .reshape(1,-1))[0][0]
print(silimarity_soce)
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