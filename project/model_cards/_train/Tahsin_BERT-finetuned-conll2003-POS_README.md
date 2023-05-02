---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- conll2003
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-finetuned-pos
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9276736387541917
    - name: Recall
      type: recall
      value: 0.9329402916272412
    - name: F1
      type: f1
      value: 0.9302995112982049
    - name: Accuracy
      type: accuracy
      value: 0.933154765408842
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-pos

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3009
- Precision: 0.9277
- Recall: 0.9329
- F1: 0.9303
- Accuracy: 0.9332

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.2791        | 1.0   | 1756 | 0.3125          | 0.9212    | 0.9263 | 0.9237 | 0.9272   |
| 0.1853        | 2.0   | 3512 | 0.3038          | 0.9241    | 0.9309 | 0.9275 | 0.9307   |
| 0.1501        | 3.0   | 5268 | 0.3009          | 0.9277    | 0.9329 | 0.9303 | 0.9332   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.17.0
- Tokenizers 0.10.3
