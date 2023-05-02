---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-small-science-papers-NIPS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-science-papers-NIPS

This model is a fine-tuned version of [Dagar/t5-small-science-papers](https://huggingface.co/Dagar/t5-small-science-papers) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.7566
- Rouge1: 15.7066
- Rouge2: 2.5654
- Rougel: 11.4679
- Rougelsum: 14.4017
- Gen Len: 19.0

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
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 318  | 5.1856          | 13.7172 | 2.0644 | 10.2189 | 12.838    | 19.0    |
| 5.4522        | 2.0   | 636  | 5.0383          | 15.6211 | 2.1808 | 11.3561 | 14.3054   | 19.0    |
| 5.4522        | 3.0   | 954  | 4.9486          | 15.1659 | 2.3308 | 11.1052 | 13.9456   | 19.0    |
| 5.1254        | 4.0   | 1272 | 4.8851          | 15.716  | 2.4099 | 11.4954 | 14.5099   | 19.0    |
| 4.9794        | 5.0   | 1590 | 4.8456          | 15.5507 | 2.4267 | 11.3867 | 14.3237   | 19.0    |
| 4.9794        | 6.0   | 1908 | 4.8073          | 15.8406 | 2.4254 | 11.6878 | 14.6154   | 19.0    |
| 4.8823        | 7.0   | 2226 | 4.7872          | 15.5554 | 2.4637 | 11.3401 | 14.3183   | 19.0    |
| 4.8338        | 8.0   | 2544 | 4.7680          | 15.4783 | 2.4888 | 11.3364 | 14.2031   | 19.0    |
| 4.8338        | 9.0   | 2862 | 4.7621          | 15.958  | 2.5662 | 11.6139 | 14.6576   | 19.0    |
| 4.7838        | 10.0  | 3180 | 4.7566          | 15.7066 | 2.5654 | 11.4679 | 14.4017   | 19.0    |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
