---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_uni250v0_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_Uni_250v0_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_uni250v0_wikigold_split
      type: tagged_uni250v0_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.4747682801235839
    - name: Recall
      type: recall
      value: 0.37317862924986506
    - name: F1
      type: f1
      value: 0.41788789847408975
    - name: Accuracy
      type: accuracy
      value: 0.8846524500234748
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_Uni_250v0_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_uni250v0_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3679
- Precision: 0.4748
- Recall: 0.3732
- F1: 0.4179
- Accuracy: 0.8847

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
| No log        | 1.0   | 91   | 0.4333          | 0.2856    | 0.1851 | 0.2246 | 0.8440   |
| No log        | 2.0   | 182  | 0.3466          | 0.3907    | 0.3038 | 0.3418 | 0.8794   |
| No log        | 3.0   | 273  | 0.3679          | 0.4748    | 0.3732 | 0.4179 | 0.8847   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
