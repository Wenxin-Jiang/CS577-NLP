---
license: mit
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: deberta-v3-base-finetuned-rte
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      config: rte
      split: train
      args: rte
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8194945848375451
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-base-finetuned-rte

This model is a fine-tuned version of [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8234
- Accuracy: 0.8195

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 156  | 0.5610          | 0.7545   |
| No log        | 2.0   | 312  | 0.6270          | 0.7617   |
| No log        | 3.0   | 468  | 0.6565          | 0.7906   |
| 0.3919        | 4.0   | 624  | 0.8234          | 0.8195   |
| 0.3919        | 5.0   | 780  | 0.9628          | 0.7978   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2