---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one500v3_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_500v3_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one500v3_wikigold_split
      type: tagged_one500v3_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.697499143542309
    - name: Recall
      type: recall
      value: 0.6782145236508994
    - name: F1
      type: f1
      value: 0.6877216686370546
    - name: Accuracy
      type: accuracy
      value: 0.9245400105495051
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_500v3_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one500v3_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2659
- Precision: 0.6975
- Recall: 0.6782
- F1: 0.6877
- Accuracy: 0.9245

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
| No log        | 1.0   | 175  | 0.2990          | 0.5405    | 0.4600 | 0.4970 | 0.9007   |
| No log        | 2.0   | 350  | 0.2789          | 0.6837    | 0.6236 | 0.6523 | 0.9157   |
| 0.1081        | 3.0   | 525  | 0.2659          | 0.6975    | 0.6782 | 0.6877 | 0.9245   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
