---
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: roberta-base-finetuned-sst2
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      args: sst2
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.944954128440367
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-finetuned-sst2

This model was trained from scratch on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3000
- Accuracy: 0.9450

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

| Training Loss | Epoch | Step  | Accuracy | Validation Loss |
|:-------------:|:-----:|:-----:|:--------:|:---------------:|
| 0.1106        | 1.0   | 4210  | 0.9255   | 0.3326          |
| 0.1497        | 2.0   | 8420  | 0.9369   | 0.2858          |
| 0.1028        | 3.0   | 12630 | 0.3128   | 0.9335          |
| 0.0872        | 4.0   | 16840 | 0.3000   | 0.9450          |
| 0.0571        | 5.0   | 21050 | 0.3378   | 0.9427          |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0+cu111
- Datasets 1.14.0
- Tokenizers 0.10.3
