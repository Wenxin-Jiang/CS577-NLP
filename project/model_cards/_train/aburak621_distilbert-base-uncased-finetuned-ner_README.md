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
      config: conll2003
      split: train
      args: conll2003
    metrics:
    - name: Precision
      type: precision
      value: 0.9356089992242048
    - name: Recall
      type: recall
      value: 0.9444009397024276
    - name: F1
      type: f1
      value: 0.9399844115354637
    - name: Accuracy
      type: accuracy
      value: 0.9851303477528714
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-ner

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the conll2003 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0645
- Precision: 0.9356
- Recall: 0.9444
- F1: 0.9400
- Accuracy: 0.9851

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.2464        | 1.0   | 878  | 0.0679          | 0.9223    | 0.9248 | 0.9236 | 0.9818   |
| 0.0526        | 2.0   | 1756 | 0.0574          | 0.9290    | 0.9367 | 0.9328 | 0.9837   |
| 0.0274        | 3.0   | 2634 | 0.0594          | 0.9282    | 0.9400 | 0.9341 | 0.9843   |
| 0.0173        | 4.0   | 3512 | 0.0617          | 0.9349    | 0.9428 | 0.9388 | 0.9851   |
| 0.0119        | 5.0   | 4390 | 0.0645          | 0.9356    | 0.9444 | 0.9400 | 0.9851   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cpu
- Datasets 2.8.0
- Tokenizers 0.13.2
