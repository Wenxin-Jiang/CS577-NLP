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

# RWKV-3 169M

## Model Description

RWKV-3 169M is a L12-D768 causal language model trained on the Pile. See https://github.com/BlinkDL/RWKV-LM for details.

At this moment you have to use my Github code (https://github.com/BlinkDL/RWKV-v2-RNN-Pile) to run it.

ctx_len = 768
n_layer = 12
n_embd = 768

Final checkpoint:
RWKV-3-Pile-20220720-10704.pth : Trained on the Pile for 328B tokens.
* Pile loss 2.5596
* LAMBADA ppl 28.82, acc 32.33%
* PIQA acc 64.15%
* SC2016 acc 57.88%
* Hellaswag acc_norm 32.45%

Preview checkpoint:
20220703-1652.pth : Trained on the Pile for 50B tokens. Pile loss 2.6375, LAMBADA ppl 33.30, acc 31.24%.