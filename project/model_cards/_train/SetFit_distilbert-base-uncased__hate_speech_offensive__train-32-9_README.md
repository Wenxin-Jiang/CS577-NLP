---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-32-9
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-32-9

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7075
- Accuracy: 0.692

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
| 1.1054        | 1.0   | 19   | 1.0938          | 0.35     |
| 1.0338        | 2.0   | 38   | 1.0563          | 0.65     |
| 0.8622        | 3.0   | 57   | 0.9372          | 0.6      |
| 0.5919        | 4.0   | 76   | 0.8461          | 0.6      |
| 0.3357        | 5.0   | 95   | 1.0206          | 0.45     |
| 0.1621        | 6.0   | 114  | 0.9802          | 0.7      |
| 0.0637        | 7.0   | 133  | 1.2434          | 0.65     |
| 0.0261        | 8.0   | 152  | 1.3865          | 0.65     |
| 0.0156        | 9.0   | 171  | 1.4414          | 0.7      |
| 0.01          | 10.0  | 190  | 1.5502          | 0.7      |
| 0.0079        | 11.0  | 209  | 1.6102          | 0.7      |
| 0.0062        | 12.0  | 228  | 1.6525          | 0.7      |
| 0.0058        | 13.0  | 247  | 1.6884          | 0.7      |
| 0.0046        | 14.0  | 266  | 1.7479          | 0.7      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
