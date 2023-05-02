---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_uni500v1_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_Uni_500v1_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_uni500v1_wikigold_split
      type: tagged_uni500v1_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.7048748353096179
    - name: Recall
      type: recall
      value: 0.7076719576719577
    - name: F1
      type: f1
      value: 0.7062706270627063
    - name: Accuracy
      type: accuracy
      value: 0.9309102015882712
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_Uni_500v1_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_uni500v1_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2425
- Precision: 0.7049
- Recall: 0.7077
- F1: 0.7063
- Accuracy: 0.9309

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
| No log        | 1.0   | 163  | 0.2804          | 0.4476    | 0.3886 | 0.4160 | 0.9019   |
| No log        | 2.0   | 326  | 0.2401          | 0.6803    | 0.6657 | 0.6729 | 0.9265   |
| No log        | 3.0   | 489  | 0.2425          | 0.7049    | 0.7077 | 0.7063 | 0.9309   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
