---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: distilbart-cnn-12-6-samsum-ts-POC
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbart-cnn-12-6-samsum-ts-POC

This model is a fine-tuned version of [philschmid/distilbart-cnn-12-6-samsum](https://huggingface.co/philschmid/distilbart-cnn-12-6-samsum) on an unknown dataset.

## Model description

DistilBart-Cnn-Samsum fine-tuned on custom dataset.

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 10

### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
