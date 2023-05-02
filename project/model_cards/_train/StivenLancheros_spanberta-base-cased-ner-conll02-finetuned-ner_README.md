---
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
- name: spanberta-base-cased-ner-conll02-finetuned-ner
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
      value: 0.911773494695951
    - name: Recall
      type: recall
      value: 0.9149861308943699
    - name: F1
      type: f1
      value: 0.9133769878391019
    - name: Accuracy
      type: accuracy
      value: 0.9803183888541573
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# spanberta-base-cased-ner-conll02-finetuned-ner

This model is a fine-tuned version of [skimai/spanberta-base-cased-ner-conll02](https://huggingface.co/skimai/spanberta-base-cased-ner-conll02) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0824
- Precision: 0.9118
- Recall: 0.9150
- F1: 0.9134
- Accuracy: 0.9803

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
| 0.2641        | 1.0   | 878  | 0.0923          | 0.8818    | 0.8802 | 0.8810 | 0.9739   |
| 0.0648        | 2.0   | 1756 | 0.0817          | 0.9033    | 0.9044 | 0.9038 | 0.9785   |
| 0.0314        | 3.0   | 2634 | 0.0824          | 0.9118    | 0.9150 | 0.9134 | 0.9803   |


### Framework versions

- Transformers 4.12.3
- Pytorch 1.9.0+cu111
- Datasets 1.15.1
- Tokenizers 0.10.3
