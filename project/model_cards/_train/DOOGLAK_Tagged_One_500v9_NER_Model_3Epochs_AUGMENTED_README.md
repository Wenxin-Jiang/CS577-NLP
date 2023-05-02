---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_one500v9_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_One_500v9_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_one500v9_wikigold_split
      type: tagged_one500v9_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.7016183412002697
    - name: Recall
      type: recall
      value: 0.7011455525606469
    - name: F1
      type: f1
      value: 0.7013818672059319
    - name: Accuracy
      type: accuracy
      value: 0.9284582154955403
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_One_500v9_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_one500v9_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2469
- Precision: 0.7016
- Recall: 0.7011
- F1: 0.7014
- Accuracy: 0.9285

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
| No log        | 1.0   | 170  | 0.2908          | 0.5414    | 0.4538 | 0.4938 | 0.9011   |
| No log        | 2.0   | 340  | 0.2680          | 0.6629    | 0.6253 | 0.6436 | 0.9172   |
| 0.1121        | 3.0   | 510  | 0.2469          | 0.7016    | 0.7011 | 0.7014 | 0.9285   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
