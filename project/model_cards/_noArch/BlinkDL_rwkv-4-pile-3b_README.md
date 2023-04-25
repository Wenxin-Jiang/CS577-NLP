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

# RWKV-4 3B

# Use RWKV-4 models (NOT RWKV-4a, NOT RWKV-4b) unless you know what you are doing.
# Use RWKV-4 models (NOT RWKV-4a, NOT RWKV-4b) unless you know what you are doing.
# Use RWKV-4 models (NOT RWKV-4a, NOT RWKV-4b) unless you know what you are doing.

## Model Description

RWKV-4 3B is a L32-D2560 causal language model trained on the Pile. See https://github.com/BlinkDL/RWKV-LM for details.

Use https://github.com/BlinkDL/ChatRWKV to run it.

RWKV-4-Pile-3B-20221110-ctx4096.pth (RECOMMENDED) : Fine-tuned to ctx_len 4096.
* LAMBADA ppl 5.25, acc 63.96%
* PIQA acc 74.16%
* SC2016 acc 70.71%
* Hellaswag acc_norm 59.89%
* ctx_len = 4096 n_layer = 32 n_embd = 2560

RWKV-4-Pile-3B-20221008-8023.pth : Trained on the Pile for 331B tokens.
* Pile loss 1.9469
* LAMBADA ppl 5.24, acc 63.94%
* PIQA acc 73.72%
* SC2016 acc 70.28%
* Hellaswag acc_norm 59.63%
* ctx_len = 1024 n_layer = 32 n_embd = 2560

### Instruct-test models: only useful if you construct your prompt following dataset templates

Note I am using "Q: instruct\n\nA: result" prompt for all instructs.

RWKV-4-Pile-3B-Instruct-test1
instruct-tuned on https://huggingface.co/datasets/bigscience/xP3all/viewer/en/train

RWKV-4-Pile-3B-Instruct-test2
instruct-tuned on https://huggingface.co/datasets/Muennighoff/flan & NIv2

### Chinese models

RWKV-4-Pile-3B-EngChn-testNovel-xxx for writing Chinese novels (trained on 200G Chinese novels.)

RWKV-4-Pile-3B-EngChn-testxxx for Chinese Q&A (trained on 10G Chinese text. only for testing purposes.)

## Note: 4 / 4a / 4b models ARE NOT compatible. Use RWKV-4 unless you know what you are doing.
