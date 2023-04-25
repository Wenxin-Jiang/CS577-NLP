---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-32-0
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-32-0

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7714
- Accuracy: 0.705

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
| 1.0871        | 1.0   | 19   | 1.0704          | 0.45     |
| 1.0019        | 2.0   | 38   | 1.0167          | 0.55     |
| 0.8412        | 3.0   | 57   | 0.9134          | 0.55     |
| 0.6047        | 4.0   | 76   | 0.8430          | 0.6      |
| 0.3746        | 5.0   | 95   | 0.8315          | 0.6      |
| 0.1885        | 6.0   | 114  | 0.8585          | 0.6      |
| 0.0772        | 7.0   | 133  | 0.9443          | 0.65     |
| 0.0312        | 8.0   | 152  | 1.1019          | 0.65     |
| 0.0161        | 9.0   | 171  | 1.1420          | 0.65     |
| 0.0102        | 10.0  | 190  | 1.2773          | 0.65     |
| 0.0077        | 11.0  | 209  | 1.2454          | 0.65     |
| 0.0064        | 12.0  | 228  | 1.2785          | 0.65     |
| 0.006         | 13.0  | 247  | 1.3834          | 0.65     |
| 0.0045        | 14.0  | 266  | 1.4139          | 0.65     |
| 0.0043        | 15.0  | 285  | 1.4056          | 0.65     |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
