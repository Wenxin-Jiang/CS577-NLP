---
tags:
- generated_from_trainer
model-index:
- name: gpt2-xl-ft-d4-0.15-n-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-xl-ft-d4-0.15-n-3

This model is a fine-tuned version of [gpt2-xl](https://huggingface.co/gpt2-xl) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4877

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 4
- eval_batch_size: 4
- seed: 2022
- gradient_accumulation_steps: 32
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100.0
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 156  | 1.3294          |
| No log        | 2.0   | 312  | 1.3466          |
| No log        | 3.0   | 468  | 1.4295          |
| 1.1304        | 4.0   | 624  | 1.4877          |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
