---
language:
- en
tags:
- pytorch
- text-generation
- causal-lm
- rwkv
license: apache-2.0
datasets:
- The Pile

---

# RWKV-3 1.5B

## Model Description

RWKV-3 1.5B is a L24-D2048 causal language model trained on the Pile. See https://github.com/BlinkDL/RWKV-LM for details.

RWKV-4 1.5B is out: https://huggingface.co/BlinkDL/rwkv-4-pile-1b5

At this moment you have to use my Github code (https://github.com/BlinkDL/RWKV-v2-RNN-Pile) to run it.

ctx_len = 896
n_layer = 24
n_embd = 2048

Preview checkpoint: RWKV-3-Pile-20220723-3542.pth : Trained on the Pile for 127B tokens.
* Pile loss 2.102 
* LAMBADA ppl 7.52, acc 54.71%
* PIQA acc 71.11%
* SC2016 acc 67.24%
* Hellaswag acc_norm 50.45%

Preview checkpoint: 20220708-1905.pth : Trained on the Pile for 68B tokens.
* Pile loss 2.148
* LAMBADA ppl 8.41, acc 53.17%
* PIQA acc 69.64%
* SC2016 acc 67.08%
* Hellaswag acc_norm 48.20%

(I am still training it)