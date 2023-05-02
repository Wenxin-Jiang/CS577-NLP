---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: roberta-base-finetuned-removed-0530
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-finetuned-removed-0530

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7910
- Accuracy: 0.9082
- F1: 0.9084

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|
| No log        | 1.0   | 3180  | 0.6250          | 0.8277   | 0.8250 |
| No log        | 2.0   | 6360  | 0.4578          | 0.8689   | 0.8684 |
| No log        | 3.0   | 9540  | 0.4834          | 0.8792   | 0.8797 |
| No log        | 4.0   | 12720 | 0.6377          | 0.8899   | 0.8902 |
| No log        | 5.0   | 15900 | 0.6498          | 0.8921   | 0.8921 |
| No log        | 6.0   | 19080 | 0.6628          | 0.8931   | 0.8928 |
| No log        | 7.0   | 22260 | 0.7380          | 0.8925   | 0.8918 |
| 0.2877        | 8.0   | 25440 | 0.7313          | 0.8975   | 0.8974 |
| 0.2877        | 9.0   | 28620 | 0.7593          | 0.9025   | 0.9026 |
| 0.2877        | 10.0  | 31800 | 0.7910          | 0.9082   | 0.9084 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.9.0
- Datasets 1.16.1
- Tokenizers 0.12.1
