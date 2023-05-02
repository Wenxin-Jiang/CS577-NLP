---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wnut_17
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: distilbert-base-uncased_ner_wnut_17
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wnut_17
      type: wnut_17
      args: wnut_17
    metrics:
    - name: Precision
      type: precision
      value: 0.6700879765395894
    - name: Recall
      type: recall
      value: 0.5466507177033493
    - name: F1
      type: f1
      value: 0.6021080368906456
    - name: Accuracy
      type: accuracy
      value: 0.9559412550066756
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased_ner_wnut_17

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the wnut_17 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2400
- Precision: 0.6701
- Recall: 0.5467
- F1: 0.6021
- Accuracy: 0.9559

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
- lr_scheduler_type: cosine
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 213  | 0.2367          | 0.6879    | 0.4270 | 0.5269 | 0.9455   |
| No log        | 2.0   | 426  | 0.2272          | 0.6913    | 0.4928 | 0.5754 | 0.9533   |
| 0.173         | 3.0   | 639  | 0.2393          | 0.6788    | 0.5132 | 0.5845 | 0.9553   |
| 0.173         | 4.0   | 852  | 0.2338          | 0.6541    | 0.5610 | 0.6040 | 0.9557   |
| 0.0489        | 5.0   | 1065 | 0.2400          | 0.6701    | 0.5467 | 0.6021 | 0.9559   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
