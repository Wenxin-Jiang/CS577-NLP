---
license: mit
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: mdeberta-v3-base-finetuned-pos
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mdeberta-v3-base-finetuned-pos

This model is a fine-tuned version of [microsoft/mdeberta-v3-base](https://huggingface.co/microsoft/mdeberta-v3-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0887
- Acc: 0.9814
- F1: 0.8861

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Acc    | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|
| No log        | 1.0   | 439  | 0.0965          | 0.9749 | 0.8471 |
| 0.3317        | 2.0   | 878  | 0.0815          | 0.9783 | 0.8702 |
| 0.0775        | 3.0   | 1317 | 0.0780          | 0.9812 | 0.8825 |
| 0.0568        | 4.0   | 1756 | 0.0769          | 0.9809 | 0.8827 |
| 0.0444        | 5.0   | 2195 | 0.0799          | 0.9811 | 0.8885 |
| 0.0339        | 6.0   | 2634 | 0.0834          | 0.9813 | 0.8821 |
| 0.0278        | 7.0   | 3073 | 0.0845          | 0.9817 | 0.8843 |
| 0.0222        | 8.0   | 3512 | 0.0866          | 0.9814 | 0.8863 |
| 0.0222        | 9.0   | 3951 | 0.0885          | 0.9814 | 0.8862 |
| 0.0188        | 10.0  | 4390 | 0.0887          | 0.9814 | 0.8861 |


### Framework versions

- Transformers 4.20.0
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
