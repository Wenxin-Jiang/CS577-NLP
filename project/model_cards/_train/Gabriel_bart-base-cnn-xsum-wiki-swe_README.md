---
license: mit
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bart-base-cnn-xsum-wiki-swe
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-base-cnn-xsum-wiki-swe

This model is a fine-tuned version of [Gabriel/bart-base-cnn-xsum-swe](https://huggingface.co/Gabriel/bart-base-cnn-xsum-swe) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3884
- Rouge1: 26.8917
- Rouge2: 11.8254
- Rougel: 22.6089
- Rougelsum: 26.1492
- Gen Len: 19.3468

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
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 9
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 2.4993        | 1.0   | 2985  | 2.3834          | 25.8959 | 10.9373 | 21.8329 | 25.2002   | 19.1416 |
| 2.2397        | 2.0   | 5970  | 2.2939          | 26.1166 | 11.4087 | 22.2444 | 25.4752   | 19.2351 |
| 2.0318        | 3.0   | 8955  | 2.2687          | 26.5222 | 11.6512 | 22.567  | 25.851    | 19.2384 |
| 1.879         | 4.0   | 11940 | 2.2750          | 26.7637 | 11.7676 | 22.6674 | 26.0753   | 19.2622 |
| 1.7532        | 5.0   | 14925 | 2.2923          | 26.8104 | 11.8724 | 22.6794 | 26.0907   | 19.3063 |
| 1.6315        | 6.0   | 17910 | 2.3190          | 26.7758 | 11.7989 | 22.5925 | 26.032    | 19.3136 |
| 1.5409        | 7.0   | 20895 | 2.3517          | 26.8762 | 11.8552 | 22.6694 | 26.1329   | 19.3275 |
| 1.4711        | 8.0   | 23880 | 2.3679          | 26.899  | 11.9185 | 22.6764 | 26.1574   | 19.2994 |
| 1.4105        | 9.0   | 26865 | 2.3884          | 26.8917 | 11.8254 | 22.6089 | 26.1492   | 19.3468 |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1
