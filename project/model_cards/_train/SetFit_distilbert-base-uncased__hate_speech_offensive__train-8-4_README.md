---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-8-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-8-4

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1045
- Accuracy: 0.128

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
| 1.1115        | 1.0   | 5    | 1.1174          | 0.0      |
| 1.0518        | 2.0   | 10   | 1.1379          | 0.0      |
| 1.0445        | 3.0   | 15   | 1.1287          | 0.0      |
| 0.9306        | 4.0   | 20   | 1.1324          | 0.2      |
| 0.8242        | 5.0   | 25   | 1.1219          | 0.2      |
| 0.7986        | 6.0   | 30   | 1.1369          | 0.4      |
| 0.7369        | 7.0   | 35   | 1.1732          | 0.2      |
| 0.534         | 8.0   | 40   | 1.1828          | 0.6      |
| 0.4285        | 9.0   | 45   | 1.1482          | 0.6      |
| 0.3691        | 10.0  | 50   | 1.1401          | 0.6      |
| 0.3215        | 11.0  | 55   | 1.1286          | 0.6      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
