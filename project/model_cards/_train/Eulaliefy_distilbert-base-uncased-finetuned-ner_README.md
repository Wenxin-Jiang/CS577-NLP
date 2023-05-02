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
      value: 0.9250691754288877
    - name: Recall
      type: recall
      value: 0.9350039154267815
    - name: F1
      type: f1
      value: 0.9300100144653389
    - name: Accuracy
      type: accuracy
      value: 0.9836052552147044
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0620
- Precision: 0.9251
- Recall: 0.9350
- F1: 0.9300
- Accuracy: 0.9836

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
| 0.2356        | 1.0   | 878  | 0.0699          | 0.9110    | 0.9225 | 0.9167 | 0.9801   |
| 0.0509        | 2.0   | 1756 | 0.0621          | 0.9180    | 0.9314 | 0.9246 | 0.9823   |
| 0.0303        | 3.0   | 2634 | 0.0620          | 0.9251    | 0.9350 | 0.9300 | 0.9836   |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
