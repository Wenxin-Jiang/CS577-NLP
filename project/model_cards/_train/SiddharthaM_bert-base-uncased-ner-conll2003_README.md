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
- name: bert-base-uncased-ner-conll2003
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
      value: 0.9342126957955482
    - name: Recall
      type: recall
      value: 0.9535509929316729
    - name: F1
      type: f1
      value: 0.943782793370534
    - name: Accuracy
      type: accuracy
      value: 0.9870194854889033
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-ner-conll2003

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0602
- Precision: 0.9342
- Recall: 0.9536
- F1: 0.9438
- Accuracy: 0.9870

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
| 0.0871        | 1.0   | 1756 | 0.0728          | 0.9138    | 0.9275 | 0.9206 | 0.9811   |
| 0.0331        | 2.0   | 3512 | 0.0591          | 0.9311    | 0.9514 | 0.9411 | 0.9866   |
| 0.0173        | 3.0   | 5268 | 0.0602          | 0.9342    | 0.9536 | 0.9438 | 0.9870   |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
