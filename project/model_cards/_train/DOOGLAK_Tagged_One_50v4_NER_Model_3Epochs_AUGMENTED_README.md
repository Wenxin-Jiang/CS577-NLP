---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one50v4_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_50v4_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one50v4_wikigold_split
      type: tagged_one50v4_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.3559670781893004
    - name: Recall
      type: recall
      value: 0.04205153135634419
    - name: F1
      type: f1
      value: 0.07521739130434783
    - name: Accuracy
      type: accuracy
      value: 0.7920209433455652
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_50v4_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one50v4_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5788
- Precision: 0.3560
- Recall: 0.0421
- F1: 0.0752
- Accuracy: 0.7920

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
| No log        | 1.0   | 22   | 0.6655          | 0.0       | 0.0    | 0.0    | 0.7775   |
| No log        | 2.0   | 44   | 0.5894          | 0.4073    | 0.0272 | 0.0510 | 0.7856   |
| No log        | 3.0   | 66   | 0.5788          | 0.3560    | 0.0421 | 0.0752 | 0.7920   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
