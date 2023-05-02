---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article50v3_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_50v3_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article50v3_wikigold_split
      type: article50v3_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.206
    - name: Recall
      type: recall
      value: 0.10105469708118715
    - name: F1
      type: f1
      value: 0.13559322033898305
    - name: Accuracy
      type: accuracy
      value: 0.8114022264702575
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_50v3_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article50v3_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5311
- Precision: 0.206
- Recall: 0.1011
- F1: 0.1356
- Accuracy: 0.8114

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
| No log        | 1.0   | 14   | 0.7040          | 0.1205    | 0.0066 | 0.0126 | 0.7826   |
| No log        | 2.0   | 28   | 0.5785          | 0.2183    | 0.0844 | 0.1217 | 0.8046   |
| No log        | 3.0   | 42   | 0.5311          | 0.206     | 0.1011 | 0.1356 | 0.8114   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
