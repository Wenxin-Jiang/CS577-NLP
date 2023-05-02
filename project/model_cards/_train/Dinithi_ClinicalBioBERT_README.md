---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: ClinicalBioBERT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ClinicalBioBERT

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9404
- Accuracy: 0.77
- Precision: 0.8333
- Recall: 0.8209
- F1: 0.8271

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
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.693         | 1.0   | 50   | 0.6142          | 0.61     | 0.8182    | 0.5373 | 0.6486 |
| 0.5547        | 2.0   | 100  | 0.5753          | 0.66     | 0.8367    | 0.6119 | 0.7069 |
| 0.3912        | 3.0   | 150  | 0.5167          | 0.8      | 0.8406    | 0.8657 | 0.8529 |
| 0.2618        | 4.0   | 200  | 0.6664          | 0.8      | 0.8133    | 0.9104 | 0.8592 |
| 0.1648        | 5.0   | 250  | 0.5954          | 0.79     | 0.8594    | 0.8209 | 0.8397 |
| 0.1446        | 6.0   | 300  | 0.6131          | 0.81     | 0.8871    | 0.8209 | 0.8527 |
| 0.0841        | 7.0   | 350  | 0.8966          | 0.79     | 0.8194    | 0.8806 | 0.8489 |
| 0.0708        | 8.0   | 400  | 0.9366          | 0.78     | 0.8169    | 0.8657 | 0.8406 |
| 0.049         | 9.0   | 450  | 0.9523          | 0.78     | 0.8358    | 0.8358 | 0.8358 |
| 0.0516        | 10.0  | 500  | 0.9404          | 0.77     | 0.8333    | 0.8209 | 0.8271 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
