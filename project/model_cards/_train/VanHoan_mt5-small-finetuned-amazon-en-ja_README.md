---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-small-finetuned-amazon-en-ja
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-small-finetuned-amazon-en-ja

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.2749
- Rouge1: 16.6603
- Rouge2: 8.1096
- Rougel: 16.0117
- Rougelsum: 16.1001

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|
| 8.0415        | 1.0   | 773  | 3.6621          | 11.6952 | 4.8642 | 11.3154 | 11.3683   |
| 4.1249        | 2.0   | 1546 | 3.3933          | 14.3113 | 6.2067 | 13.9923 | 14.0476   |
| 3.7462        | 3.0   | 2319 | 3.3725          | 15.7855 | 8.0892 | 15.2485 | 15.3145   |
| 3.5608        | 4.0   | 3092 | 3.3270          | 16.0732 | 7.8202 | 15.4816 | 15.6421   |
| 3.4471        | 5.0   | 3865 | 3.2908          | 16.4399 | 7.6723 | 15.514  | 15.7309   |
| 3.3604        | 6.0   | 4638 | 3.2904          | 16.6074 | 8.3131 | 16.0711 | 16.1382   |
| 3.3081        | 7.0   | 5411 | 3.2827          | 16.2547 | 8.1096 | 15.6128 | 15.7097   |
| 3.2905        | 8.0   | 6184 | 3.2749          | 16.6603 | 8.1096 | 16.0117 | 16.1001   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
