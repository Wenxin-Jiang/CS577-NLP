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
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9230429988974642
    - name: Recall
      type: recall
      value: 0.9365700861393892
    - name: F1
      type: f1
      value: 0.9297573435504469
    - name: Accuracy
      type: accuracy
      value: 0.983176322938345
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0611
- Precision: 0.9230
- Recall: 0.9366
- F1: 0.9298
- Accuracy: 0.9832

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
| 0.2349        | 1.0   | 878  | 0.0736          | 0.9140    | 0.9211 | 0.9175 | 0.9803   |
| 0.0546        | 2.0   | 1756 | 0.0582          | 0.9244    | 0.9368 | 0.9305 | 0.9830   |
| 0.03          | 3.0   | 2634 | 0.0611          | 0.9230    | 0.9366 | 0.9298 | 0.9832   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
