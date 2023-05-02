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
- name: finetuned_token_3e-05_all_16_02_2022-16_09_36
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_token_3e-05_all_16_02_2022-16_09_36

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1630
- Precision: 0.3684
- Recall: 0.3714
- F1: 0.3699
- Accuracy: 0.9482

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 38   | 0.3339          | 0.1075    | 0.2324 | 0.1470 | 0.8379   |
| No log        | 2.0   | 76   | 0.3074          | 0.1589    | 0.2926 | 0.2060 | 0.8489   |
| No log        | 3.0   | 114  | 0.2914          | 0.2142    | 0.3278 | 0.2591 | 0.8591   |
| No log        | 4.0   | 152  | 0.2983          | 0.1951    | 0.3595 | 0.2529 | 0.8454   |
| No log        | 5.0   | 190  | 0.2997          | 0.1851    | 0.3528 | 0.2428 | 0.8487   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
