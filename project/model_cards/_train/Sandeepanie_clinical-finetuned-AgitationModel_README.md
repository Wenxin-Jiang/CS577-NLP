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
- name: clinical-finetuned-AgitationModel
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# clinical-finetuned-AgitationModel

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9746
- Accuracy: 0.88
- Precision: 0.9178
- Recall: 0.9178
- F1: 0.9178

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
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.0949        | 1.0   | 50   | 1.0393          | 0.85     | 0.8816    | 0.9178 | 0.8993 |
| 0.0475        | 2.0   | 100  | 1.0619          | 0.85     | 0.8816    | 0.9178 | 0.8993 |
| 0.0149        | 3.0   | 150  | 0.9746          | 0.88     | 0.9178    | 0.9178 | 0.9178 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Tokenizers 0.12.1
