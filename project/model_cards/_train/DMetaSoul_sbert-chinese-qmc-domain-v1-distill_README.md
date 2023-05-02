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

# DMetaSoul/sbert-chinese-qmc-domain-v1

此模型是基于之前开源[问题匹配模型](https://huggingface.co/DMetaSoul/sbert-chinese-qmc-domain-v1)的蒸馏轻量化版本（仅含4层 BERT），适用于**开放领域的问题匹配**场景，比如：


- 洗澡用什么香皂好？vs. 洗澡用什么香皂好
- 大连哪里拍婚纱照好点？ vs. 大连哪里拍婚纱照比较好
- 银行卡怎样挂失？vs. 银行卡丢了怎么挂失啊？

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

model = SentenceTransformer('DMetaSoul/sbert-chinese-qmc-domain-v1')
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
tokenizer = AutoTokenizer.from_pretrained('DMetaSoul/sbert-chinese-qmc-domain-v1')
model = AutoModel.from_pretrained('DMetaSoul/sbert-chinese-qmc-domain-v1')

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

这里主要跟蒸馏前对应的 teacher 模型作了对比

*性能：*

|            | Teacher               | Student             | Gap   |
| ---------- | --------------------- | ------------------- | ----- |
| Model      | BERT-12-layers (102M) | BERT-4-layers (45M) | 0.44x |
| Cost       | 23s                   | 12s                 | -47%  |
| Latency    | 38ms                  | 20ms                | -47%  |
| Throughput | 421 sentence/s        | 791 sentence/s      | 1.9x  |

*精度：*

|                | **csts_dev** | **csts_test** | **afqmc** | **lcqmc** | **bqcorpus** | **pawsx** | **xiaobu** | **Avg** |
| -------------- | ------------ | ------------- | --------- | --------- | ------------ | --------- | ---------- | ------- |
| **Teacher**    | 80.90%       | 76.62%        | 34.51%    | 77.05%    | 52.95%       | 12.97%    | 59.47%     | 56.35%  |
| **Student**    | 79.89%       | 76.34%        | 27.59%    | 69.26%    | 49.40%       | 9.06%     | 53.52%     | 52.15%  |
| **Gap** (abs.) | -            | -             | -         | -         | -            | -         | -          | -4.2%   |

*基于1万条数据测试，GPU设备是V100，batch_size=16，max_seq_len=256*

## Citing & Authors

E-mail: xiaowenbin@dmetasoul.com