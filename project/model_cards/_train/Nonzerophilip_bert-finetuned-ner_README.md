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
      value: 0.7978891820580475
    - name: Recall
      type: recall
      value: 0.8600682593856656
    - name: F1
      type: f1
      value: 0.8278127566383794
    - name: Accuracy
      type: accuracy
      value: 0.9614351593776922
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1286
- Precision: 0.7979
- Recall: 0.8601
- F1: 0.8278
- Accuracy: 0.9614

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
| No log        | 1.0   | 125  | 0.2188          | 0.6221    | 0.6985 | 0.6581 | 0.9285   |
| No log        | 2.0   | 250  | 0.1396          | 0.7681    | 0.8402 | 0.8025 | 0.9590   |
| No log        | 3.0   | 375  | 0.1286          | 0.7979    | 0.8601 | 0.8278 | 0.9614   |


### Framework versions

- Transformers 4.19.3
- Pytorch 1.7.1
- Datasets 2.2.2
- Tokenizers 0.12.1
