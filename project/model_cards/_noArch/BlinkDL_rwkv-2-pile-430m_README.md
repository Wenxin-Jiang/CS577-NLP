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

# RWKV-2 430M

## Model Description

RWKV-2 430M is a L24-D1024 causal language model trained on the Pile. See https://github.com/BlinkDL/RWKV-LM for details.

At this moment you have to use my Github code (https://github.com/BlinkDL/RWKV-v2-RNN-Pile) to run it.

ctx_len = 768 n_layer = 24 n_embd = 1024

Final checkpoint: 20220615-10803.pth : Trained on the Pile for 331B tokens.
* Pile loss 2.349
* LAMBADA ppl 15.34, acc 42.42%
* PIQA acc 67.03%
* SC2016 acc 62.05%
* Hellaswag acc_norm 38.47%