---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-32-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-32-2

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7136
- Accuracy: 0.679

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
| 1.1052        | 1.0   | 19   | 1.0726          | 0.45     |
| 1.0421        | 2.0   | 38   | 1.0225          | 0.5      |
| 0.9173        | 3.0   | 57   | 0.9164          | 0.6      |
| 0.6822        | 4.0   | 76   | 0.8251          | 0.7      |
| 0.4407        | 5.0   | 95   | 0.8908          | 0.5      |
| 0.2367        | 6.0   | 114  | 0.6772          | 0.75     |
| 0.1145        | 7.0   | 133  | 0.7792          | 0.65     |
| 0.0479        | 8.0   | 152  | 1.0657          | 0.6      |
| 0.0186        | 9.0   | 171  | 1.2228          | 0.65     |
| 0.0111        | 10.0  | 190  | 1.1100          | 0.6      |
| 0.0083        | 11.0  | 209  | 1.1991          | 0.65     |
| 0.0067        | 12.0  | 228  | 1.2654          | 0.65     |
| 0.0061        | 13.0  | 247  | 1.2837          | 0.65     |
| 0.0046        | 14.0  | 266  | 1.2860          | 0.6      |
| 0.0043        | 15.0  | 285  | 1.3160          | 0.65     |
| 0.0037        | 16.0  | 304  | 1.3323          | 0.65     |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
