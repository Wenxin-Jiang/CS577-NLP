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
- name: finetuned_token_itr0_0.0002_all_16_02_2022-20_30_01
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_itr0_0.0002_all_16_02_2022-20_30_01

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1577
- Precision: 0.4469
- Recall: 0.5280
- F1: 0.4841
- Accuracy: 0.9513

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 38   | 0.3553          | 0.1068    | 0.0810 | 0.0922 | 0.8412   |
| No log        | 2.0   | 76   | 0.2812          | 0.2790    | 0.4017 | 0.3293 | 0.8684   |
| No log        | 3.0   | 114  | 0.2793          | 0.3086    | 0.4586 | 0.3689 | 0.8747   |
| No log        | 4.0   | 152  | 0.2766          | 0.3057    | 0.4190 | 0.3535 | 0.8763   |
| No log        | 5.0   | 190  | 0.2805          | 0.2699    | 0.4845 | 0.3467 | 0.8793   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
