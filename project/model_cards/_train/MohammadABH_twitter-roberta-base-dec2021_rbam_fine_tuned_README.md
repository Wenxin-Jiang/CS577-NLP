---
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: twitter-roberta-base-dec2021_rbam_fine_tuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter-roberta-base-dec2021_rbam_fine_tuned

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base-dec2021](https://huggingface.co/cardiffnlp/twitter-roberta-base-dec2021) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8295
- Accuracy: 0.6777
- Precision: 0.6743
- Recall: 0.6777
- F1: 0.6753

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.8455        | 1.0   | 3264 | 0.7663          | 0.6661   | 0.6802    | 0.6661 | 0.6693 |
| 0.6421        | 2.0   | 6528 | 0.8295          | 0.6777   | 0.6743    | 0.6777 | 0.6753 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
