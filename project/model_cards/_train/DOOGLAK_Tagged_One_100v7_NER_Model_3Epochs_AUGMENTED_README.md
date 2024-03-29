---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one100v7_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_100v7_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one100v7_wikigold_split
      type: tagged_one100v7_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.2402332361516035
    - name: Recall
      type: recall
      value: 0.10690192008303062
    - name: F1
      type: f1
      value: 0.14796193212425932
    - name: Accuracy
      type: accuracy
      value: 0.817534449274022
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_100v7_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one100v7_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5232
- Precision: 0.2402
- Recall: 0.1069
- F1: 0.1480
- Accuracy: 0.8175

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
| No log        | 1.0   | 26   | 0.6129          | 0.0647    | 0.0023 | 0.0045 | 0.7840   |
| No log        | 2.0   | 52   | 0.5177          | 0.2035    | 0.0807 | 0.1156 | 0.8130   |
| No log        | 3.0   | 78   | 0.5232          | 0.2402    | 0.1069 | 0.1480 | 0.8175   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
