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

# RWKV-4 7B

## Model Description

RWKV-4 7B is a L32-D4096 causal language model trained on the Pile. See https://github.com/BlinkDL/RWKV-LM for details.

Use https://github.com/BlinkDL/ChatRWKV to run it.

ctx_len = 1024
n_layer = 32
n_embd = 4096

RWKV-4-Pile-7B-20230109-ctx4096.pth : Fine-tuned to ctx_len 4096.
* Likely the best. Please test.

################################

"Raven": RWKV alpaca+vicuna-style model: https://huggingface.co/BlinkDL/rwkv-4-raven (highly recommended)

It is a strong chat model too. You can use +i for "Alpaca Instruct" in latest ChatRWKV v2. Examples:
```
+i Explain the following metaphor: "Life is like cats". 
+i write a python function to read data from an excel file.
```
################################

RWKV-4-Pile-7B-20230xxx-ctx8192-testxxx : Fine-tuned to ctx_len 8192.
* Slightly weaker than ctx4096 model when ctxlen < 3k.

RWKV-4-Pile-7B-20221115-8047.pth : Trained on the Pile for 332B tokens.
* Pile loss 1.8415T
* LAMBADA ppl 4.38, acc 67.18%
* PIQA acc 76.06%
* SC2016 acc 73.44%
* Hellaswag acc_norm 65.51%

### Instruct-test models (OLD): only useful if you construct your prompt following dataset templates

Note I am using "Q: instruct\n\nA: result" prompt for all instructs.

RWKV-4-Pile-7B-Instruct-test1
instruct-tuned on https://huggingface.co/datasets/bigscience/xP3all/viewer/en/train

RWKV-4-Pile-7B-Instruct-test2
instruct-tuned on https://huggingface.co/datasets/Muennighoff/flan & NIv2

### Chinese models

RWKV-4-Pile-7B-EngChn-testNovel-xxx for writing Chinese novels (trained on 200G Chinese novels.)
