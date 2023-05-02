---
license: cc-by-nc-sa-4.0
tags:
- generated_from_trainer
datasets:
- cord-layoutlmv3
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: layoutlmv3-finetuned-cord_100
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: cord-layoutlmv3
      type: cord-layoutlmv3
      config: cord
      split: train
      args: cord
    metrics:
    - name: Precision
      type: precision
      value: 0.9478778853313478
    - name: Recall
      type: recall
      value: 0.9528443113772455
    - name: F1
      type: f1
      value: 0.950354609929078
    - name: Accuracy
      type: accuracy
      value: 0.9541595925297114
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlmv3-finetuned-cord_100

This model is a fine-tuned version of [microsoft/layoutlmv3-base](https://huggingface.co/microsoft/layoutlmv3-base) on the cord-layoutlmv3 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2176
- Precision: 0.9479
- Recall: 0.9528
- F1: 0.9504
- Accuracy: 0.9542

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 5
- eval_batch_size: 5
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 2500

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.56  | 250  | 1.0378          | 0.7404    | 0.7964 | 0.7674 | 0.8035   |
| 1.4104        | 3.12  | 500  | 0.5605          | 0.8291    | 0.8645 | 0.8465 | 0.8790   |
| 1.4104        | 4.69  | 750  | 0.3959          | 0.8728    | 0.8990 | 0.8857 | 0.9155   |
| 0.4054        | 6.25  | 1000 | 0.3111          | 0.9231    | 0.9349 | 0.9290 | 0.9393   |
| 0.4054        | 7.81  | 1250 | 0.2847          | 0.9135    | 0.9251 | 0.9193 | 0.9317   |
| 0.2124        | 9.38  | 1500 | 0.2457          | 0.9281    | 0.9379 | 0.9330 | 0.9410   |
| 0.2124        | 10.94 | 1750 | 0.2390          | 0.9371    | 0.9484 | 0.9427 | 0.9520   |
| 0.1438        | 12.5  | 2000 | 0.2196          | 0.9443    | 0.9513 | 0.9478 | 0.9546   |
| 0.1438        | 14.06 | 2250 | 0.2182          | 0.9478    | 0.9521 | 0.9500 | 0.9533   |
| 0.1093        | 15.62 | 2500 | 0.2176          | 0.9479    | 0.9528 | 0.9504 | 0.9542   |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1
