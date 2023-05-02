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
- name: muril-base-cased-finetuned-non-code-mixed-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# muril-base-cased-finetuned-non-code-mixed-DS

This model is a fine-tuned version of [google/muril-base-cased](https://huggingface.co/google/muril-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2867
- Accuracy: 0.6214
- Precision: 0.6081
- Recall: 0.6009
- F1: 0.6034

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
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 25

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0861        | 2.0   | 463  | 1.0531          | 0.3506   | 0.1169    | 0.3333 | 0.1731 |
| 0.99          | 3.99  | 926  | 0.9271          | 0.5836   | 0.4310    | 0.5200 | 0.4502 |
| 0.8759        | 5.99  | 1389 | 0.9142          | 0.5965   | 0.5788    | 0.5907 | 0.5802 |
| 0.7726        | 7.98  | 1852 | 0.8726          | 0.6095   | 0.6079    | 0.6078 | 0.6027 |
| 0.6659        | 9.98  | 2315 | 0.9145          | 0.6246   | 0.6139    | 0.6174 | 0.6140 |
| 0.5727        | 11.97 | 2778 | 0.9606          | 0.6311   | 0.6180    | 0.6109 | 0.6133 |
| 0.4889        | 13.97 | 3241 | 1.0342          | 0.6170   | 0.6059    | 0.6054 | 0.6045 |
| 0.4267        | 15.97 | 3704 | 1.0539          | 0.6170   | 0.6089    | 0.6081 | 0.6066 |
| 0.3751        | 17.96 | 4167 | 1.1740          | 0.6343   | 0.6255    | 0.6074 | 0.6112 |
| 0.3402        | 19.96 | 4630 | 1.2021          | 0.6192   | 0.6078    | 0.6013 | 0.6031 |
| 0.318         | 21.95 | 5093 | 1.2875          | 0.6181   | 0.6007    | 0.5946 | 0.5965 |
| 0.2977        | 23.95 | 5556 | 1.2867          | 0.6214   | 0.6081    | 0.6009 | 0.6034 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
