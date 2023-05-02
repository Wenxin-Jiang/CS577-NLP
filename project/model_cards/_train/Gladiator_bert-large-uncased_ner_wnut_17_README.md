---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wnut_17
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-large-uncased_ner_wnut_17
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: wnut_17
      type: wnut_17
      args: wnut_17
    metrics:
    - name: Precision
      type: precision
      value: 0.7052785923753666
    - name: Recall
      type: recall
      value: 0.5753588516746412
    - name: F1
      type: f1
      value: 0.6337285902503295
    - name: Accuracy
      type: accuracy
      value: 0.9602644796236252
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-large-uncased_ner_wnut_17

This model is a fine-tuned version of [bert-large-uncased](https://huggingface.co/bert-large-uncased) on the wnut_17 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2516
- Precision: 0.7053
- Recall: 0.5754
- F1: 0.6337
- Accuracy: 0.9603

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 213  | 0.2143          | 0.6353    | 0.4605 | 0.5340 | 0.9490   |
| No log        | 2.0   | 426  | 0.2299          | 0.7322    | 0.5036 | 0.5967 | 0.9556   |
| 0.1489        | 3.0   | 639  | 0.2137          | 0.6583    | 0.5945 | 0.6248 | 0.9603   |
| 0.1489        | 4.0   | 852  | 0.2494          | 0.7035    | 0.5789 | 0.6352 | 0.9604   |
| 0.0268        | 5.0   | 1065 | 0.2516          | 0.7053    | 0.5754 | 0.6337 | 0.9603   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
