---
tags:
- generated_from_trainer
model-index:
- name: librispeech-semi-supervised-without-LM
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# librispeech-semi-supervised-without-LM

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1837
- Wer: 0.0580

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 15
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 0.0565        | 0.56  | 1000  | 0.1354          | 0.0641 |
| 0.0548        | 1.12  | 2000  | 0.1320          | 0.0628 |
| 0.0478        | 1.68  | 3000  | 0.1247          | 0.0612 |
| 0.0451        | 2.24  | 4000  | 0.1256          | 0.0613 |
| 0.0401        | 2.8   | 5000  | 0.1269          | 0.0606 |
| 0.035         | 3.36  | 6000  | 0.1370          | 0.0595 |
| 0.0344        | 3.92  | 7000  | 0.1280          | 0.0589 |
| 0.031         | 4.48  | 8000  | 0.1350          | 0.0589 |
| 0.031         | 5.04  | 9000  | 0.1418          | 0.0614 |
| 0.0278        | 5.61  | 10000 | 0.1382          | 0.0604 |
| 0.0272        | 6.17  | 11000 | 0.1502          | 0.0615 |
| 0.0246        | 6.73  | 12000 | 0.1443          | 0.0609 |
| 0.0233        | 7.29  | 13000 | 0.1548          | 0.0589 |
| 0.0224        | 7.85  | 14000 | 0.1547          | 0.0599 |
| 0.0202        | 8.41  | 15000 | 0.1570          | 0.0590 |
| 0.0199        | 8.97  | 16000 | 0.1564          | 0.0594 |
| 0.0186        | 9.53  | 17000 | 0.1598          | 0.0595 |
| 0.0187        | 10.09 | 18000 | 0.1657          | 0.0585 |
| 0.017         | 10.65 | 19000 | 0.1690          | 0.0584 |
| 0.016         | 11.21 | 20000 | 0.1689          | 0.0588 |
| 0.0156        | 11.77 | 21000 | 0.1745          | 0.0585 |
| 0.0151        | 12.33 | 22000 | 0.1777          | 0.0583 |
| 0.0144        | 12.89 | 23000 | 0.1778          | 0.0590 |
| 0.0142        | 13.45 | 24000 | 0.1803          | 0.0585 |
| 0.0137        | 14.01 | 25000 | 0.1796          | 0.0581 |
| 0.0132        | 14.57 | 26000 | 0.1837          | 0.0580 |


### Framework versions

- Transformers 4.14.1
- Pytorch 1.10.2
- Datasets 1.18.2
- Tokenizers 0.10.3
