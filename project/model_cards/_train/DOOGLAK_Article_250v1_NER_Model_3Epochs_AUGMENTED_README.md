---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article250v1_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_250v1_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article250v1_wikigold_split
      type: article250v1_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.6698863636363637
    - name: Recall
      type: recall
      value: 0.665725578769057
    - name: F1
      type: f1
      value: 0.6677994902293968
    - name: Accuracy
      type: accuracy
      value: 0.9256427192358501
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_250v1_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article250v1_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2324
- Precision: 0.6699
- Recall: 0.6657
- F1: 0.6678
- Accuracy: 0.9256

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
| No log        | 1.0   | 94   | 0.2546          | 0.5933    | 0.5539 | 0.5729 | 0.9127   |
| No log        | 2.0   | 188  | 0.2337          | 0.6564    | 0.6629 | 0.6596 | 0.9242   |
| No log        | 3.0   | 282  | 0.2324          | 0.6699    | 0.6657 | 0.6678 | 0.9256   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
