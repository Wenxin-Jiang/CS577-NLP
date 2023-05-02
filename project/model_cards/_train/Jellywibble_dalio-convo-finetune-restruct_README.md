---
tags:
- text-generation
library_name: transformers
---

## Model description
Based on Jellywibble/dalio-pretrained-book-bs4-seed1 which was pre-trained on the Dalio Principles Book
Finetuned on handwritten conversations Jellywibble/dalio_handwritten-conversations

## Dataset Used
Jellywibble/dalio_handwritten-conversations

## Training Parameters
- Deepspeed on 4xA40 GPUs
- Ensuring EOS token `<s>` appears only at the beginning of each 'This is a conversation where Ray ...'
- Gradient Accumulation steps = 1 (Effective batch size of 4)
- 2e-6 Learning Rate, AdamW optimizer
- Block size of 1000
- Trained for 1 Epoch (additional epochs yielded worse Hellaswag result)

## Metrics
- Hellaswag Perplexity: 29.83
- Eval accuracy: 58.1%
- Eval loss: 1.883
- Checkpoint 9 uploaded
- Wandb run: https://wandb.ai/jellywibble/huggingface/runs/157eehn9?workspace=user-jellywibble