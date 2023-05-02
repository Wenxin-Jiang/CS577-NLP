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
model_index:
- name: distilbert-base-uncased-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      args: conll2003
    metric:
      name: Accuracy
      type: accuracy
      value: 0.9833669595056158
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0611
- Precision: 0.9250
- Recall: 0.9321
- F1: 0.9285
- Accuracy: 0.9834

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
| 0.2399        | 1.0   | 878  | 0.0702          | 0.9118    | 0.9208 | 0.9163 | 0.9805   |
| 0.0503        | 2.0   | 1756 | 0.0614          | 0.9176    | 0.9311 | 0.9243 | 0.9824   |
| 0.0304        | 3.0   | 2634 | 0.0611          | 0.9250    | 0.9321 | 0.9285 | 0.9834   |


### Framework versions

- Transformers 4.9.1
- Pytorch 1.9.0+cu102
- Datasets 1.11.0
- Tokenizers 0.10.3
