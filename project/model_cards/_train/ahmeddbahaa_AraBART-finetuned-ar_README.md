---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
datasets:
- xlsum
model-index:
- name: AraBART-finetune-ar-xlsum
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# AraBART-finetuned-ar

This model is a fine-tuned version of [moussaKam/AraBART](https://huggingface.co/moussaKam/AraBART) on the xlsum dataset.
It achieves the following results on the evaluation set:
- Loss: 3.7449
- Rouge-1: 31.08
- Rouge-2: 14.68
- Rouge-l: 27.36
- Gen Len: 19.64
- Bertscore: 73.86

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
- lr_scheduler_warmup_steps: 250
- num_epochs: 10
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge-1 | Rouge-2 | Rouge-l | Gen Len | Bertscore |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:-------:|:---------:|
| 4.4318        | 1.0   | 2345  | 3.7996          | 28.93   | 13.2    | 25.56   | 19.51   | 73.17     |
| 4.0338        | 2.0   | 4690  | 3.7483          | 30.29   | 14.24   | 26.73   | 19.5    | 73.59     |
| 3.8586        | 3.0   | 7035  | 3.7281          | 30.44   | 14.44   | 26.92   | 19.75   | 73.58     |
| 3.7289        | 4.0   | 9380  | 3.7204          | 30.55   | 14.49   | 26.88   | 19.66   | 73.73     |
| 3.6245        | 5.0   | 11725 | 3.7199          | 30.73   | 14.63   | 27.11   | 19.69   | 73.68     |
| 3.5392        | 6.0   | 14070 | 3.7221          | 30.85   | 14.65   | 27.21   | 19.7    | 73.77     |
| 3.4694        | 7.0   | 16415 | 3.7286          | 31.08   | 14.8    | 27.41   | 19.62   | 73.84     |
| 3.4126        | 8.0   | 18760 | 3.7384          | 31.06   | 14.77   | 27.41   | 19.64   | 73.82     |
| 3.3718        | 9.0   | 21105 | 3.7398          | 31.18   | 14.89   | 27.49   | 19.67   | 73.87     |
| 3.3428        | 10.0  | 23450 | 3.7449          | 31.19   | 14.88   | 27.44   | 19.68   | 73.87     |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1
