---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: roberta-base-bne-finetuned-detests-02-11-2022
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-bne-finetuned-detests-02-11-2022

This model is a fine-tuned version of [BSC-TeMU/roberta-base-bne](https://huggingface.co/BSC-TeMU/roberta-base-bne) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8124
- F1: 0.6381

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.379         | 0.64  | 25   | 0.4136          | 0.0    |
| 0.315         | 1.28  | 50   | 0.3663          | 0.6343 |
| 0.3228        | 1.92  | 75   | 0.3424          | 0.6386 |
| 0.1657        | 2.56  | 100  | 0.5133          | 0.5385 |
| 0.108         | 3.21  | 125  | 0.4766          | 0.6452 |
| 0.0631        | 3.85  | 150  | 0.6063          | 0.6083 |
| 0.0083        | 4.49  | 175  | 0.6200          | 0.6198 |
| 0.0032        | 5.13  | 200  | 0.6508          | 0.6335 |
| 0.0047        | 5.77  | 225  | 0.6877          | 0.6269 |
| 0.0018        | 6.41  | 250  | 0.7745          | 0.6148 |
| 0.0014        | 7.05  | 275  | 0.7741          | 0.6299 |
| 0.001         | 7.69  | 300  | 0.7896          | 0.6381 |
| 0.0011        | 8.33  | 325  | 0.8008          | 0.6381 |
| 0.0008        | 8.97  | 350  | 0.8086          | 0.6381 |
| 0.0009        | 9.62  | 375  | 0.8124          | 0.6381 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
