---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: distilbert-base-uncased-IMDB_distilbert
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-IMDB_distilbert

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.6232

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 16

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 3.1531        | 1.0   | 1250  | 2.9545          |
| 2.9251        | 2.0   | 2500  | 2.8577          |
| 2.7865        | 3.0   | 3750  | 2.8460          |
| 2.692         | 4.0   | 5000  | 2.7769          |
| 2.611         | 5.0   | 6250  | 2.8373          |
| 2.5341        | 6.0   | 7500  | 2.7105          |
| 2.4887        | 7.0   | 8750  | 2.6864          |
| 2.4292        | 8.0   | 10000 | 2.6600          |
| 2.3524        | 9.0   | 11250 | 2.6872          |
| 2.3217        | 10.0  | 12500 | 2.6527          |
| 2.2961        | 11.0  | 13750 | 2.6659          |
| 2.2553        | 12.0  | 15000 | 2.6513          |
| 2.2066        | 13.0  | 16250 | 2.6443          |
| 2.1912        | 14.0  | 17500 | 2.5912          |
| 2.1703        | 15.0  | 18750 | 2.6312          |
| 2.1715        | 16.0  | 20000 | 2.6232          |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
