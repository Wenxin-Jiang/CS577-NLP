---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
metrics:
- f1
model-index:
- name: vit-base-riego
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: imagefolder
      type: imagefolder
      config: MaxP--agro_riego
      split: test
      args: MaxP--agro_riego
    metrics:
    - name: F1
      type: f1
      value: 0.37288135593220334
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-base-riego

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the imagefolder dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2998
- F1: 0.3729

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 16
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.1696        | 0.79  | 100  | 1.1385          | 0.352  |
| 0.08          | 1.59  | 200  | 0.9071          | 0.3774 |
| 0.0928        | 2.38  | 300  | 1.1181          | 0.3454 |
| 0.0189        | 3.17  | 400  | 0.8262          | 0.3425 |
| 0.0728        | 3.97  | 500  | 0.9647          | 0.3747 |
| 0.0756        | 4.76  | 600  | 0.6097          | 0.4776 |
| 0.0018        | 5.56  | 700  | 1.3900          | 0.3652 |
| 0.002         | 6.35  | 800  | 0.7498          | 0.4606 |
| 0.0304        | 7.14  | 900  | 1.4367          | 0.3666 |
| 0.0024        | 7.94  | 1000 | 1.5714          | 0.3041 |
| 0.0463        | 8.73  | 1100 | 0.8038          | 0.4016 |
| 0.0014        | 9.52  | 1200 | 0.7175          | 0.4795 |
| 0.0015        | 10.32 | 1300 | 1.0347          | 0.3959 |
| 0.0009        | 11.11 | 1400 | 1.3881          | 0.3670 |
| 0.0131        | 11.9  | 1500 | 1.0780          | 0.4044 |
| 0.0007        | 12.7  | 1600 | 0.9834          | 0.4255 |
| 0.0011        | 13.49 | 1700 | 1.0753          | 0.4033 |
| 0.0007        | 14.29 | 1800 | 1.1514          | 0.3989 |
| 0.0007        | 15.08 | 1900 | 1.2373          | 0.3769 |
| 0.0007        | 15.87 | 2000 | 1.2998          | 0.3729 |


### Framework versions

- Transformers 4.26.1
- Pytorch 1.13.1+cu116
- Datasets 2.10.1
- Tokenizers 0.13.2
