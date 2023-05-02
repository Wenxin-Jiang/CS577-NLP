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
      value: 0.9325062034739454
    - name: Recall
      type: recall
      value: 0.9486704813194211
    - name: F1
      type: f1
      value: 0.9405188954700927
    - name: Accuracy
      type: accuracy
      value: 0.9859745687878966
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0618
- Precision: 0.9325
- Recall: 0.9487
- F1: 0.9405
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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0874        | 1.0   | 1756 | 0.0645          | 0.9194    | 0.9382 | 0.9287 | 0.9835   |
| 0.0384        | 2.0   | 3512 | 0.0614          | 0.9297    | 0.9463 | 0.9379 | 0.9845   |
| 0.0186        | 3.0   | 5268 | 0.0618          | 0.9325    | 0.9487 | 0.9405 | 0.9860   |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
