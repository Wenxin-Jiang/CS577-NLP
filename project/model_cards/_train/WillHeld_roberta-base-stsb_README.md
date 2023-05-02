---
language:
- en
license: mit
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- spearmanr
model-index:
- name: roberta-base-stsb
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE STSB
      type: glue
      args: stsb
    metrics:
    - name: Spearmanr
      type: spearmanr
      value: 0.9092158650855444
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-stsb

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the GLUE STSB dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4221
- Pearson: 0.9116
- Spearmanr: 0.9092
- Combined Score: 0.9104

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
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Pearson | Spearmanr | Combined Score |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:---------:|:--------------:|
| 1.6552        | 1.39  | 500  | 0.5265          | 0.8925  | 0.8925    | 0.8925         |
| 0.3579        | 2.78  | 1000 | 0.4626          | 0.9022  | 0.8991    | 0.9007         |
| 0.2198        | 4.17  | 1500 | 0.4396          | 0.9054  | 0.9042    | 0.9048         |
| 0.1585        | 5.56  | 2000 | 0.4537          | 0.9069  | 0.9052    | 0.9060         |
| 0.1139        | 6.94  | 2500 | 0.4975          | 0.9091  | 0.9065    | 0.9078         |
| 0.0868        | 8.33  | 3000 | 0.4221          | 0.9116  | 0.9092    | 0.9104         |
| 0.073         | 9.72  | 3500 | 0.4311          | 0.9096  | 0.9077    | 0.9086         |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.7.1
- Datasets 1.18.3
- Tokenizers 0.11.6
