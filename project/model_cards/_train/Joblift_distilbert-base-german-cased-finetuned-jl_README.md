---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: distilbert-base-german-cased-finetuned-jl
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-german-cased-finetuned-jl

This model is a fine-tuned version of [distilbert-base-german-cased](https://huggingface.co/distilbert-base-german-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9427

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
- train_batch_size: 128
- eval_batch_size: 128
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| No log        | 0.1   | 1000  | 1.5731          |
| No log        | 0.19  | 2000  | 1.4019          |
| No log        | 0.29  | 3000  | 1.3042          |
| No log        | 0.39  | 4000  | 1.2398          |
| No log        | 0.48  | 5000  | 1.1949          |
| No log        | 0.58  | 6000  | 1.1584          |
| No log        | 0.68  | 7000  | 1.1296          |
| No log        | 0.77  | 8000  | 1.1055          |
| No log        | 0.87  | 9000  | 1.0842          |
| No log        | 0.97  | 10000 | 1.0680          |
| No log        | 1.06  | 11000 | 1.0521          |
| No log        | 1.16  | 12000 | 1.0388          |
| No log        | 1.26  | 13000 | 1.0248          |
| No log        | 1.35  | 14000 | 1.0154          |
| No log        | 1.45  | 15000 | 1.0051          |
| No log        | 1.55  | 16000 | 0.9981          |
| No log        | 1.64  | 17000 | 0.9891          |
| No log        | 1.74  | 18000 | 0.9827          |
| No log        | 1.84  | 19000 | 0.9765          |
| No log        | 1.93  | 20000 | 0.9714          |
| 1.2477        | 2.03  | 21000 | 0.9672          |
| 1.2477        | 2.13  | 22000 | 0.9613          |
| 1.2477        | 2.22  | 23000 | 0.9582          |
| 1.2477        | 2.32  | 24000 | 0.9548          |
| 1.2477        | 2.42  | 25000 | 0.9508          |
| 1.2477        | 2.51  | 26000 | 0.9491          |
| 1.2477        | 2.61  | 27000 | 0.9466          |
| 1.2477        | 2.71  | 28000 | 0.9458          |
| 1.2477        | 2.8   | 29000 | 0.9446          |
| 1.2477        | 2.9   | 30000 | 0.9431          |
| 1.2477        | 3.0   | 31000 | 0.9427          |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.9.0+cu111
- Datasets 2.5.1
- Tokenizers 0.12.1
