---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one500v4_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_500v4_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one500v4_wikigold_split
      type: tagged_one500v4_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.6656017039403621
    - name: Recall
      type: recall
      value: 0.6225099601593626
    - name: F1
      type: f1
      value: 0.6433350488934636
    - name: Accuracy
      type: accuracy
      value: 0.9187013683928092
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_500v4_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one500v4_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2804
- Precision: 0.6656
- Recall: 0.6225
- F1: 0.6433
- Accuracy: 0.9187

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
| No log        | 1.0   | 183  | 0.2784          | 0.5897    | 0.5076 | 0.5456 | 0.9064   |
| No log        | 2.0   | 366  | 0.2816          | 0.6535    | 0.5787 | 0.6138 | 0.9112   |
| 0.1091        | 3.0   | 549  | 0.2804          | 0.6656    | 0.6225 | 0.6433 | 0.9187   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
