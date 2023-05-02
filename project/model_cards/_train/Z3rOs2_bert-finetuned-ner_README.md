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
      config: conll2003
      split: train
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9389811738648948
    - name: Recall
      type: recall
      value: 0.9485401051571765
    - name: F1
      type: f1
      value: 0.9437364349713395
    - name: Accuracy
      type: accuracy
      value: 0.9867348721940681
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0557
- Precision: 0.9390
- Recall: 0.9485
- F1: 0.9437
- Accuracy: 0.9867

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
| 0.2174        | 1.0   | 878  | 0.0619          | 0.9296    | 0.9349 | 0.9322 | 0.9841   |
| 0.0498        | 2.0   | 1756 | 0.0550          | 0.9337    | 0.9442 | 0.9389 | 0.9861   |
| 0.0257        | 3.0   | 2634 | 0.0557          | 0.9390    | 0.9485 | 0.9437 | 0.9867   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
