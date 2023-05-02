---
license: cc-by-nc-sa-4.0
tags:
- generated_from_trainer
datasets:
- sroie
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: REPROCESO
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: sroie
      type: sroie
      config: discharge
      split: train
      args: discharge
    metrics:
    - name: Precision
      type: precision
      value: 0.9666666666666667
    - name: Recall
      type: recall
      value: 0.9666666666666667
    - name: F1
      type: f1
      value: 0.9666666666666667
    - name: Accuracy
      type: accuracy
      value: 0.9991055456171736
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# REPROCESO

This model is a fine-tuned version of [microsoft/layoutlmv3-large](https://huggingface.co/microsoft/layoutlmv3-large) on the sroie dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0069
- Precision: 0.9667
- Recall: 0.9667
- F1: 0.9667
- Accuracy: 0.9991

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 1000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 7.14  | 100  | 0.0048          | 0.9667    | 0.9667 | 0.9667 | 0.9991   |
| No log        | 14.29 | 200  | 0.0054          | 0.9667    | 0.9667 | 0.9667 | 0.9991   |
| No log        | 21.43 | 300  | 0.0058          | 0.9667    | 0.9667 | 0.9667 | 0.9991   |
| No log        | 28.57 | 400  | 0.0061          | 0.9667    | 0.9667 | 0.9667 | 0.9991   |
| 0.0095        | 35.71 | 500  | 0.0063          | 0.9667    | 0.9667 | 0.9667 | 0.9991   |
| 0.0095        | 42.86 | 600  | 0.0065          | 0.9667    | 0.9667 | 0.9667 | 0.9991   |
| 0.0095        | 50.0  | 700  | 0.0067          | 0.9667    | 0.9667 | 0.9667 | 0.9991   |
| 0.0095        | 57.14 | 800  | 0.0068          | 0.9667    | 0.9667 | 0.9667 | 0.9991   |
| 0.0095        | 64.29 | 900  | 0.0069          | 0.9667    | 0.9667 | 0.9667 | 0.9991   |
| 0.0           | 71.43 | 1000 | 0.0069          | 0.9667    | 0.9667 | 0.9667 | 0.9991   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.2.2
- Tokenizers 0.13.2
