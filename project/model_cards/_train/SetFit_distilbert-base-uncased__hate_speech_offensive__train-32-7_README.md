---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-32-7
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-32-7

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8210
- Accuracy: 0.6305

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
| 1.0989        | 1.0   | 19   | 1.0655          | 0.4      |
| 1.0102        | 2.0   | 38   | 0.9927          | 0.6      |
| 0.8063        | 3.0   | 57   | 0.9117          | 0.5      |
| 0.5284        | 4.0   | 76   | 0.8058          | 0.55     |
| 0.2447        | 5.0   | 95   | 0.8393          | 0.45     |
| 0.098         | 6.0   | 114  | 0.8438          | 0.6      |
| 0.0388        | 7.0   | 133  | 1.1901          | 0.45     |
| 0.0188        | 8.0   | 152  | 1.4429          | 0.45     |
| 0.0121        | 9.0   | 171  | 1.3648          | 0.4      |
| 0.0082        | 10.0  | 190  | 1.4768          | 0.4      |
| 0.0066        | 11.0  | 209  | 1.4830          | 0.45     |
| 0.0057        | 12.0  | 228  | 1.4936          | 0.45     |
| 0.0053        | 13.0  | 247  | 1.5649          | 0.4      |
| 0.0041        | 14.0  | 266  | 1.6306          | 0.4      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
