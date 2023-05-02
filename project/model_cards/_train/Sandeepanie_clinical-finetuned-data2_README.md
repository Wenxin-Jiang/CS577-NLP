---
license: mit
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: clinical-finetuned-data2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinical-finetuned-data2

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4949
- F1: 0.7800

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
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.66          | 1.0   | 50   | 0.6269          | 0.6659 |
| 0.5476        | 2.0   | 100  | 0.5311          | 0.7615 |
| 0.3766        | 3.0   | 150  | 0.4457          | 0.7970 |
| 0.2785        | 4.0   | 200  | 0.5251          | 0.7615 |
| 0.2274        | 5.0   | 250  | 0.4949          | 0.7800 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
