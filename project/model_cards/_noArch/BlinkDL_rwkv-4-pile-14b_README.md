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

# RWKV-4 14B

## Model Description

RWKV-4 14B is a L40-D5120 causal language model trained on the Pile. See https://github.com/BlinkDL/RWKV-LM for details.

args.n_layer = 40
args.n_embd = 5120

Use https://github.com/BlinkDL/ChatRWKV to run it.

RWKV-4-Pile-14B-2023xxxx-ctx8192-testxxx.pth : Fine-tuned to ctx_len 8192.
* The best general model.

################################

"Raven": RWKV alpaca+vicuna-style model: https://huggingface.co/BlinkDL/rwkv-4-raven (highly recommended)

It is a strong chat model too. You can use +i for "Alpaca Instruct" in latest ChatRWKV v2. Examples:
```
+i Explain the following metaphor: "Life is like cats". 
+i write a python function to read data from an excel file.
```
################################

RWKV-4-Pile-14B-20230213-8019.pth : Trained on the Pile for 331B tokens
* Pile loss 1.7579 (ctx_len 1024)
* LAMBADA ppl 3.81, acc 71.05%
* PIQA acc 77.42%
* SC2016 acc 75.57%
* Hellaswag acc_norm 70.24%
* WinoGrande acc 62.98%
