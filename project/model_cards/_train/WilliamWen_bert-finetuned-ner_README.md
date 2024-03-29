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
      config: conll2003
      split: train
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9314616019818331
    - name: Recall
      type: recall
      value: 0.9491753618310333
    - name: F1
      type: f1
      value: 0.9402350587646913
    - name: Accuracy
      type: accuracy
      value: 0.9857243774651204
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0636
- Precision: 0.9315
- Recall: 0.9492
- F1: 0.9402
- Accuracy: 0.9857

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
| 0.0898        | 1.0   | 1756 | 0.0718          | 0.9149    | 0.9359 | 0.9253 | 0.9811   |
| 0.0351        | 2.0   | 3512 | 0.0641          | 0.9298    | 0.9490 | 0.9393 | 0.9860   |
| 0.0186        | 3.0   | 5268 | 0.0636          | 0.9315    | 0.9492 | 0.9402 | 0.9857   |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1
- Datasets 2.5.1
- Tokenizers 0.12.1
