---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- accuracy
model-index:
- name: beit-base-patch16-224-pt22k-ft22k-rim_one-new
  results:
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      type: rimonedl
      name: RIM ONE DL
      split: test
    metrics:
    - type: f1
      value: 0.9197860962566845
      name: F1
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      type: rim one
      name: RIMONEDL
      split: test
    metrics:
    - type: precision
      value: 0.9247311827956989
      name: precision
    - type: recall
      value: 0.9148936170212766
      name: Recall
    - type: accuracy
      value: 0.8972602739726028
      name: Accuracy
    - type: roc_auc
      value: 0.8901391162029461
      name: AUC
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# beit-base-patch16-224-pt22k-ft22k-rim_one-new

This model is a fine-tuned version of [microsoft/beit-base-patch16-224-pt22k-ft22k](https://huggingface.co/microsoft/beit-base-patch16-224-pt22k-ft22k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4550
- Accuracy: 0.8767

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 0.73  | 2    | 0.2411          | 0.9178   |
| No log        | 1.73  | 4    | 0.2182          | 0.8973   |
| No log        | 2.73  | 6    | 0.3085          | 0.8973   |
| No log        | 3.73  | 8    | 0.2794          | 0.8973   |
| 0.1392        | 4.73  | 10   | 0.2398          | 0.9110   |
| 0.1392        | 5.73  | 12   | 0.2925          | 0.8973   |
| 0.1392        | 6.73  | 14   | 0.2798          | 0.9110   |
| 0.1392        | 7.73  | 16   | 0.2184          | 0.9178   |
| 0.1392        | 8.73  | 18   | 0.3007          | 0.9110   |
| 0.0416        | 9.73  | 20   | 0.3344          | 0.9041   |
| 0.0416        | 10.73 | 22   | 0.3626          | 0.9110   |
| 0.0416        | 11.73 | 24   | 0.4842          | 0.8904   |
| 0.0416        | 12.73 | 26   | 0.3664          | 0.8973   |
| 0.0416        | 13.73 | 28   | 0.3458          | 0.9110   |
| 0.0263        | 14.73 | 30   | 0.2810          | 0.9110   |
| 0.0263        | 15.73 | 32   | 0.4695          | 0.8699   |
| 0.0263        | 16.73 | 34   | 0.3723          | 0.9041   |
| 0.0263        | 17.73 | 36   | 0.3447          | 0.9041   |
| 0.0263        | 18.73 | 38   | 0.3708          | 0.8904   |
| 0.0264        | 19.73 | 40   | 0.4052          | 0.9110   |
| 0.0264        | 20.73 | 42   | 0.4492          | 0.9041   |
| 0.0264        | 21.73 | 44   | 0.4649          | 0.8904   |
| 0.0264        | 22.73 | 46   | 0.4061          | 0.9178   |
| 0.0264        | 23.73 | 48   | 0.4136          | 0.9110   |
| 0.0139        | 24.73 | 50   | 0.4183          | 0.8973   |
| 0.0139        | 25.73 | 52   | 0.4504          | 0.8904   |
| 0.0139        | 26.73 | 54   | 0.4368          | 0.8973   |
| 0.0139        | 27.73 | 56   | 0.4711          | 0.9110   |
| 0.0139        | 28.73 | 58   | 0.3928          | 0.9110   |
| 0.005         | 29.73 | 60   | 0.4550          | 0.8767   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
