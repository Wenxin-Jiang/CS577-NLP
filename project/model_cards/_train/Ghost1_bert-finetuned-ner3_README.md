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
- name: bert-finetuned-ner3
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
      value: 0.9296076491922189
    - name: Recall
      type: recall
      value: 0.9490070683271625
    - name: F1
      type: f1
      value: 0.9392071952031978
    - name: Accuracy
      type: accuracy
      value: 0.986342497203744
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner3

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0603
- Precision: 0.9296
- Recall: 0.9490
- F1: 0.9392
- Accuracy: 0.9863

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
| 0.0855        | 1.0   | 1756 | 0.0673          | 0.9130    | 0.9340 | 0.9234 | 0.9827   |
| 0.0345        | 2.0   | 3512 | 0.0590          | 0.9284    | 0.9445 | 0.9363 | 0.9855   |
| 0.0229        | 3.0   | 5268 | 0.0603          | 0.9296    | 0.9490 | 0.9392 | 0.9863   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1
