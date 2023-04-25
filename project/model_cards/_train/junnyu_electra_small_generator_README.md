---
language: en
thumbnail: https://github.com/junnyu
tags:
- pytorch
- electra
- masked-lm
license: mit
datasets:
- openwebtext
---
# 一、 个人在openwebtext数据集上训练得到的electra-small模型

# 二、 复现结果(dev dataset)
|Model|CoLA|SST|MRPC|STS|QQP|MNLI|QNLI|RTE|Avg.|
|---|---|---|---|---|---|---|---|---|---|
|ELECTRA-Small-OWT(original)|56.8|88.3|87.4|86.8|88.3|78.9|87.9|68.5|80.36|
|**ELECTRA-Small-OWT (this)**| 55.82 |89.67|87.0|86.96|89.28|80.08|87.50|66.07|80.30|

# 三、 训练细节
- 数据集 openwebtext
- 训练batch_size 256
- 学习率lr  5e-4
- 最大句子长度max_seqlen  128
- 训练total step  62.5W
- GPU RTX3090
- 训练时间总共耗费2.5天

# 四、 使用
```python
from transformers import pipeline
fill_mask = pipeline(
	"fill-mask",
	model="junnyu/electra_small_generator",
	tokenizer="junnyu/electra_small_generator"
)
print(
	fill_mask("HuggingFace is creating a [MASK] that the community uses to solve NLP tasks.")
)
```