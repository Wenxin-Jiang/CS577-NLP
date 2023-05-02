---
tags:
- generated_from_trainer
model-index:
- name: kobigbird-bert-base-finetuned-klue-goorm-q-a-task
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# kobigbird-bert-base-finetuned-klue-goorm-q-a-task

This model is a fine-tuned version of [ToToKr/kobigbird-bert-base-finetuned-klue](https://huggingface.co/ToToKr/kobigbird-bert-base-finetuned-klue) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2115

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.6159        | 0.09  | 500  | 1.7522          |
| 1.554         | 0.17  | 1000 | 1.5953          |
| 1.4493        | 0.26  | 1500 | 1.3769          |
| 1.4051        | 0.35  | 2000 | 1.3746          |
| 1.3251        | 0.43  | 2500 | 1.5049          |
| 1.2855        | 0.52  | 3000 | 1.1733          |
| 1.2226        | 0.6   | 3500 | 1.1538          |
| 1.1907        | 0.69  | 4000 | 1.1470          |
| 1.1655        | 0.78  | 4500 | 1.0759          |
| 1.1411        | 0.86  | 5000 | 1.0676          |
| 1.0752        | 0.95  | 5500 | 0.9894          |
| 0.9389        | 1.04  | 6000 | 1.2020          |
| 0.8457        | 1.12  | 6500 | 1.1004          |
| 0.7977        | 1.21  | 7000 | 1.1397          |
| 0.818         | 1.29  | 7500 | 1.2960          |
| 0.8142        | 1.38  | 8000 | 1.2115          |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1
