---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-16-8
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-16-8

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0704
- Accuracy: 0.394

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
| 1.1031        | 1.0   | 10   | 1.1286          | 0.1      |
| 1.0648        | 2.0   | 20   | 1.1157          | 0.3      |
| 0.9982        | 3.0   | 30   | 1.1412          | 0.2      |
| 0.9283        | 4.0   | 40   | 1.2053          | 0.2      |
| 0.7958        | 5.0   | 50   | 1.1466          | 0.2      |
| 0.6668        | 6.0   | 60   | 1.1783          | 0.3      |
| 0.5068        | 7.0   | 70   | 1.2992          | 0.3      |
| 0.3741        | 8.0   | 80   | 1.3483          | 0.3      |
| 0.1653        | 9.0   | 90   | 1.4533          | 0.2      |
| 0.0946        | 10.0  | 100  | 1.6292          | 0.2      |
| 0.0569        | 11.0  | 110  | 1.8381          | 0.2      |
| 0.0346        | 12.0  | 120  | 2.0781          | 0.2      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
