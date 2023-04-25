---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-16-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-16-2

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9210
- Accuracy: 0.5635

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
| 1.0915        | 1.0   | 10   | 1.1051          | 0.4      |
| 1.0663        | 2.0   | 20   | 1.0794          | 0.3      |
| 1.0307        | 3.0   | 30   | 1.0664          | 0.5      |
| 0.9443        | 4.0   | 40   | 1.0729          | 0.5      |
| 0.8373        | 5.0   | 50   | 1.0175          | 0.4      |
| 0.6892        | 6.0   | 60   | 0.9624          | 0.5      |
| 0.538         | 7.0   | 70   | 0.9924          | 0.5      |
| 0.4173        | 8.0   | 80   | 1.0136          | 0.6      |
| 0.1846        | 9.0   | 90   | 1.0683          | 0.6      |
| 0.1125        | 10.0  | 100  | 1.2376          | 0.6      |
| 0.0754        | 11.0  | 110  | 1.2537          | 0.6      |
| 0.0401        | 12.0  | 120  | 1.4387          | 0.6      |
| 0.0285        | 13.0  | 130  | 1.5702          | 0.6      |
| 0.0241        | 14.0  | 140  | 1.6795          | 0.6      |
| 0.0175        | 15.0  | 150  | 1.7228          | 0.6      |
| 0.0147        | 16.0  | 160  | 1.7892          | 0.6      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
