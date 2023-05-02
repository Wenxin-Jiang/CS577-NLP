---
tags:
- generated_from_trainer
datasets:
- indonlu
metrics:
- accuracy
- f1
model-index:
- name: distilled-optimized-indobert-classification
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
      value: 0.9
    - name: F1
      type: f1
      value: 0.8994069293432798
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilled-optimized-indobert-classification

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the indonlu dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7397
- Accuracy: 0.9
- F1: 0.8994

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4.315104717136378e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 33
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 9

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.128         | 1.0   | 688  | 0.8535          | 0.8913   | 0.8917 |
| 0.1475        | 2.0   | 1376 | 0.9171          | 0.8913   | 0.8913 |
| 0.0997        | 3.0   | 2064 | 0.7799          | 0.8960   | 0.8951 |
| 0.0791        | 4.0   | 2752 | 0.7179          | 0.9032   | 0.9023 |
| 0.0577        | 5.0   | 3440 | 0.6908          | 0.9063   | 0.9055 |
| 0.0406        | 6.0   | 4128 | 0.7613          | 0.8992   | 0.8986 |
| 0.0275        | 7.0   | 4816 | 0.7502          | 0.8992   | 0.8989 |
| 0.023         | 8.0   | 5504 | 0.7408          | 0.8976   | 0.8969 |
| 0.0169        | 9.0   | 6192 | 0.7397          | 0.9      | 0.8994 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1
