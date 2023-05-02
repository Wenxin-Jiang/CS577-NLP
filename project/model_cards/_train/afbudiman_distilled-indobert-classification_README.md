---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- indonlu
metrics:
- accuracy
- f1
model-index:
- name: distilled-indobert-classification
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: indonlu
      type: indonlu
      args: smsa
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9015873015873016
    - name: F1
      type: f1
      value: 0.9014926755197933
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilled-indobert-classification

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the indonlu dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6015
- Accuracy: 0.9016
- F1: 0.9015

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 33
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 1.0427        | 1.0   | 688  | 0.6306          | 0.8683   | 0.8684 |
| 0.5332        | 2.0   | 1376 | 0.5621          | 0.8794   | 0.8779 |
| 0.3021        | 3.0   | 2064 | 0.6785          | 0.8905   | 0.8896 |
| 0.1851        | 4.0   | 2752 | 0.6085          | 0.8968   | 0.8959 |
| 0.1152        | 5.0   | 3440 | 0.6015          | 0.9016   | 0.9015 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
