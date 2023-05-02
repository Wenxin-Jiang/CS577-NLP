---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-8-6
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-8-6

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1275
- Accuracy: 0.3795

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
| 1.11          | 1.0   | 5    | 1.1184          | 0.0      |
| 1.0608        | 2.0   | 10   | 1.1227          | 0.0      |
| 1.0484        | 3.0   | 15   | 1.1009          | 0.2      |
| 0.9614        | 4.0   | 20   | 1.1009          | 0.2      |
| 0.8545        | 5.0   | 25   | 1.0772          | 0.2      |
| 0.8241        | 6.0   | 30   | 1.0457          | 0.2      |
| 0.708         | 7.0   | 35   | 1.0301          | 0.4      |
| 0.5045        | 8.0   | 40   | 1.0325          | 0.4      |
| 0.4175        | 9.0   | 45   | 1.0051          | 0.4      |
| 0.3446        | 10.0  | 50   | 0.9610          | 0.4      |
| 0.2851        | 11.0  | 55   | 0.9954          | 0.4      |
| 0.1808        | 12.0  | 60   | 1.0561          | 0.4      |
| 0.1435        | 13.0  | 65   | 1.0218          | 0.4      |
| 0.1019        | 14.0  | 70   | 1.0254          | 0.4      |
| 0.0908        | 15.0  | 75   | 0.9935          | 0.4      |
| 0.0591        | 16.0  | 80   | 1.0090          | 0.4      |
| 0.0512        | 17.0  | 85   | 1.0884          | 0.4      |
| 0.0397        | 18.0  | 90   | 1.2732          | 0.4      |
| 0.039         | 19.0  | 95   | 1.2979          | 0.6      |
| 0.0325        | 20.0  | 100  | 1.2705          | 0.4      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
