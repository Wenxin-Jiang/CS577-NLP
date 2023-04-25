---
language: zh
tags:
- roformer
- pytorch
- tf2.0
- paddlepaddle
widget:
- text: "今天[MASK]很好，我想去公园玩！"
---
## 介绍
Pretrained model on 13G Chinese corpus(clue corpus small). Masked language modeling(MLM) and sentence order prediction(SOP) are used as training task.
在13g的clue corpus small数据集上进行的预训练，使用了`Whole Mask LM` 和 `SOP` 任务

训练逻辑参考了这里。https://github.com/PaddlePaddle/PaddleNLP/tree/develop/examples/language_model/ernie-1.0

## 训练细节：
- paddlepaddle+paddlenlp
- V100 x 4
- batch size 256
- max_seq_len 512 
- max_lr 0.0001
- min_lr 0.00001
- weight_decay 0.01
- grad_clip 1.0
- 总共训练的句子```128*30w + 256*15w + 256*14.5w + 256*46.5w + 256*17w = 27648w```
- 约等于512 batch size, 100w步条件下的54%

最终loss：
```python
[2022-02-05 16:05:59,067] [    INFO] - global step 170100, loss: 2.651634932, lm_loss: 2.603405, sop_loss: 0.048229, speed: 1.06 steps/s, ips: 271.68 seqs/s, learning rate: 6.66465e-05, loss_scaling: 137438.96875, num_good_steps: 356, num_bad_steps: 0
[2022-02-05 16:07:28,227] [    INFO] - global step 170200, loss: 2.822231531, lm_loss: 2.662831, sop_loss: 0.159401, speed: 1.12 steps/s, ips: 287.13 seqs/s, learning rate: 6.66263e-05, loss_scaling: 137438.96875, num_good_steps: 59, num_bad_steps: 0
[2022-02-05 16:08:57,346] [    INFO] - global step 170300, loss: 2.710968971, lm_loss: 2.673646, sop_loss: 0.037323, speed: 1.12 steps/s, ips: 287.26 seqs/s, learning rate: 6.66061e-05, loss_scaling: 137438.96875, num_good_steps: 159, num_bad_steps: 0
[2022-02-05 16:10:26,698] [    INFO] - global step 170400, loss: 2.867662907, lm_loss: 2.619032, sop_loss: 0.248631, speed: 1.12 steps/s, ips: 286.51 seqs/s, learning rate: 6.65859e-05, loss_scaling: 137438.96875, num_good_steps: 259, num_bad_steps: 0
[2022-02-05 16:11:55,714] [    INFO] - global step 170500, loss: 3.158756495, lm_loss: 2.953678, sop_loss: 0.205079, speed: 1.12 steps/s, ips: 287.59 seqs/s, learning rate: 6.65657e-05, loss_scaling: 137438.96875, num_good_steps: 359, num_bad_steps: 0
[2022-02-05 16:13:24,869] [    INFO] - global step 170600, loss: 2.860815048, lm_loss: 2.754750, sop_loss: 0.106064, speed: 1.12 steps/s, ips: 287.14 seqs/s, learning rate: 6.65455e-05, loss_scaling: 137438.96875, num_good_steps: 33, num_bad_steps: 0
```
### tf版本 
https://github.com/ZhuiyiTechnology/roformer

### pytorch版本+tf2.0版本
https://github.com/JunnYu/RoFormer_pytorch

## pytorch使用
```python
import torch
from transformers import RoFormerForMaskedLM, BertTokenizer

text = "今天[MASK]很好，我[MASK]去公园玩。"
tokenizer = BertTokenizer.from_pretrained("junnyu/roformer_base_wwm_cluecorpussmall")
pt_model = RoFormerForMaskedLM.from_pretrained("junnyu/roformer_base_wwm_cluecorpussmall")
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
            tokenizer.convert_ids_to_tokens([id], skip_special_tokens=True))
print(pt_outputs_sentence)
# pytorch: 今天[天||人||气||阳||雨]很好，我[想||就||要||也||还]去公园玩。

```

## 引用

Bibtex：

```tex
@misc{su2021roformer,
      title={RoFormer: Enhanced Transformer with Rotary Position Embedding}, 
      author={Jianlin Su and Yu Lu and Shengfeng Pan and Bo Wen and Yunfeng Liu},
      year={2021},
      eprint={2104.09864},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```