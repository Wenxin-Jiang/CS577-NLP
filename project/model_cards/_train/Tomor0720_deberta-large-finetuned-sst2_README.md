---
license: mit
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: deberta-large-finetuned-sst2
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
      value: 0.9495412844036697
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-large-finetuned-sst2

This model is a fine-tuned version of [microsoft/deberta-large](https://huggingface.co/microsoft/deberta-large) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2159
- Accuracy: 0.9495

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.1214        | 1.0   | 4210  | 0.1969          | 0.9438   |
| 0.067         | 2.0   | 8420  | 0.2159          | 0.9495   |
| 0.0405        | 3.0   | 12630 | 0.2159          | 0.9495   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
