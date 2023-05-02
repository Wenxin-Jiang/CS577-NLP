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
- name: bert-finetuned-ner1
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
      value: 0.9285832096321953
    - name: Recall
      type: recall
      value: 0.9474924267923258
    - name: F1
      type: f1
      value: 0.9379425239483548
    - name: Accuracy
      type: accuracy
      value: 0.9859009831047272
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner1

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0584
- Precision: 0.9286
- Recall: 0.9475
- F1: 0.9379
- Accuracy: 0.9859

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
| 0.2183        | 1.0   | 878  | 0.0753          | 0.9087    | 0.9291 | 0.9188 | 0.9800   |
| 0.0462        | 2.0   | 1756 | 0.0614          | 0.9329    | 0.9470 | 0.9399 | 0.9858   |
| 0.0244        | 3.0   | 2634 | 0.0584          | 0.9286    | 0.9475 | 0.9379 | 0.9859   |


### Framework versions

- Transformers 4.12.3
- Pytorch 1.8.2+cu111
- Datasets 1.15.1
- Tokenizers 0.10.3
