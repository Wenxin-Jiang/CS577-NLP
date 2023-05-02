---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-32-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-32-4

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7384
- Accuracy: 0.724

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
| 1.1013        | 1.0   | 19   | 1.0733          | 0.55     |
| 1.0226        | 2.0   | 38   | 1.0064          | 0.65     |
| 0.8539        | 3.0   | 57   | 0.8758          | 0.75     |
| 0.584         | 4.0   | 76   | 0.6941          | 0.7      |
| 0.2813        | 5.0   | 95   | 0.5151          | 0.7      |
| 0.1122        | 6.0   | 114  | 0.4351          | 0.8      |
| 0.0432        | 7.0   | 133  | 0.4896          | 0.85     |
| 0.0199        | 8.0   | 152  | 0.5391          | 0.85     |
| 0.0126        | 9.0   | 171  | 0.5200          | 0.85     |
| 0.0085        | 10.0  | 190  | 0.5622          | 0.85     |
| 0.0069        | 11.0  | 209  | 0.5950          | 0.85     |
| 0.0058        | 12.0  | 228  | 0.6015          | 0.85     |
| 0.0053        | 13.0  | 247  | 0.6120          | 0.85     |
| 0.0042        | 14.0  | 266  | 0.6347          | 0.85     |
| 0.0039        | 15.0  | 285  | 0.6453          | 0.85     |
| 0.0034        | 16.0  | 304  | 0.6660          | 0.85     |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
