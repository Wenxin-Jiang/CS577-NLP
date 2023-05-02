---
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
widget:
  source_sentence: "亚丝娜"
  sentences:
    - "火影忍者"
    - "Sword Art Online"
    - "结城明日奈"
    - "アスナ"

---

# ACGVoc2vec

结构为[sentence-transformers](https://github.com/UKPLab/sentence-transformers)，使用其**distiluse-base-multilingual-cased-v2**预训练权重，以5e-5的学习率在动漫相关语句对数据集下进行微调，损失函数为MultipleNegativesRankingLoss。

数据集主要包括：

* Bangumi

  * 动画日文名-动画中文名
  * 动画日文名-简介
  * 动画中文名-简介
  * 动画中文名-标签
  * 动画日文名-角色
  * 动画中文名-角色
  * 声优日文名-声优中文名

* pixiv

  * 标签日文名-标签中文名
* AnimeList

  * 动画日文名-动画英文名

* 维基百科

  * 动画日文名-动画中文名
  * 动画日文名-动画英文名
  * 中英日详情页h2标题及其对应文本
  * 简介多语言对照（中日英）
  * 动画名-简介（中日英）  

* moegirl

  * 动画中文名的简介-简介
* 动画中文名+小标题-对应内容

在进行爬取，清洗，处理后得到8000w对文本对（还在持续增加），batchzise=80训练了20个epoch，使st的权重能够适应该问题空间，生成融合了领域知识的文本特征向量（体现为有关的文本距离更加接近，例如作品与登场人物，或者来自同一作品的登场人物）。

## Usage

Using this model becomes easy when you have [sentence-transformers](https://www.SBERT.net) installed:

```
pip install -U sentence-transformers
```

Then you can use the model like this:

```python
from sentence_transformers import SentenceTransformer
sentences = ["This is an example sentence", "Each sentence is converted"]

model = SentenceTransformer('OysterQAQ/ACGVoc2vec')
embeddings = model.encode(sentences)
print(embeddings)
```


## Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 128, 'do_lower_case': False}) with Transformer model: DistilBertModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
  (2): Dense({'in_features': 768, 'out_features': 512, 'bias': True, 'activation_function': 'torch.nn.modules.activation.Tanh'})
)
```

## Citing & Authors

<!--- Describe where people can find more information -->