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

# RWKV-4 169M

# Use RWKV-4 models (NOT RWKV-4a, NOT RWKV-4b) unless you know what you are doing.
# Use RWKV-4 models (NOT RWKV-4a, NOT RWKV-4b) unless you know what you are doing.
# Use RWKV-4 models (NOT RWKV-4a, NOT RWKV-4b) unless you know what you are doing.

## Model Description

RWKV-4 169M is a L12-D768 causal language model trained on the Pile. See https://github.com/BlinkDL/RWKV-LM for details.

Use https://github.com/BlinkDL/ChatRWKV to run it.

ctx_len = 1024
n_layer = 12
n_embd = 768

Final checkpoint:
RWKV-4-Pile-169M-20220807-8023.pth : Trained on the Pile for 332B tokens.
* Pile loss 2.5355
* LAMBADA ppl 29.33, acc 32.99%
* PIQA acc 65.07%
* SC2016 acc 58.79%
* Hellaswag acc_norm 32.26%

With tiny attention (--tiny_att_dim 256 --tiny_att_layer 9):
RWKV-4a-Pile-170M-20221209-7955.pth
* Pile loss 2.4702
* LAMBADA ppl 21.42, acc 38.23%
* PIQA acc 63.76%
* SC2016 acc 59.06%
* Hellaswag acc_norm 32.40%

RWKV-4b-Pile-171M-20230202-7922.pth (--my_testing 'a')
* Pile loss 2.4222
* LAMBADA ppl 22.02, acc 38.56%
* PIQA acc 64.04%
* SC2016 acc 59.91%
* Hellaswag acc_norm 33.33%
