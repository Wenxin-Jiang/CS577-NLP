---
license: apache-2.0
tags:
- text-classification
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
- f1
model-index:
- name: platzi-roberta-bryan
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
      value: 0.8308823529411765
    - name: F1
      type: f1
      value: 0.8787346221441125
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# platzi-roberta-bryan

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on the glue and the mrpc datasets.
It achieves the following results on the evaluation set:
- Loss: 0.6294
- Accuracy: 0.8309
- F1: 0.8787

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.3798        | 1.09  | 500  | 0.6294          | 0.8309   | 0.8787 |
| 0.3876        | 2.18  | 1000 | 0.6294          | 0.8309   | 0.8787 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
