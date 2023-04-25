---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-32-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-32-1

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0606
- Accuracy: 0.4745

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
| 1.0941        | 1.0   | 19   | 1.1045          | 0.2      |
| 0.9967        | 2.0   | 38   | 1.1164          | 0.35     |
| 0.8164        | 3.0   | 57   | 1.1570          | 0.4      |
| 0.5884        | 4.0   | 76   | 1.2403          | 0.35     |
| 0.3322        | 5.0   | 95   | 1.3815          | 0.35     |
| 0.156         | 6.0   | 114  | 1.8102          | 0.3      |
| 0.0576        | 7.0   | 133  | 2.1439          | 0.4      |
| 0.0227        | 8.0   | 152  | 2.4368          | 0.3      |
| 0.0133        | 9.0   | 171  | 2.5994          | 0.4      |
| 0.009         | 10.0  | 190  | 2.7388          | 0.35     |
| 0.0072        | 11.0  | 209  | 2.8287          | 0.35     |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
