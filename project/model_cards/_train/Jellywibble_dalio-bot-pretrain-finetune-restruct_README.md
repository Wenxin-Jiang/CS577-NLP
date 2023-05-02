---
tags:
- text-generation
library_name: transformers
---

## Model description
Dalio Bot Pre-trained on Principles, fine-tuned on handwritten examples.

Pre-trained model: Jellywibble/dalio-pretrained-book-bs4-seed1 (based-off OPT30B)

Fine-tuning dataset: Jellywibble/dalio_handwritten-conversations

## Model Parameters
- 4xA40 (eff. batch size = 4)
- base_mode_name Jellywibble/dalio-pretrained-book-bs4-seed1
- dataset_name Jellywibble/dalio_handwritten-conversations
- block size 500
- per_device_train_batch_size 1
- gradient_accumulation steps 1
- learning_rate 2e-6
- seed 28
- validation split percentage 20
- hellaswag_sample_size 100

## Metrics
- Hellaswag Perplexity: 29.9
- Eval acc: 57.1%
- Eval loss: 1.971
- wandb: https://wandb.ai/jellywibble/huggingface/runs/12lgyt20?workspace=user-jellywibble
- Checkpoint 10 selected and uploaded