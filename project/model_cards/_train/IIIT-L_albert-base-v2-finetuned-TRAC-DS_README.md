---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: albert-base-v2-finetuned-TRAC-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-base-v2-finetuned-TRAC-DS

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8271
- Accuracy: 0.6315
- Precision: 0.6206
- Recall: 0.6201
- F1: 0.6147

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.919508251872584e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0373        | 1.0   | 612  | 1.1241          | 0.3627   | 0.5914    | 0.3618 | 0.2414 |
| 1.0617        | 2.0   | 1224 | 1.1039          | 0.3350   | 0.2781    | 0.3354 | 0.1740 |
| 0.9791        | 3.0   | 1836 | 0.8365          | 0.5989   | 0.6192    | 0.5887 | 0.5883 |
| 0.798         | 3.99  | 2448 | 0.8271          | 0.6315   | 0.6206    | 0.6201 | 0.6147 |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
