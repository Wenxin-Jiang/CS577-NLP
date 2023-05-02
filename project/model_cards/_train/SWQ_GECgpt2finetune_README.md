---
license: mit
tags:
- generated_from_trainer
model-index:
- name: gptfinetune2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gptfinetune2

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.1463

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 8e-06
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 482  | 3.1945          |
| 3.4235        | 2.0   | 964  | 3.1655          |
| 3.2473        | 3.0   | 1446 | 3.1560          |
| 3.1981        | 4.0   | 1928 | 3.1508          |
| 3.1767        | 5.0   | 2410 | 3.1477          |
| 3.1502        | 6.0   | 2892 | 3.1467          |
| 3.1387        | 7.0   | 3374 | 3.1464          |
| 3.1275        | 8.0   | 3856 | 3.1463          |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.0
- Tokenizers 0.13.2
