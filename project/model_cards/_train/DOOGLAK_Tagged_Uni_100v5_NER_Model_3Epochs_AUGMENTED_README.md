---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_uni100v5_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_Uni_100v5_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_uni100v5_wikigold_split
      type: tagged_uni100v5_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.27475592747559274
    - name: Recall
      type: recall
      value: 0.20112302194997447
    - name: F1
      type: f1
      value: 0.2322428529325081
    - name: Accuracy
      type: accuracy
      value: 0.8489666875886277
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_Uni_100v5_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_uni100v5_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4479
- Precision: 0.2748
- Recall: 0.2011
- F1: 0.2322
- Accuracy: 0.8490

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
| No log        | 1.0   | 39   | 0.4908          | 0.2544    | 0.1445 | 0.1843 | 0.8292   |
| No log        | 2.0   | 78   | 0.4703          | 0.2611    | 0.1881 | 0.2187 | 0.8437   |
| No log        | 3.0   | 117  | 0.4479          | 0.2748    | 0.2011 | 0.2322 | 0.8490   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
