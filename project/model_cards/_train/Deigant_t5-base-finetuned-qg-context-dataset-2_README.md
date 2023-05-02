---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-base-finetuned-qg-context-dataset-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-finetuned-qg-context-dataset-2

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5958
- Rouge1: 37.1698
- Rouge2: 15.8177
- Rougel: 33.3329
- Rougelsum: 33.0872

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 16
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| No log        | 1.0   | 73   | 1.8700          | 30.0504 | 9.8379  | 24.0514 | 24.1584   |
| No log        | 2.0   | 146  | 1.6264          | 34.715  | 12.71   | 27.825  | 27.7697   |
| No log        | 3.0   | 219  | 1.5904          | 33.9221 | 10.688  | 29.5483 | 29.5388   |
| No log        | 4.0   | 292  | 1.5623          | 36.5544 | 14.8003 | 31.6295 | 31.4603   |
| No log        | 5.0   | 365  | 1.5463          | 34.071  | 13.189  | 30.1517 | 30.3325   |
| No log        | 6.0   | 438  | 1.5539          | 37.7324 | 15.5312 | 33.3968 | 33.2518   |
| 1.5099        | 7.0   | 511  | 1.5643          | 32.5168 | 11.2479 | 27.4951 | 27.4425   |
| 1.5099        | 8.0   | 584  | 1.5653          | 39.5646 | 17.9528 | 35.4095 | 35.2042   |
| 1.5099        | 9.0   | 657  | 1.5679          | 39.333  | 17.0059 | 34.9131 | 34.7696   |
| 1.5099        | 10.0  | 730  | 1.5757          | 37.5046 | 16.2468 | 32.5031 | 32.4012   |
| 1.5099        | 11.0  | 803  | 1.5738          | 37.601  | 16.4592 | 33.5804 | 33.1352   |
| 1.5099        | 12.0  | 876  | 1.5894          | 42.1889 | 19.3169 | 37.8273 | 37.7312   |
| 1.5099        | 13.0  | 949  | 1.5929          | 38.5814 | 17.0896 | 34.4696 | 34.3629   |
| 1.015         | 14.0  | 1022 | 1.5922          | 36.6392 | 16.8083 | 32.6318 | 32.4199   |
| 1.015         | 15.0  | 1095 | 1.5948          | 34.6707 | 15.7198 | 30.319  | 30.3403   |
| 1.015         | 16.0  | 1168 | 1.5958          | 37.1698 | 15.8177 | 33.3329 | 33.0872   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2