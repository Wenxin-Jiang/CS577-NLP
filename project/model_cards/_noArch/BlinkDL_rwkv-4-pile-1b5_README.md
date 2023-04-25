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

# RWKV-4 1.5B

# Use RWKV-4 models (NOT RWKV-4a, NOT RWKV-4b) unless you know what you are doing.
# Use RWKV-4 models (NOT RWKV-4a, NOT RWKV-4b) unless you know what you are doing.
# Use RWKV-4 models (NOT RWKV-4a, NOT RWKV-4b) unless you know what you are doing.

## Model Description

RWKV-4 1.5B is a L24-D2048 causal language model trained on the Pile. See https://github.com/BlinkDL/RWKV-LM for details.

Use https://github.com/BlinkDL/ChatRWKV to run it.

ctx_len = 1024
n_layer = 24
n_embd = 2048

RWKV-4-Pile-1B5-20220929-ctx4096.pth : Fine-tuned to ctx_len 4096.
* Likely better when ctxlen > 100. Please test.

RWKV-4-Pile-1B5-20220903-8040.pth : Trained on the Pile for 332B tokens.
* Pile loss 2.0415
* LAMBADA ppl 7.04, acc 56.43%
* PIQA acc 72.36%
* SC2016 acc 68.73%
* Hellaswag acc_norm 52.48%

### Instruct-test models: only useful if you construct your prompt following dataset templates

Note I am using "Q: instruct\n\nA: result" prompt for all instructs.

RWKV-4-Pile-1B5-Instruct-test1-20230124.pth
instruct-tuned on https://huggingface.co/datasets/bigscience/xP3all/viewer/en/train

RWKV-4-Pile-1B5-Instruct-test2-20230209.pth
instruct-tuned on https://huggingface.co/datasets/Muennighoff/flan & NIv2

### Chinese models

RWKV-4-Pile-1B5-EngChn-testNovel-xxx for writing Chinese novels (trained on 200G Chinese novels.)

RWKV-4-Pile-1B5-EngChn-testxxx for Chinese Q&A (trained on 10G Chinese text. only for testing purposes.)

## Note: 4 / 4a / 4b models ARE NOT compatible. Use RWKV-4 unless you know what you are doing.

RWKV-4b-Pile-1B5-20230217-7954.pth (--my_testing 'a') with tiny amt of QKV attention to improve performance
* Pile loss 1.9947
* LAMBADA ppl 5.82, acc 62.35%
* PIQA acc 72.52%
* SC2016 acc 68.89%
* Hellaswag acc_norm 54.32%
