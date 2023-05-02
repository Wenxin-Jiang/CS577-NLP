---
license: mit
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
- f1
model-index:
- name: deberta-v3-base-finetuned-mrpc
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      config: mrpc
      split: train
      args: mrpc
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8921568627450981
    - name: F1
      type: f1
      value: 0.9241379310344827
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-base-finetuned-mrpc

This model is a fine-tuned version of [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3297
- Accuracy: 0.8922
- F1: 0.9241

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| No log        | 1.0   | 230  | 0.3411          | 0.8725   | 0.9081 |
| No log        | 2.0   | 460  | 0.3297          | 0.8922   | 0.9241 |
| 0.3727        | 3.0   | 690  | 0.4133          | 0.8922   | 0.9236 |
| 0.3727        | 4.0   | 920  | 0.5315          | 0.8848   | 0.9174 |
| 0.1068        | 5.0   | 1150 | 0.5898          | 0.8848   | 0.9171 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
