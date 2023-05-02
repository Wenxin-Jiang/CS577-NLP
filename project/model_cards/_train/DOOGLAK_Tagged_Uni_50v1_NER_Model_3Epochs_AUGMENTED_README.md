---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_uni50v1_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_Uni_50v1_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_uni50v1_wikigold_split
      type: tagged_uni50v1_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.14664804469273743
    - name: Recall
      type: recall
      value: 0.025647288715192965
    - name: F1
      type: f1
      value: 0.043659043659043655
    - name: Accuracy
      type: accuracy
      value: 0.7940580232453374
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_Uni_50v1_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_uni50v1_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5851
- Precision: 0.1466
- Recall: 0.0256
- F1: 0.0437
- Accuracy: 0.7941

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
| No log        | 1.0   | 24   | 0.6704          | 0.0       | 0.0    | 0.0    | 0.7775   |
| No log        | 2.0   | 48   | 0.5824          | 0.1479    | 0.0154 | 0.0279 | 0.7895   |
| No log        | 3.0   | 72   | 0.5851          | 0.1466    | 0.0256 | 0.0437 | 0.7941   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
