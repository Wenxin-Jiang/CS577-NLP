---
license: mit
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: camembert-base-finetuned-Train_RAW10-dd
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# camembert-base-finetuned-Train_RAW10-dd

This model is a fine-tuned version of [camembert-base](https://huggingface.co/camembert-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2175
- Precision: 0.8744
- Recall: 0.9056
- F1: 0.8897
- Accuracy: 0.9357

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1873        | 1.0   | 9930  | 0.2088          | 0.8652    | 0.8927 | 0.8788 | 0.9326   |
| 0.1533        | 2.0   | 19860 | 0.2175          | 0.8744    | 0.9056 | 0.8897 | 0.9357   |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
