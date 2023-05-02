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
- name: distilbert-base-uncased_ner_conll2003
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
      value: 0.9357583847822459
    - name: Recall
      type: recall
      value: 0.9437899697071693
    - name: F1
      type: f1
      value: 0.939757017176372
    - name: Accuracy
      type: accuracy
      value: 0.987675713562556
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased_ner_conll2003

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0524
- Precision: 0.9358
- Recall: 0.9438
- F1: 0.9398
- Accuracy: 0.9877

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
| 0.1897        | 1.0   | 878  | 0.0544          | 0.9223    | 0.9270 | 0.9246 | 0.9848   |
| 0.0363        | 2.0   | 1756 | 0.0486          | 0.9316    | 0.9391 | 0.9353 | 0.9869   |
| 0.0194        | 3.0   | 2634 | 0.0496          | 0.9369    | 0.9403 | 0.9386 | 0.9873   |
| 0.0114        | 4.0   | 3512 | 0.0526          | 0.9340    | 0.9436 | 0.9388 | 0.9875   |
| 0.0089        | 5.0   | 4390 | 0.0524          | 0.9358    | 0.9438 | 0.9398 | 0.9877   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
