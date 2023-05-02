---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_uni500v6_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_Uni_500v6_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_uni500v6_wikigold_split
      type: tagged_uni500v6_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.699155524278677
    - name: Recall
      type: recall
      value: 0.6986638537271449
    - name: F1
      type: f1
      value: 0.6989096025325361
    - name: Accuracy
      type: accuracy
      value: 0.9317908843795436
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_Uni_500v6_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_uni500v6_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2386
- Precision: 0.6992
- Recall: 0.6987
- F1: 0.6989
- Accuracy: 0.9318

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
| No log        | 1.0   | 182  | 0.2452          | 0.5956    | 0.5432 | 0.5682 | 0.9189   |
| No log        | 2.0   | 364  | 0.2571          | 0.6832    | 0.6354 | 0.6584 | 0.9204   |
| 0.1093        | 3.0   | 546  | 0.2386          | 0.6992    | 0.6987 | 0.6989 | 0.9318   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
