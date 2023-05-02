---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-8-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-8-5

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7214
- Accuracy: 0.37

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
| 1.0995        | 1.0   | 5    | 1.1301          | 0.0      |
| 1.0227        | 2.0   | 10   | 1.1727          | 0.0      |
| 1.0337        | 3.0   | 15   | 1.1734          | 0.2      |
| 0.9137        | 4.0   | 20   | 1.1829          | 0.2      |
| 0.8065        | 5.0   | 25   | 1.1496          | 0.4      |
| 0.7038        | 6.0   | 30   | 1.1101          | 0.4      |
| 0.6246        | 7.0   | 35   | 1.0982          | 0.2      |
| 0.4481        | 8.0   | 40   | 1.0913          | 0.2      |
| 0.3696        | 9.0   | 45   | 1.0585          | 0.4      |
| 0.3137        | 10.0  | 50   | 1.0418          | 0.4      |
| 0.2482        | 11.0  | 55   | 1.0078          | 0.4      |
| 0.196         | 12.0  | 60   | 0.9887          | 0.6      |
| 0.1344        | 13.0  | 65   | 0.9719          | 0.6      |
| 0.1014        | 14.0  | 70   | 1.0053          | 0.6      |
| 0.111         | 15.0  | 75   | 0.9653          | 0.6      |
| 0.0643        | 16.0  | 80   | 0.9018          | 0.6      |
| 0.0559        | 17.0  | 85   | 0.9393          | 0.6      |
| 0.0412        | 18.0  | 90   | 1.0210          | 0.6      |
| 0.0465        | 19.0  | 95   | 0.9965          | 0.6      |
| 0.0328        | 20.0  | 100  | 0.9739          | 0.6      |
| 0.0289        | 21.0  | 105  | 0.9796          | 0.6      |
| 0.0271        | 22.0  | 110  | 0.9968          | 0.6      |
| 0.0239        | 23.0  | 115  | 1.0143          | 0.6      |
| 0.0201        | 24.0  | 120  | 1.0459          | 0.6      |
| 0.0185        | 25.0  | 125  | 1.0698          | 0.6      |
| 0.0183        | 26.0  | 130  | 1.0970          | 0.6      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
