---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: twitter-data-distilbert-base-uncased-sentiment-finetuned-memes-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# twitter-data-distilbert-base-uncased-sentiment-finetuned-memes-v1

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2426
- Accuracy: 0.6492
- Precision: 0.6498
- Recall: 0.6492
- F1: 0.6492

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.8263        | 1.0   | 663  | 0.7315          | 0.6536   | 0.6699    | 0.6536 | 0.6502 |
| 0.6658        | 2.0   | 1326 | 0.7801          | 0.6565   | 0.6613    | 0.6565 | 0.6560 |
| 0.5735        | 3.0   | 1989 | 0.8170          | 0.6514   | 0.6579    | 0.6514 | 0.6504 |
| 0.344         | 4.0   | 2652 | 1.0184          | 0.6512   | 0.6525    | 0.6512 | 0.6512 |
| 0.2671        | 5.0   | 3315 | 1.1672          | 0.6503   | 0.6519    | 0.6503 | 0.6504 |
| 0.2236        | 6.0   | 3978 | 1.2426          | 0.6492   | 0.6498    | 0.6492 | 0.6492 |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
