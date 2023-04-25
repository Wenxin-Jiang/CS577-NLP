---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-16-6
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-16-6

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8331
- Accuracy: 0.625

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
| 1.0881        | 1.0   | 10   | 1.1248          | 0.1      |
| 1.0586        | 2.0   | 20   | 1.1162          | 0.2      |
| 0.9834        | 3.0   | 30   | 1.1199          | 0.3      |
| 0.9271        | 4.0   | 40   | 1.0740          | 0.3      |
| 0.7663        | 5.0   | 50   | 1.0183          | 0.5      |
| 0.6042        | 6.0   | 60   | 1.0259          | 0.5      |
| 0.4482        | 7.0   | 70   | 0.8699          | 0.7      |
| 0.3072        | 8.0   | 80   | 1.0615          | 0.5      |
| 0.1458        | 9.0   | 90   | 1.0164          | 0.5      |
| 0.0838        | 10.0  | 100  | 1.0620          | 0.5      |
| 0.055         | 11.0  | 110  | 1.1829          | 0.5      |
| 0.0347        | 12.0  | 120  | 1.2815          | 0.4      |
| 0.0244        | 13.0  | 130  | 1.2607          | 0.6      |
| 0.0213        | 14.0  | 140  | 1.3695          | 0.5      |
| 0.0169        | 15.0  | 150  | 1.4397          | 0.5      |
| 0.0141        | 16.0  | 160  | 1.4388          | 0.6      |
| 0.0122        | 17.0  | 170  | 1.4242          | 0.6      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
