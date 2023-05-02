---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
- semantic-search
- chinese
---

# DMetaSoul/sbert-chinese-dtm-domain-v1-distill

此模型是之前[开源对话匹配模型](https://huggingface.co/DMetaSoul/sbert-chinese-dtm-domain-v1)的蒸馏版本（仅4层 BERT），适用于**开放领域的对话匹配**场景（偏口语化），比如：

- 哪有好玩的 VS. 这附近有什么好玩的地方
- 定时25分钟 VS. 计时半个小时
- 我要听王琦的歌 VS. 放一首王琦的歌

离线训练好的大模型如果直接用于线上推理，对计算资源有苛刻的需求，而且难以满足业务环境对延迟、吞吐量等性能指标的要求，这里我们使用蒸馏手段来把大模型轻量化。从 12 层 BERT 蒸馏为 4 层后，模型参数量缩小到 44%，大概 latency 减半、throughput 翻倍、精度下降 4% 左右（具体结果详见下文评估小节）。

# Usage

## 1. Sentence-Transformers

通过  [sentence-transformers](https://www.SBERT.net) 框架来使用该模型，首先进行安装：

```
pip install -U sentence-transformers
```

然后使用下面的代码来载入该模型并进行文本表征向量的提取：

```python
from sentence_transformers import SentenceTransformer
sentences = ["我的儿子！他猛然间喊道，我的儿子在哪儿？", "我的儿子呢！他突然喊道，我的儿子在哪里？"]

model = SentenceTransformer('DMetaSoul/sbert-chinese-dtm-domain-v1-distill')
embeddings = model.encode(sentences)
print(embeddings)
```

## 2. HuggingFace Transformers

如果不想使用   [sentence-transformers](https://www.SBERT.net) 的话，也可以通过 HuggingFace Transformers 来载入该模型并进行文本向量抽取：

```python
from transformers import AutoTokenizer, AutoModel
import torch


#Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


# Sentences we want sentence embeddings for
sentences = ["我的儿子！他猛然间喊道，我的儿子在哪儿？", "我的儿子呢！他突然喊道，我的儿子在哪里？"]

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('DMetaSoul/sbert-chinese-dtm-domain-v1-distill')
model = AutoModel.from_pretrained('DMetaSoul/sbert-chinese-dtm-domain-v1-distill')

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

# Perform pooling. In this case, mean pooling.
sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

print("Sentence embeddings:")
print(sentence_embeddings)
```

## Evaluation

这里主要跟蒸馏前对应的 teacher 模型作了对比：

*性能*

|            | Teacher               | Student             | Gap   |
| ---------- | --------------------- | ------------------- | ----- |
| Model      | BERT-12-layers (102M) | BERT-4-layers (45M) | 0.44x |
| Cost       | 24s                   | 12s                 | -50%  |
| Latency    | 39ms                  | 19ms                | -51%  |
| Throughput | 407 sentence/s        | 815 sentence/s      | 2.0x  |

*精度*

|                | **csts_dev** | **csts_test** | **afqmc** | **lcqmc** | **bqcorpus** | **pawsx** | **xiaobu** | **Avg** |
| -------------- | ------------ | ------------- | --------- | --------- | ------------ | --------- | ---------- | ------- |
| **Teacher**    | 78.35%       | 74.45%        | 32.17%    | 75.95%    | 44.00%       | 14.50%    | 66.84%     | 55.17%  |
| **Student**    | 77.99%       | 73.95%        | 27.20%    | 67.49%    | 43.90%       | 10.79%    | 58.21%     | 51.36%  |
| **Gap** (abs.) | -            | -             | -         | -         | -            | -         | -          | -3.81%  |

*基于1万条数据测试，GPU设备是V100，batch_size=16，max_seq_len=256*

## Citing & Authors

E-mail: xiaowenbin@dmetasoul.com