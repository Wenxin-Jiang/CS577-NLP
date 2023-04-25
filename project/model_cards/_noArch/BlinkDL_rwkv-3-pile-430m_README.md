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

# RWKV-3 430M

## Model Description

RWKV-3 430M is a L24-D1024 causal language model trained on the Pile. See https://github.com/BlinkDL/RWKV-LM for details.

At this moment you have to use my Github code (https://github.com/BlinkDL/RWKV-v2-RNN-Pile) to run it.

ctx_len = 768
n_layer = 24
n_embd = 1024

Final checkpoint: RWKV-3-Pile-430M-20220817-10602.pth : Trained on the Pile for 326B tokens.
* Pile loss 2.288
* LAMBADA ppl 12.83, acc 45.45%
* PIQA acc 68.50%
* SC2016 acc 63.60%
* Hellaswag acc_norm 40.68%

Preview checkpoint: RWKV-3-Pile-20220721-3029.pth : Trained on the Pile for 93B tokens.
* Pile loss 2.341
* LAMBADA ppl 14.18, acc 44.25%
* PIQA acc 67.95%
* SC2016 acc 63.39%
* Hellaswag acc_norm 39.06%
