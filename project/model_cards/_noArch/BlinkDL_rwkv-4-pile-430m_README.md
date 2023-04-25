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
- the_pile

---

# RWKV-4 430M

# Use RWKV-4 models (NOT RWKV-4a, NOT RWKV-4b) unless you know what you are doing.
# Use RWKV-4 models (NOT RWKV-4a, NOT RWKV-4b) unless you know what you are doing.
# Use RWKV-4 models (NOT RWKV-4a, NOT RWKV-4b) unless you know what you are doing.

## Model Description

RWKV-4 430M is a L24-D1024 causal language model trained on the Pile. See https://github.com/BlinkDL/RWKV-LM for details.

Use https://github.com/BlinkDL/ChatRWKV to run it.

ctx_len = 1024
n_layer = 24
n_embd = 1024

Final checkpoint:
RWKV-4-Pile-430M-20220808-8066.pth : Trained on the Pile for 333B tokens.
* Pile loss 2.2621
* LAMBADA ppl 13.04, acc 45.16%
* PIQA acc 67.52%
* SC2016 acc 63.87%
* Hellaswag acc_norm 40.90%

With tiny attention (--tiny_att_dim 512 --tiny_att_layer 18):
RWKV-4a-Pile-433M-20221223-8039.pth
* Pile loss 2.2394
* LAMBADA ppl 10.54, acc 50.20%
* PIQA acc 68.12%
* SC2016 acc 63.55%
* Hellaswag acc_norm 40.82%

RWKV-4b-Pile-436M-20230211-8012.pth (--my_testing 'a')
* Pile loss 2.2026
* LAMBADA ppl 10.48, acc 51.35%
* PIQA acc 68.06%
* SC2016 acc 63.17%
* Hellaswag acc_norm 42.09%
