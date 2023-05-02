---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article250v8_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_250v8_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article250v8_wikigold_split
      type: article250v8_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.6710306406685237
    - name: Recall
      type: recall
      value: 0.6662057522123894
    - name: F1
      type: f1
      value: 0.6686094920899252
    - name: Accuracy
      type: accuracy
      value: 0.9222875386408554
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_250v8_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article250v8_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2522
- Precision: 0.6710
- Recall: 0.6662
- F1: 0.6686
- Accuracy: 0.9223

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
| No log        | 1.0   | 100  | 0.2607          | 0.5716    | 0.5575 | 0.5645 | 0.9106   |
| No log        | 2.0   | 200  | 0.2498          | 0.6572    | 0.6427 | 0.6499 | 0.9200   |
| No log        | 3.0   | 300  | 0.2522          | 0.6710    | 0.6662 | 0.6686 | 0.9223   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
