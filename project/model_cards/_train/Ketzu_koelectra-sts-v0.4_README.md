---
tags:
- generated_from_trainer
metrics:
- spearmanr
model-index:
- name: koelectra-sts-v0.4
  results:
  - task:
      name: Text Classification
      type: text-classification
    metrics:
    - name: Spearmanr
      type: spearmanr
      value: 0.9286505242442783
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# koelectra-sts-v0.4

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3368
- Pearson: 0.9303
- Spearmanr: 0.9287

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Pearson | Spearmanr |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:---------:|
| 0.0345        | 1.0   | 730  | 0.3368          | 0.9303  | 0.9287    |
| 0.0343        | 2.0   | 1460 | 0.3368          | 0.9303  | 0.9287    |
| 0.0337        | 3.0   | 2190 | 0.3368          | 0.9303  | 0.9287    |
| 0.0345        | 4.0   | 2920 | 0.3368          | 0.9303  | 0.9287    |
| 0.0347        | 5.0   | 3650 | 0.3368          | 0.9303  | 0.9287    |


### Framework versions

- Transformers 4.10.0
- Pytorch 1.10.1+cu113
- Datasets 1.17.0
- Tokenizers 0.10.3
