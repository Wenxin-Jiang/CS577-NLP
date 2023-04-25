---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__hate_speech_offensive__train-16-0
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__hate_speech_offensive__train-16-0

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2707
- Accuracy: 0.517

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
| 1.0943        | 1.0   | 10   | 1.1095          | 0.3      |
| 1.0602        | 2.0   | 20   | 1.1086          | 0.4      |
| 1.0159        | 3.0   | 30   | 1.1165          | 0.4      |
| 0.9027        | 4.0   | 40   | 1.1377          | 0.4      |
| 0.8364        | 5.0   | 50   | 1.0126          | 0.5      |
| 0.6653        | 6.0   | 60   | 0.9298          | 0.5      |
| 0.535         | 7.0   | 70   | 0.9555          | 0.5      |
| 0.3713        | 8.0   | 80   | 0.8543          | 0.4      |
| 0.1633        | 9.0   | 90   | 0.9876          | 0.4      |
| 0.1069        | 10.0  | 100  | 0.8383          | 0.6      |
| 0.0591        | 11.0  | 110  | 0.8056          | 0.6      |
| 0.0344        | 12.0  | 120  | 0.8915          | 0.6      |
| 0.0265        | 13.0  | 130  | 0.8722          | 0.6      |
| 0.0196        | 14.0  | 140  | 1.0064          | 0.6      |
| 0.0158        | 15.0  | 150  | 1.0479          | 0.6      |
| 0.0128        | 16.0  | 160  | 1.0723          | 0.6      |
| 0.0121        | 17.0  | 170  | 1.0758          | 0.6      |
| 0.0093        | 18.0  | 180  | 1.1236          | 0.6      |
| 0.0085        | 19.0  | 190  | 1.1480          | 0.6      |
| 0.0084        | 20.0  | 200  | 1.1651          | 0.6      |
| 0.0077        | 21.0  | 210  | 1.1832          | 0.6      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
