---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-16-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-16-3

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0675
- Accuracy: 0.44

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
| 1.0951        | 1.0   | 10   | 1.1346          | 0.1      |
| 1.0424        | 2.0   | 20   | 1.1120          | 0.2      |
| 0.957         | 3.0   | 30   | 1.1002          | 0.3      |
| 0.7889        | 4.0   | 40   | 1.0838          | 0.4      |
| 0.6162        | 5.0   | 50   | 1.0935          | 0.5      |
| 0.4849        | 6.0   | 60   | 1.0867          | 0.5      |
| 0.3089        | 7.0   | 70   | 1.1145          | 0.5      |
| 0.2145        | 8.0   | 80   | 1.1278          | 0.6      |
| 0.0805        | 9.0   | 90   | 1.2801          | 0.6      |
| 0.0497        | 10.0  | 100  | 1.3296          | 0.6      |
| 0.0328        | 11.0  | 110  | 1.2913          | 0.6      |
| 0.0229        | 12.0  | 120  | 1.3692          | 0.6      |
| 0.0186        | 13.0  | 130  | 1.4642          | 0.6      |
| 0.0161        | 14.0  | 140  | 1.5568          | 0.6      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
