---
license: cc-by-4.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: hing-mbert-ours-run-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hing-mbert-ours-run-3

This model is a fine-tuned version of [l3cube-pune/hing-mbert](https://huggingface.co/l3cube-pune/hing-mbert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.9769
- Accuracy: 0.675
- Precision: 0.6433
- Recall: 0.6344
- F1: 0.6344

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.9089        | 1.0   | 100  | 1.0993          | 0.635    | 0.6487    | 0.5304 | 0.5060 |
| 0.6657        | 2.0   | 200  | 0.8138          | 0.645    | 0.6550    | 0.6482 | 0.6234 |
| 0.3858        | 3.0   | 300  | 1.1334          | 0.665    | 0.6162    | 0.6061 | 0.5995 |
| 0.208         | 4.0   | 400  | 1.9041          | 0.685    | 0.6488    | 0.6169 | 0.6087 |
| 0.0996        | 5.0   | 500  | 2.3735          | 0.645    | 0.5867    | 0.5781 | 0.5794 |
| 0.0296        | 6.0   | 600  | 2.5772          | 0.665    | 0.6284    | 0.6208 | 0.6198 |
| 0.0623        | 7.0   | 700  | 2.8906          | 0.655    | 0.6040    | 0.5916 | 0.5926 |
| 0.0395        | 8.0   | 800  | 2.6567          | 0.675    | 0.6279    | 0.6254 | 0.6219 |
| 0.029         | 9.0   | 900  | 2.9277          | 0.655    | 0.6208    | 0.5950 | 0.5991 |
| 0.0194        | 10.0  | 1000 | 2.7362          | 0.665    | 0.6241    | 0.6208 | 0.6190 |
| 0.0092        | 11.0  | 1100 | 2.5561          | 0.68     | 0.6396    | 0.6401 | 0.6385 |
| 0.0059        | 12.0  | 1200 | 3.1112          | 0.675    | 0.6350    | 0.5967 | 0.6042 |
| 0.0133        | 13.0  | 1300 | 2.5269          | 0.685    | 0.6520    | 0.6607 | 0.6519 |
| 0.0051        | 14.0  | 1400 | 2.8736          | 0.68     | 0.6381    | 0.6158 | 0.6134 |
| 0.0044        | 15.0  | 1500 | 2.9132          | 0.675    | 0.6336    | 0.6180 | 0.6200 |
| 0.0029        | 16.0  | 1600 | 2.8701          | 0.675    | 0.6337    | 0.6214 | 0.6233 |
| 0.0015        | 17.0  | 1700 | 2.8115          | 0.69     | 0.6475    | 0.6388 | 0.6420 |
| 0.0019        | 18.0  | 1800 | 2.9517          | 0.67     | 0.6373    | 0.6276 | 0.6273 |
| 0.0013        | 19.0  | 1900 | 2.9633          | 0.67     | 0.6373    | 0.6276 | 0.6273 |
| 0.0007        | 20.0  | 2000 | 2.9769          | 0.675    | 0.6433    | 0.6344 | 0.6344 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Tokenizers 0.13.2
