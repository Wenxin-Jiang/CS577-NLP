---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one500v5_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_500v5_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one500v5_wikigold_split
      type: tagged_one500v5_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.6984998170508598
    - name: Recall
      type: recall
      value: 0.6817857142857143
    - name: F1
      type: f1
      value: 0.690041568769203
    - name: Accuracy
      type: accuracy
      value: 0.9276886906197251
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_500v5_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one500v5_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2523
- Precision: 0.6985
- Recall: 0.6818
- F1: 0.6900
- Accuracy: 0.9277

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
| No log        | 1.0   | 161  | 0.2446          | 0.5625    | 0.5493 | 0.5558 | 0.9167   |
| No log        | 2.0   | 322  | 0.2487          | 0.6894    | 0.6557 | 0.6722 | 0.9237   |
| No log        | 3.0   | 483  | 0.2523          | 0.6985    | 0.6818 | 0.6900 | 0.9277   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
