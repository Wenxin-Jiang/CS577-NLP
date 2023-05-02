---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: twitter_RoBERTa_token_itr0_1e-05_essays_01_03_2022-14_40_24
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter_RoBERTa_token_itr0_1e-05_essays_01_03_2022-14_40_24

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3067
- Precision: 0.2871
- Recall: 0.4433
- F1: 0.3485
- Accuracy: 0.8906

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 11   | 0.4768          | 0.0       | 0.0    | 0.0    | 0.7546   |
| No log        | 2.0   | 22   | 0.3665          | 0.1610    | 0.3211 | 0.2145 | 0.8487   |
| No log        | 3.0   | 33   | 0.3010          | 0.1994    | 0.3690 | 0.2589 | 0.8868   |
| No log        | 4.0   | 44   | 0.2748          | 0.2839    | 0.4479 | 0.3475 | 0.9037   |
| No log        | 5.0   | 55   | 0.2670          | 0.3104    | 0.4704 | 0.3740 | 0.9083   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
