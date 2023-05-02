---
tags:
- text-generation
library_name: transformers
---

## Model description
Based off facebook/opt-30b model, finetuned on chucked Dalio responses

## Dataset Used
Jellywibble/dalio-pretrain-book-dataset-v2

## Training Parameters
- Deepspeed on 4xA40 GPUs
- Ensuring EOS token `<s>` appears only at the beginning of each chunk
- Gradient Accumulation steps = 1 (Effective batch size of 4)
- 3e-6 Learning Rate, AdamW optimizer
- Block size of 800
- Trained for 1 Epoch (additional epochs yielded worse Hellaswag result)

## Metrics
- Hellaswag Perplexity: 30.2
- Eval accuracy: 49.8%
- Eval loss: 2.283
- Checkpoint 16 uploaded
- wandb run: https://wandb.ai/jellywibble/huggingface/runs/2vtr39rk?workspace=user-jellywibble