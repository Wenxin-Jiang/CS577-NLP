---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-16-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-16-1

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0424
- Accuracy: 0.5355

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
| 1.0989        | 1.0   | 10   | 1.1049          | 0.1      |
| 1.0641        | 2.0   | 20   | 1.0768          | 0.3      |
| 0.9742        | 3.0   | 30   | 1.0430          | 0.4      |
| 0.8765        | 4.0   | 40   | 1.0058          | 0.4      |
| 0.6979        | 5.0   | 50   | 0.8488          | 0.7      |
| 0.563         | 6.0   | 60   | 0.7221          | 0.7      |
| 0.4135        | 7.0   | 70   | 0.6587          | 0.8      |
| 0.2509        | 8.0   | 80   | 0.5577          | 0.7      |
| 0.0943        | 9.0   | 90   | 0.5840          | 0.7      |
| 0.0541        | 10.0  | 100  | 0.6959          | 0.7      |
| 0.0362        | 11.0  | 110  | 0.6884          | 0.6      |
| 0.0254        | 12.0  | 120  | 0.9263          | 0.6      |
| 0.0184        | 13.0  | 130  | 0.7992          | 0.6      |
| 0.0172        | 14.0  | 140  | 0.7351          | 0.6      |
| 0.0131        | 15.0  | 150  | 0.7664          | 0.6      |
| 0.0117        | 16.0  | 160  | 0.8262          | 0.6      |
| 0.0101        | 17.0  | 170  | 0.8839          | 0.6      |
| 0.0089        | 18.0  | 180  | 0.9018          | 0.6      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
