---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- article250v5_wikigold_split
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Article_250v5_NER_Model_3Epochs_AUGMENTED
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: article250v5_wikigold_split
      type: article250v5_wikigold_split
      args: default
    metrics:
    - name: Precision
      type: precision
      value: 0.6723730814639906
    - name: Recall
      type: recall
      value: 0.6475270039795338
    - name: F1
      type: f1
      value: 0.6597161888213148
    - name: Accuracy
      type: accuracy
      value: 0.927727249370536
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Article_250v5_NER_Model_3Epochs_AUGMENTED

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the article250v5_wikigold_split dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2378
- Precision: 0.6724
- Recall: 0.6475
- F1: 0.6597
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
| No log        | 1.0   | 101  | 0.2402          | 0.5235    | 0.5003 | 0.5116 | 0.9157   |
| No log        | 2.0   | 202  | 0.2579          | 0.6314    | 0.6043 | 0.6176 | 0.9189   |
| No log        | 3.0   | 303  | 0.2378          | 0.6724    | 0.6475 | 0.6597 | 0.9277   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.11.6
