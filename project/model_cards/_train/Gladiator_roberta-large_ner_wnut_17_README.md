---
license: mit
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
- name: roberta-large_ner_wnut_17
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
      value: 0.7345505617977528
    - name: Recall
      type: recall
      value: 0.6255980861244019
    - name: F1
      type: f1
      value: 0.6757105943152455
    - name: Accuracy
      type: accuracy
      value: 0.9650416322379711
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large_ner_wnut_17

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on the wnut_17 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2288
- Precision: 0.7346
- Recall: 0.6256
- F1: 0.6757
- Accuracy: 0.9650

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
| No log        | 1.0   | 213  | 0.1805          | 0.6403    | 0.6089 | 0.6242 | 0.9598   |
| No log        | 2.0   | 426  | 0.1925          | 0.7314    | 0.5993 | 0.6588 | 0.9624   |
| 0.1192        | 3.0   | 639  | 0.1883          | 0.7088    | 0.6172 | 0.6598 | 0.9637   |
| 0.1192        | 4.0   | 852  | 0.2144          | 0.7289    | 0.6400 | 0.6815 | 0.9655   |
| 0.0301        | 5.0   | 1065 | 0.2288          | 0.7346    | 0.6256 | 0.6757 | 0.9650   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
