---
language: en
thumbnail: https://github.com/junnyu
tags:
- pytorch
- electra
- masked-lm
- rotary position embedding
widget:
- text: Paris is the [MASK] of France.
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
from transformers import ElectraTokenizer,RoFormerForMaskedLM

text = "Beijing is the capital of [MASK]."
tokenizer = ElectraTokenizer.from_pretrained("junnyu/roformer_small_generator")
pt_model = RoFormerForMaskedLM.from_pretrained(
    "junnyu/roformer_small_generator")
pt_inputs = tokenizer(text, return_tensors="pt")
with torch.no_grad():
    pt_outputs = pt_model(**pt_inputs).logits[0]
pt_outputs_sentence = "pytorch: "
for i, id in enumerate(tokenizer.encode(text)):
    if id == tokenizer.mask_token_id:
        tokens = tokenizer.convert_ids_to_tokens(pt_outputs[i].topk(k=5)[1])
        pt_outputs_sentence += "[" + "||".join(tokens) + "]"
    else:
        pt_outputs_sentence += "".join(
            tokenizer.convert_ids_to_tokens([id], skip_special_tokens=True))+" "
print(pt_outputs_sentence)
# pytorch:  beijing is the capital of [china||beijing||taiwan||india||shanghai].  
```