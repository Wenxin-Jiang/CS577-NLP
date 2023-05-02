---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-8-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-8-2

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6794
- Accuracy: 0.6063

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.6942        | 1.0   | 3    | 0.7940          | 0.25     |
| 0.6068        | 2.0   | 6    | 0.9326          | 0.25     |
| 0.6553        | 3.0   | 9    | 0.7979          | 0.25     |
| 0.475         | 4.0   | 12   | 0.7775          | 0.25     |
| 0.377         | 5.0   | 15   | 0.7477          | 0.25     |
| 0.3176        | 6.0   | 18   | 0.6856          | 0.75     |
| 0.2708        | 7.0   | 21   | 0.6554          | 0.75     |
| 0.2855        | 8.0   | 24   | 0.8129          | 0.5      |
| 0.148         | 9.0   | 27   | 0.7074          | 0.75     |
| 0.0947        | 10.0  | 30   | 0.7090          | 0.75     |
| 0.049         | 11.0  | 33   | 0.7885          | 0.75     |
| 0.0252        | 12.0  | 36   | 0.9203          | 0.75     |
| 0.0165        | 13.0  | 39   | 1.0937          | 0.75     |
| 0.0084        | 14.0  | 42   | 1.2502          | 0.75     |
| 0.0059        | 15.0  | 45   | 1.3726          | 0.75     |
| 0.0037        | 16.0  | 48   | 1.4784          | 0.75     |
| 0.003         | 17.0  | 51   | 1.5615          | 0.75     |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
