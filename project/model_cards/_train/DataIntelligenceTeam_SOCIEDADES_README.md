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
- name: SOCIEDADES
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: sroie
      type: sroie
      config: discharge
      split: test
      args: discharge
    metrics:
    - name: Precision
      type: precision
      value: 0.972318339100346
    - name: Recall
      type: recall
      value: 0.972318339100346
    - name: F1
      type: f1
      value: 0.972318339100346
    - name: Accuracy
      type: accuracy
      value: 0.9998354676831107
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# SOCIEDADES

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the sroie dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0008
- Precision: 0.9723
- Recall: 0.9723
- F1: 0.9723
- Accuracy: 0.9998

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
- training_steps: 2000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 0.28  | 100  | 0.0013          | 0.9686    | 0.9619 | 0.9653 | 0.9998   |
| No log        | 0.56  | 200  | 0.0025          | 0.9070    | 0.9446 | 0.9254 | 0.9994   |
| No log        | 0.85  | 300  | 0.0067          | 0.8562    | 0.9273 | 0.8904 | 0.9985   |
| No log        | 1.13  | 400  | 0.0013          | 0.9454    | 0.9585 | 0.9519 | 0.9997   |
| 0.0055        | 1.41  | 500  | 0.0009          | 0.9654    | 0.9654 | 0.9654 | 0.9998   |
| 0.0055        | 1.69  | 600  | 0.0042          | 0.8795    | 0.9343 | 0.9060 | 0.9987   |
| 0.0055        | 1.97  | 700  | 0.0006          | 0.9723    | 0.9723 | 0.9723 | 0.9998   |
| 0.0055        | 2.25  | 800  | 0.0010          | 0.9485    | 0.9550 | 0.9517 | 0.9998   |
| 0.0055        | 2.54  | 900  | 0.0006          | 0.9723    | 0.9723 | 0.9723 | 0.9998   |
| 0.001         | 2.82  | 1000 | 0.0014          | 0.9553    | 0.9619 | 0.9586 | 0.9997   |
| 0.001         | 3.1   | 1100 | 0.0010          | 0.9585    | 0.9585 | 0.9585 | 0.9998   |
| 0.001         | 3.38  | 1200 | 0.0009          | 0.9585    | 0.9585 | 0.9585 | 0.9998   |
| 0.001         | 3.66  | 1300 | 0.0010          | 0.9585    | 0.9585 | 0.9585 | 0.9998   |
| 0.001         | 3.94  | 1400 | 0.0010          | 0.9654    | 0.9654 | 0.9654 | 0.9998   |
| 0.0003        | 4.23  | 1500 | 0.0008          | 0.9723    | 0.9723 | 0.9723 | 0.9998   |
| 0.0003        | 4.51  | 1600 | 0.0009          | 0.9654    | 0.9654 | 0.9654 | 0.9998   |
| 0.0003        | 4.79  | 1700 | 0.0008          | 0.9723    | 0.9723 | 0.9723 | 0.9998   |
| 0.0003        | 5.07  | 1800 | 0.0008          | 0.9723    | 0.9723 | 0.9723 | 0.9998   |
| 0.0003        | 5.35  | 1900 | 0.0008          | 0.9723    | 0.9723 | 0.9723 | 0.9998   |
| 0.0002        | 5.63  | 2000 | 0.0008          | 0.9723    | 0.9723 | 0.9723 | 0.9998   |


### Framework versions

- Transformers 4.27.0.dev0
- Pytorch 1.13.1+cu116
- Datasets 2.2.2
- Tokenizers 0.13.2
