---
language: 
  - en
  
inference: false
license: apache-2.0
---

# Yuyuan-GPT2-3.5B

- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM)
- Docs: [Fengshenbang-Docs](https://fengshenbang-doc.readthedocs.io/)

## 简介 Brief Introduction

目前最大的，医疗领域的生成语言模型GPT2。

The currently largest, generative language model GPT2 in the medical domain.

## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 特殊 Special | 领域 Domain | 余元 Yuyuan | GPT2 |      3.5B      |     -     |

## 模型信息 Model Information

我们采用与Wenzhong-GPT2-3.5B相同的架构，在50GB的医学(PubMed)语料库上进行预训练。我们使用了32个NVIDIA A100显卡大约7天。我们的Yuyuan-GPT2-3.5B是医疗领域最大的开源的GPT2模型。进一步地，模型可以通过计算困惑度（PPL）来判断事实。为了完成问答功能，我们将短语模式从疑问的形式转换为了陈述句。

We adopt the same architecture as Wenzhong-GPT2-3.5B to be pre-trained on 50 GB medical (PubMed) corpus. We use 32 NVIDIA A100 GPUs for about 7 days. Our Yuyuan-GPT2-3.5B is the largest open-source GPT2 model in the medical domain. We further allow the model to judge facts by computing perplexity (PPL). To accomplish question-and-answer functionality, we transform the phrase pattern from interrogative to declarative.

## 使用 Usage

### 加载模型 Loading Models

```python 
from transformers import GPT2Tokenizer, GPT2Model
tokenizer = GPT2Tokenizer.from_pretrained('IDEA-CCNL/Yuyuan-GPT2-3.5B')
model = GPT2Model.from_pretrained('IDEA-CCNL/Yuyuan-GPT2-3.5B')
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
```

### 使用示例 Usage Examples

```python
from transformers import pipeline, set_seed
set_seed(55)
generator = pipeline('text-generation', model='IDEA-CCNL/Yuyuan-GPT2-3.5B')
generator("Diabetics should not eat", max_length=30, num_return_sequences=1)

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
