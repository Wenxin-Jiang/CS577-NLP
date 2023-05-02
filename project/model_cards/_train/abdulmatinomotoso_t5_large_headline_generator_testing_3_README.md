---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: t5_large_headline_generator_testing_3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5_large_headline_generator_testing_3

This model is a fine-tuned version of [t5-large](https://huggingface.co/t5-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8407

## Model description

More information needed

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.9638        | 0.79  | 500  | 0.8474          |
| 0.8478        | 1.57  | 1000 | 0.8356          |
| 0.6981        | 2.36  | 1500 | 0.8407          |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
