---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- squad_modified_for_t5_qg
model-index:
- name: t5-end2end-questions-generation
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-end2end-questions-generation

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on the squad_modified_for_t5_qg dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8015

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.609         | 0.34  | 100  | 1.9542          |
| 2.0336        | 0.68  | 200  | 1.8015          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
