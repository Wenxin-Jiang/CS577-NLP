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
- name: bert-finetuned-ner
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
      value: 0.9321670242614293
    - name: Recall
      type: recall
      value: 0.9505217098619994
    - name: F1
      type: f1
      value: 0.9412548954253812
    - name: Accuracy
      type: accuracy
      value: 0.9860334373344322
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0575
- Precision: 0.9322
- Recall: 0.9505
- F1: 0.9413
- Accuracy: 0.9860

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
| 0.2219        | 1.0   | 878  | 0.0716          | 0.9076    | 0.9288 | 0.9181 | 0.9808   |
| 0.0453        | 2.0   | 1756 | 0.0597          | 0.9297    | 0.9477 | 0.9386 | 0.9852   |
| 0.0239        | 3.0   | 2634 | 0.0575          | 0.9322    | 0.9505 | 0.9413 | 0.9860   |


### Framework versions

- Transformers 4.12.3
- Pytorch 1.8.2+cu111
- Datasets 1.15.1
- Tokenizers 0.10.3
