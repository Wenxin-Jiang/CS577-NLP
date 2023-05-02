---
tags:
- generated_from_trainer
model-index:
- name: kobigbird-bert-base-finetuned-klue
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# kobigbird-bert-base-finetuned-klue

This model is a fine-tuned version of [monologg/kobigbird-bert-base](https://huggingface.co/monologg/kobigbird-bert-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8347

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 5.3957        | 0.13  | 500   | 3.7603          |
| 3.2242        | 0.26  | 1000  | 2.3961          |
| 2.0812        | 0.4   | 1500  | 1.5552          |
| 1.6198        | 0.53  | 2000  | 1.3609          |
| 1.447         | 0.66  | 2500  | 1.2270          |
| 1.3438        | 0.79  | 3000  | 1.1321          |
| 1.2399        | 0.93  | 3500  | 1.0973          |
| 1.1976        | 1.06  | 4000  | 1.0418          |
| 1.1177        | 1.19  | 4500  | 1.0301          |
| 1.0811        | 1.32  | 5000  | 1.0232          |
| 1.0506        | 1.45  | 5500  | 0.9971          |
| 1.0293        | 1.59  | 6000  | 0.9580          |
| 1.0196        | 1.72  | 6500  | 0.9551          |
| 0.9846        | 1.85  | 7000  | 0.9274          |
| 0.9702        | 1.98  | 7500  | 0.9286          |
| 0.9224        | 2.11  | 8000  | 0.8961          |
| 0.8867        | 2.25  | 8500  | 0.9193          |
| 0.8711        | 2.38  | 9000  | 0.8727          |
| 0.883         | 2.51  | 9500  | 0.8790          |
| 0.8513        | 2.64  | 10000 | 0.8830          |
| 0.8709        | 2.78  | 10500 | 0.8604          |
| 0.8766        | 2.91  | 11000 | 0.8260          |
| 0.7976        | 3.04  | 11500 | 0.8401          |
| 0.7724        | 3.17  | 12000 | 0.8617          |
| 0.78          | 3.3   | 12500 | 0.8601          |
| 0.7566        | 3.44  | 13000 | 0.8657          |
| 0.7407        | 3.57  | 13500 | 0.8347          |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
