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
      value: 0.9250386398763524
    - name: Recall
      type: recall
      value: 0.9373531714956931
    - name: F1
      type: f1
      value: 0.9311551925320887
    - name: Accuracy
      type: accuracy
      value: 0.9839388692074285
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0589
- Precision: 0.9250
- Recall: 0.9374
- F1: 0.9312
- Accuracy: 0.9839

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
| 0.2343        | 1.0   | 878  | 0.0674          | 0.9177    | 0.9233 | 0.9205 | 0.9818   |
| 0.0525        | 2.0   | 1756 | 0.0582          | 0.9245    | 0.9362 | 0.9304 | 0.9837   |
| 0.0288        | 3.0   | 2634 | 0.0589          | 0.9250    | 0.9374 | 0.9312 | 0.9839   |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1
- Datasets 2.5.1
- Tokenizers 0.12.1
