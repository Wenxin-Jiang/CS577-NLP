---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: t5-small-finetuned-wikiSQL
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-wikiSQL

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1110
- Rouge2 Precision: 0.8308
- Rouge2 Recall: 0.7395
- Rouge2 Fmeasure: 0.7754

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge2 Precision | Rouge2 Recall | Rouge2 Fmeasure |
|:-------------:|:-----:|:-----:|:---------------:|:----------------:|:-------------:|:---------------:|
| 0.1975        | 1.0   | 4049  | 0.1602          | 0.7879           | 0.7007        | 0.7346          |
| 0.1643        | 2.0   | 8098  | 0.1371          | 0.8068           | 0.7163        | 0.7519          |
| 0.1501        | 3.0   | 12147 | 0.1280          | 0.8158           | 0.7246        | 0.7604          |
| 0.1403        | 4.0   | 16196 | 0.1216          | 0.8211           | 0.7304        | 0.7661          |
| 0.1317        | 5.0   | 20245 | 0.1176          | 0.8236           | 0.7323        | 0.7682          |
| 0.1267        | 6.0   | 24294 | 0.1150          | 0.8263           | 0.7343        | 0.7705          |
| 0.1271        | 7.0   | 28343 | 0.1133          | 0.8286           | 0.7371        | 0.7731          |
| 0.1199        | 8.0   | 32392 | 0.1121          | 0.8295           | 0.7384        | 0.7743          |
| 0.1167        | 9.0   | 36441 | 0.1111          | 0.8304           | 0.7391        | 0.775           |
| 0.1158        | 10.0  | 40490 | 0.1110          | 0.8308           | 0.7395        | 0.7754          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Tokenizers 0.13.1
