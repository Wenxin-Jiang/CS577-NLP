---
tags:
- generated_from_trainer
metrics:
- spearmanr
model-index:
- name: koelectra-sts-v0.5
  results:
  - task:
      name: Text Classification
      type: text-classification
    metrics:
    - name: Spearmanr
      type: spearmanr
      value: 0.87026647480689
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# koelectra-sts-v0.5

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0213
- Pearson: 0.9958
- Spearmanr: 0.8703

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

| Training Loss | Epoch | Step  | Validation Loss | Pearson | Spearmanr |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:---------:|
| 0.058         | 1.0   | 6250  | 0.0428          | 0.9915  | 0.8702    |
| 0.0433        | 2.0   | 12500 | 0.0448          | 0.9911  | 0.8685    |
| 0.0362        | 3.0   | 18750 | 0.0261          | 0.9950  | 0.8705    |
| 0.0107        | 4.0   | 25000 | 0.0234          | 0.9953  | 0.8702    |
| 0.0075        | 5.0   | 31250 | 0.0213          | 0.9958  | 0.8703    |


### Framework versions

- Transformers 4.10.0
- Pytorch 1.10.1+cu113
- Datasets 1.17.0
- Tokenizers 0.10.3
