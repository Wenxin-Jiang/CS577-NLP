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
- name: deberta-large-finetuned-qqp
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      config: qqp
      split: train
      args: qqp
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8985901558248826
    - name: F1
      type: f1
      value: 0.8648292232625608
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-large-finetuned-qqp

This model is a fine-tuned version of [microsoft/deberta-large](https://huggingface.co/microsoft/deberta-large) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2635
- Accuracy: 0.8986
- F1: 0.8648

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|
| 0.4058        | 1.0   | 22741 | 0.3923          | 0.8496   | 0.8108 |
| 0.2347        | 2.0   | 45482 | 0.2635          | 0.8986   | 0.8648 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
