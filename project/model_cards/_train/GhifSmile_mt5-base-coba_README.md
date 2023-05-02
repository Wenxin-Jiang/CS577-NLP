---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mt5-base-coba
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-base-coba

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5870
- Rouge1: 0.4338
- Rouge2: 0.2876
- Rougel: 0.3743
- Rougelsum: 0.409

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-06
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:---------:|
| 7.0922        | 1.0   | 7452  | 0.6538          | 0.3566 | 0.239  | 0.3218 | 0.3348    |
| 0.9442        | 2.0   | 14904 | 0.6900          | 0.427  | 0.2868 | 0.3711 | 0.402     |
| 3.0789        | 3.0   | 22356 | 0.6775          | 0.3808 | 0.2584 | 0.3398 | 0.3567    |
| 1.0565        | 4.0   | 29808 | 0.5928          | 0.4348 | 0.2882 | 0.3756 | 0.4096    |
| 0.7872        | 5.0   | 37260 | 0.5870          | 0.4338 | 0.2876 | 0.3743 | 0.409     |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.9.1
- Datasets 2.7.1
- Tokenizers 0.13.2
