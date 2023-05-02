---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- conll2003
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: distilbert-base-uncased-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: conll2003
      type: conll2003
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9273854328093868
    - name: Recall
      type: recall
      value: 0.9372413021590782
    - name: F1
      type: f1
      value: 0.9322873198686918
    - name: Accuracy
      type: accuracy
      value: 0.9840341874910639
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0599
- Precision: 0.9274
- Recall: 0.9372
- F1: 0.9323
- Accuracy: 0.9840

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
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.2378        | 1.0   | 878  | 0.0719          | 0.9107    | 0.9200 | 0.9154 | 0.9801   |
| 0.0509        | 2.0   | 1756 | 0.0620          | 0.9156    | 0.9311 | 0.9233 | 0.9821   |
| 0.0307        | 3.0   | 2634 | 0.0599          | 0.9274    | 0.9372 | 0.9323 | 0.9840   |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
