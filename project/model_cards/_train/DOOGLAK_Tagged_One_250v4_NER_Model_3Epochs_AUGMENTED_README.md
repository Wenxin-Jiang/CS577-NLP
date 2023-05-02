---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one250v4_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_250v4_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one250v4_wikigold_split
      type: tagged_one250v4_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.568499837292548
    - name: Recall
      type: recall
      value: 0.48473917869034405
    - name: F1
      type: f1
      value: 0.5232889022015875
    - name: Accuracy
      type: accuracy
      value: 0.8927736584139752
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_250v4_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one250v4_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3389
- Precision: 0.5685
- Recall: 0.4847
- F1: 0.5233
- Accuracy: 0.8928

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
| No log        | 1.0   | 87   | 0.4018          | 0.2797    | 0.1842 | 0.2221 | 0.8514   |
| No log        | 2.0   | 174  | 0.3266          | 0.5245    | 0.4398 | 0.4784 | 0.8888   |
| No log        | 3.0   | 261  | 0.3389          | 0.5685    | 0.4847 | 0.5233 | 0.8928   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
