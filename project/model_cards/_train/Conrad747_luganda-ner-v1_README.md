---
license: mit
tags:
- generated_from_trainer
datasets:
- lg-ner
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: luganda-ner-v1
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: lg-ner
      type: lg-ner
      config: lug
      split: test
      args: lug
    metrics:
    - name: Precision
      type: precision
      value: 0.7987967914438503
    - name: Recall
      type: recall
      value: 0.8025520483546004
    - name: F1
      type: f1
      value: 0.8006700167504188
    - name: Accuracy
      type: accuracy
      value: 0.9451502831421519
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# luganda-ner-v1

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the lg-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3188
- Precision: 0.7988
- Recall: 0.8026
- F1: 0.8007
- Accuracy: 0.9452

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 261  | 0.2915          | 0.7456    | 0.6891 | 0.7162 | 0.9240   |
| 0.2284        | 2.0   | 522  | 0.2965          | 0.7393    | 0.7314 | 0.7353 | 0.9294   |
| 0.2284        | 3.0   | 783  | 0.2830          | 0.7426    | 0.7576 | 0.7500 | 0.9271   |
| 0.1426        | 4.0   | 1044 | 0.2710          | 0.7935    | 0.7690 | 0.7810 | 0.9387   |
| 0.1426        | 5.0   | 1305 | 0.2805          | 0.8087    | 0.7636 | 0.7855 | 0.9389   |
| 0.0881        | 6.0   | 1566 | 0.2992          | 0.7734    | 0.7884 | 0.7808 | 0.9404   |
| 0.0881        | 7.0   | 1827 | 0.2746          | 0.8109    | 0.7864 | 0.7985 | 0.9457   |
| 0.0582        | 8.0   | 2088 | 0.3149          | 0.7753    | 0.7925 | 0.7838 | 0.9400   |
| 0.0582        | 9.0   | 2349 | 0.3179          | 0.7940    | 0.7945 | 0.7942 | 0.9440   |
| 0.0403        | 10.0  | 2610 | 0.3188          | 0.7988    | 0.8026 | 0.8007 | 0.9452   |


### Framework versions

- Transformers 4.27.4
- Pytorch 1.13.1+cu116
- Datasets 2.11.0
- Tokenizers 0.13.2
