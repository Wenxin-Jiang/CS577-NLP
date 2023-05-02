---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- becasv3
model-index:
- name: distilbert-base-uncased-modelo-becas0
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-modelo-becas0

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the becasv3 dataset.
It achieves the following results on the evaluation set:
- Loss: 3.1182

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 5    | 5.5381          |
| No log        | 2.0   | 10   | 4.9493          |
| No log        | 3.0   | 15   | 4.4985          |
| No log        | 4.0   | 20   | 4.1063          |
| No log        | 5.0   | 25   | 3.7708          |
| No log        | 6.0   | 30   | 3.5205          |
| No log        | 7.0   | 35   | 3.3313          |
| No log        | 8.0   | 40   | 3.2195          |
| No log        | 9.0   | 45   | 3.1453          |
| No log        | 10.0  | 50   | 3.1182          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
