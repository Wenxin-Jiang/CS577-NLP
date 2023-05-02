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
- name: distilbert-base-uncased-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      config: conll2003
      split: train
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9233240997229917
    - name: Recall
      type: recall
      value: 0.9322071820114106
    - name: F1
      type: f1
      value: 0.9277443776441772
    - name: Accuracy
      type: accuracy
      value: 0.9829221408486505
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0641
- Precision: 0.9233
- Recall: 0.9322
- F1: 0.9277
- Accuracy: 0.9829

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

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.2448        | 1.0   | 878  | 0.0718          | 0.9110    | 0.9165 | 0.9138 | 0.9803   |
| 0.0547        | 2.0   | 1756 | 0.0635          | 0.9197    | 0.9297 | 0.9247 | 0.9821   |
| 0.0303        | 3.0   | 2634 | 0.0641          | 0.9233    | 0.9322 | 0.9277 | 0.9829   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
