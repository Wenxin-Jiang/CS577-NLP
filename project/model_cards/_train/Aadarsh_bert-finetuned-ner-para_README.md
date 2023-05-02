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
- name: bert-finetuned-ner-para
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner-para

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0818
- Precision: 0.6445
- Recall: 0.7434
- F1: 0.6904
- Accuracy: 0.9762

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
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 80   | 0.2387          | 0.4214    | 0.4053 | 0.4132 | 0.9387   |
| No log        | 2.0   | 160  | 0.1301          | 0.6105    | 0.6163 | 0.6134 | 0.9650   |
| No log        | 3.0   | 240  | 0.0952          | 0.6515    | 0.7218 | 0.6849 | 0.9741   |
| No log        | 4.0   | 320  | 0.0818          | 0.6445    | 0.7434 | 0.6904 | 0.9762   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
