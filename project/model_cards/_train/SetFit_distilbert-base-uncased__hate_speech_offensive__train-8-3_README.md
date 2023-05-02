---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-8-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-8-3

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9681
- Accuracy: 0.549

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
| 1.1073        | 1.0   | 5    | 1.1393          | 0.0      |
| 1.0392        | 2.0   | 10   | 1.1729          | 0.0      |
| 1.0302        | 3.0   | 15   | 1.1694          | 0.2      |
| 0.9176        | 4.0   | 20   | 1.1846          | 0.2      |
| 0.8339        | 5.0   | 25   | 1.1663          | 0.2      |
| 0.7533        | 6.0   | 30   | 1.1513          | 0.4      |
| 0.6327        | 7.0   | 35   | 1.1474          | 0.4      |
| 0.4402        | 8.0   | 40   | 1.1385          | 0.4      |
| 0.3752        | 9.0   | 45   | 1.0965          | 0.2      |
| 0.3448        | 10.0  | 50   | 1.0357          | 0.2      |
| 0.2582        | 11.0  | 55   | 1.0438          | 0.2      |
| 0.1903        | 12.0  | 60   | 1.0561          | 0.2      |
| 0.1479        | 13.0  | 65   | 1.0569          | 0.2      |
| 0.1129        | 14.0  | 70   | 1.0455          | 0.2      |
| 0.1071        | 15.0  | 75   | 1.0416          | 0.4      |
| 0.0672        | 16.0  | 80   | 1.1164          | 0.4      |
| 0.0561        | 17.0  | 85   | 1.1846          | 0.6      |
| 0.0463        | 18.0  | 90   | 1.2040          | 0.6      |
| 0.0431        | 19.0  | 95   | 1.2078          | 0.6      |
| 0.0314        | 20.0  | 100  | 1.2368          | 0.6      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
