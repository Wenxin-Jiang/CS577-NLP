---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article50v6_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_50v6_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article50v6_wikigold_split
      type: article50v6_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.093935790725327
    - name: Recall
      type: recall
      value: 0.0191747572815534
    - name: F1
      type: f1
      value: 0.0318484176577303
    - name: Accuracy
      type: accuracy
      value: 0.7867061489108733
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_50v6_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article50v6_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5618
- Precision: 0.0939
- Recall: 0.0192
- F1: 0.0318
- Accuracy: 0.7867

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
| No log        | 1.0   | 23   | 0.6891          | 0.1429    | 0.0002 | 0.0005 | 0.7772   |
| No log        | 2.0   | 46   | 0.5836          | 0.0796    | 0.0087 | 0.0157 | 0.7822   |
| No log        | 3.0   | 69   | 0.5618          | 0.0939    | 0.0192 | 0.0318 | 0.7867   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
