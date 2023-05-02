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
- name: bert-finetuned-pos
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
      value: 0.9347682119205298
    - name: Recall
      type: recall
      value: 0.9501851228542578
    - name: F1
      type: f1
      value: 0.9424136204306459
    - name: Accuracy
      type: accuracy
      value: 0.9867840113027609
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-pos

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0580
- Precision: 0.9348
- Recall: 0.9502
- F1: 0.9424
- Accuracy: 0.9868

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
| 0.0875        | 1.0   | 1756 | 0.0680          | 0.9158    | 0.9352 | 0.9254 | 0.9826   |
| 0.0321        | 2.0   | 3512 | 0.0611          | 0.9289    | 0.9448 | 0.9368 | 0.9856   |
| 0.0222        | 3.0   | 5268 | 0.0580          | 0.9348    | 0.9502 | 0.9424 | 0.9868   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0
- Datasets 2.0.0
- Tokenizers 0.11.6
