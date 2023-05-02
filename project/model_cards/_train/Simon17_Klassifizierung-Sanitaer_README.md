---
license: mit
tags:
- generated_from_trainer
metrics:
- f1
widget:
- text: "12064SAN101WAZW05"
- text: "11004SAN001AH01SM83"
- text: "11004SAN002DE02SM46"
- text: "11040HZG501WW01MT01"
- text: "Stör. Tauchpumpen fest"
model-index:
- name: Klassifizierung-Sanitaer
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Klassifizierung-Sanitaer

This model is a fine-tuned version of [bert-base-german-cased](https://huggingface.co/bert-base-german-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4922
- F1: 0.7374

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 1.4874        | 1.0   | 11   | 1.0656          | 0.6124 |
| 0.9892        | 2.0   | 22   | 0.6269          | 0.7374 |
| 0.5846        | 3.0   | 33   | 0.4922          | 0.7374 |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1
