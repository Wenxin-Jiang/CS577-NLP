---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one500v2_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_500v2_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one500v2_wikigold_split
      type: tagged_one500v2_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.6801334321719792
    - name: Recall
      type: recall
      value: 0.6826636904761905
    - name: F1
      type: f1
      value: 0.681396212402525
    - name: Accuracy
      type: accuracy
      value: 0.9255115790793144
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_500v2_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one500v2_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2644
- Precision: 0.6801
- Recall: 0.6827
- F1: 0.6814
- Accuracy: 0.9255

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
| No log        | 1.0   | 172  | 0.2827          | 0.5880    | 0.5692 | 0.5784 | 0.9073   |
| No log        | 2.0   | 344  | 0.2581          | 0.6629    | 0.6585 | 0.6607 | 0.9222   |
| 0.1089        | 3.0   | 516  | 0.2644          | 0.6801    | 0.6827 | 0.6814 | 0.9255   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
