## bert-from-clip-chinese pretrained model
该预训练权重是从BertCLIP预训练模型中单独取出来的Bert的权重，BertCLIP是中文版本的CLIP预训练模型，基于LiT-tuning（Locked-image Text tuning）的策略，
使用140万中文图文对数据进行多模态对比学习预训练。

Github: [CLIP-Chinese](https://github.com/yangjianxin1/CLIP-Chinese)

Bolg: [CLIP-Chinese：中文多模态对比学习CLIP预训练模型](https://mp.weixin.qq.com/s/6gQX91M-Lt7eiMimhYRJEw)

## Usage
可以直接使用Huggingface的BertModel直接加载该预训练权重，进行下游的任务。

```python
from transformers import BertTokenizer, BertModel

model_name_or_path = 'YeungNLP/bert-from-clip-chinese-1M'
tokenizer = BertTokenizer.from_pretrained(model_name_or_path)
model = BertModel.from_pretrained(model_name_or_path)
```