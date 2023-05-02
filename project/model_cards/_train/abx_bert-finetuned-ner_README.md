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
- name: bert-finetuned-ner
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
      value: 0.9341713529606351
    - name: Recall
      type: recall
      value: 0.9505217098619994
    - name: F1
      type: f1
      value: 0.9422756089422756
    - name: Accuracy
      type: accuracy
      value: 0.9861070230176017
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0623
- Precision: 0.9342
- Recall: 0.9505
- F1: 0.9423
- Accuracy: 0.9861

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
| 0.0865        | 1.0   | 1756 | 0.0667          | 0.9166    | 0.9379 | 0.9271 | 0.9829   |
| 0.0397        | 2.0   | 3512 | 0.0560          | 0.9337    | 0.9522 | 0.9428 | 0.9867   |
| 0.0194        | 3.0   | 5268 | 0.0623          | 0.9342    | 0.9505 | 0.9423 | 0.9861   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu116
- Datasets 2.3.2
- Tokenizers 0.12.1
