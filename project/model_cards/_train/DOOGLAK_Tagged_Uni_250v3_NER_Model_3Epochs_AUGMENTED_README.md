---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tagged_uni250v3_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Tagged_Uni_250v3_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: tagged_uni250v3_wikigold_split
      type: tagged_uni250v3_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.5830763960260363
    - name: Recall
      type: recall
      value: 0.4849002849002849
    - name: F1
      type: f1
      value: 0.5294758127235961
    - name: Accuracy
      type: accuracy
      value: 0.8988582871706847
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Tagged_Uni_250v3_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the tagged_uni250v3_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3093
- Precision: 0.5831
- Recall: 0.4849
- F1: 0.5295
- Accuracy: 0.8989

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
| No log        | 1.0   | 78   | 0.3468          | 0.3486    | 0.2362 | 0.2816 | 0.8670   |
| No log        | 2.0   | 156  | 0.3071          | 0.5484    | 0.4516 | 0.4953 | 0.8943   |
| No log        | 3.0   | 234  | 0.3093          | 0.5831    | 0.4849 | 0.5295 | 0.8989   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
