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

# DMetaSoul/sbert-chinese-qmc-finance-v1

此模型基于 [bert-base-chinese](https://huggingface.co/bert-base-chinese) 版本 BERT 模型，在大规模银行问题匹配数据集（[BQCorpus](http://icrc.hitsz.edu.cn/info/1037/1162.htm)）上进行训练调优，适用于**金融领域的问题匹配**场景，比如：

- 8千日利息400元? VS 10000元日利息多少钱
- 提前还款是按全额计息 VS 还款扣款不成功怎么还款？
- 为什么我借钱交易失败 VS 刚申请的借款为什么会失败

注：此模型的[轻量化版本](https://huggingface.co/DMetaSoul/sbert-chinese-qmc-finance-v1-distill)，也已经开源啦！

# Usage

## 1. Sentence-Transformers

通过  [sentence-transformers](https://www.SBERT.net) 框架来使用该模型，首先进行安装：

```
pip install -U sentence-transformers
```

然后使用下面的代码来载入该模型并进行文本表征向量的提取：

```python
from sentence_transformers import SentenceTransformer
sentences = ["到期不能按时还款怎么办", "剩余欠款还有多少？"]

model = SentenceTransformer('DMetaSoul/sbert-chinese-qmc-finance-v1')
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
sentences = ["到期不能按时还款怎么办", "剩余欠款还有多少？"]

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('DMetaSoul/sbert-chinese-qmc-finance-v1')
model = AutoModel.from_pretrained('DMetaSoul/sbert-chinese-qmc-finance-v1')

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

该模型在公开的几个语义匹配数据集上进行了评测，计算了向量相似度跟真实标签之间的相关性系数：

|                                  | **csts_dev** | **csts_test** | **afqmc** | **lcqmc** | **bqcorpus** | **pawsx** | **xiaobu** |
| -------------------------------- | ------------ | ------------- | --------- | --------- | ------------ | --------- | ---------- |
| **sbert-chinese-qmc-finance-v1** | 77.40%       | 74.55%        | 36.01%    | 75.75%    | 73.25%       | 11.58%    | 54.76%     |

## Citing & Authors

E-mail: xiaowenbin@dmetasoul.com