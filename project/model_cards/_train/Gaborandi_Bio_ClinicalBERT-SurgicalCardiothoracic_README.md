---
license: mit
tags:
- generated_from_trainer
model-index:
- name: Bio_ClinicalBERT-SurgicalCardiothoracic
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Bio_ClinicalBERT-SurgicalCardiothoracic

This model is a fine-tuned version of [emilyalsentzer/Bio_ClinicalBERT](https://huggingface.co/emilyalsentzer/Bio_ClinicalBERT) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8426

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
- train_batch_size: 1
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| No log        | 1.0   | 13144 | 0.9092          |
| No log        | 2.0   | 26288 | 0.8575          |
| No log        | 3.0   | 39432 | 0.8417          |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.8.0
- Datasets 2.2.2
- Tokenizers 0.11.6
