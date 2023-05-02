---
tags:
- generated_from_trainer
model-index:
- name: kobigbird-bert-base-finetuned-klue-v2_epoch64
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# kobigbird-bert-base-finetuned-klue-v2_epoch64

This model is a fine-tuned version of [monologg/kobigbird-bert-base](https://huggingface.co/monologg/kobigbird-bert-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8139

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.5026        | 0.55  | 500  | 1.3754          |
| 0.9551        | 1.1   | 1000 | 0.9633          |
| 0.8           | 1.64  | 1500 | 0.8191          |
| 0.6182        | 2.19  | 2000 | 0.7808          |
| 0.5731        | 2.74  | 2500 | 0.7482          |
| 0.3699        | 3.29  | 3000 | 0.8175          |
| 0.3634        | 3.84  | 3500 | 0.8139          |


### Framework versions

- Transformers 4.23.0
- Pytorch 1.12.1+cu113
- Datasets 2.5.2
- Tokenizers 0.13.1
