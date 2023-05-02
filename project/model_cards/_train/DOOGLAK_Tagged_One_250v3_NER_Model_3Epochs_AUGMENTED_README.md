---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one250v3_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_250v3_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one250v3_wikigold_split
      type: tagged_one250v3_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.5783339046966061
    - name: Recall
      type: recall
      value: 0.4806267806267806
    - name: F1
      type: f1
      value: 0.5249727711218297
    - name: Accuracy
      type: accuracy
      value: 0.8981560947699669
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_250v3_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one250v3_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3179
- Precision: 0.5783
- Recall: 0.4806
- F1: 0.5250
- Accuracy: 0.8982

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
| No log        | 1.0   | 81   | 0.3974          | 0.2778    | 0.1869 | 0.2235 | 0.8530   |
| No log        | 2.0   | 162  | 0.3095          | 0.5594    | 0.4470 | 0.4969 | 0.8944   |
| No log        | 3.0   | 243  | 0.3179          | 0.5783    | 0.4806 | 0.5250 | 0.8982   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
