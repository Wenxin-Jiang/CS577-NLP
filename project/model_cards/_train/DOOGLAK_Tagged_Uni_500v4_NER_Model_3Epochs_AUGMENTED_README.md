---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_uni500v4_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_Uni_500v4_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_uni500v4_wikigold_split
      type: tagged_uni500v4_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.6813225466056982
    - name: Recall
      type: recall
      value: 0.6430942895086321
    - name: F1
      type: f1
      value: 0.6616567036720751
    - name: Accuracy
      type: accuracy
      value: 0.9231136153593894
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_Uni_500v4_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_uni500v4_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2629
- Precision: 0.6813
- Recall: 0.6431
- F1: 0.6617
- Accuracy: 0.9231

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
| No log        | 1.0   | 182  | 0.2853          | 0.5326    | 0.4525 | 0.4893 | 0.8999   |
| No log        | 2.0   | 364  | 0.2683          | 0.6492    | 0.5930 | 0.6198 | 0.9143   |
| 0.1134        | 3.0   | 546  | 0.2629          | 0.6813    | 0.6431 | 0.6617 | 0.9231   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
