---
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased-finetuned-sst2-finetuned-sst2
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      config: sst2
      split: train
      args: sst2
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9071100917431193
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-sst2-finetuned-sst2

This model was trained from scratch on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3156
- Accuracy: 0.9071

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
- train_batch_size: 256
- eval_batch_size: 256
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 264  | 0.2830          | 0.9014   |
| 0.111         | 2.0   | 528  | 0.3156          | 0.9071   |
| 0.111         | 3.0   | 792  | 0.3351          | 0.8979   |
| 0.0688        | 4.0   | 1056 | 0.3377          | 0.9037   |
| 0.0688        | 5.0   | 1320 | 0.3526          | 0.9048   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1
- Datasets 2.7.1
- Tokenizers 0.13.2
