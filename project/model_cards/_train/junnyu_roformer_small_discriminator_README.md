---
language: en
thumbnail: https://github.com/junnyu
tags:
- pytorch
- electra
- roformer
- rotary position embedding
license: mit
datasets:
- openwebtext
---
# 一、 个人在openwebtext数据集上添加rotary-position-embedding，训练得到的electra-small模型

# 二、 复现结果(dev dataset)
|Model|CoLA|SST|MRPC|STS|QQP|MNLI|QNLI|RTE|Avg.|
|---|---|---|---|---|---|---|---|---|---|
|ELECTRA-Small-OWT(original)|56.8|88.3|87.4|86.8|88.3|78.9|87.9|68.5|80.36|
|**ELECTRA-RoFormer-Small-OWT (this)**|55.76|90.45|87.3|86.64|89.61|81.17|88.85|62.71|80.31|

# 三、 训练细节
- 数据集 openwebtext
- 训练batch_size 256
- 学习率lr  5e-4
- 最大句子长度max_seqlen  128
- 训练total step  50W
- GPU RTX3090
- 训练时间总共耗费55h

# 四、wandb日志 
- [**预训练日志**](https://wandb.ai/junyu/electra_rotary_small_pretrain?workspace=user-junyu)
- [**GLUE微调日志**](https://wandb.ai/junyu/electra_rotary_glue_100?workspace=user-junyu)


# 五、 使用
```python
import torch
from transformers import ElectraTokenizer,RoFormerModel
tokenizer = ElectraTokenizer.from_pretrained("junnyu/roformer_small_discriminator")
model = RoFormerModel.from_pretrained("junnyu/roformer_small_discriminator")
inputs = tokenizer("Beijing is the capital of China.", return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)
    print(outputs[0].shape)
```