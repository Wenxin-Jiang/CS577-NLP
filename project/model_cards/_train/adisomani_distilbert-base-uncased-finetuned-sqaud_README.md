---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: distilbert-base-uncased-finetuned-sqaud
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-sqaud

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2831

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
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 14   | 0.9851          |
| No log        | 2.0   | 28   | 0.6955          |
| No log        | 3.0   | 42   | 0.5781          |
| No log        | 4.0   | 56   | 0.4548          |
| No log        | 5.0   | 70   | 0.4208          |
| No log        | 6.0   | 84   | 0.3592          |
| No log        | 7.0   | 98   | 0.3422          |
| No log        | 8.0   | 112  | 0.3424          |
| No log        | 9.0   | 126  | 0.4046          |
| No log        | 10.0  | 140  | 0.3142          |
| No log        | 11.0  | 154  | 0.3262          |
| No log        | 12.0  | 168  | 0.2879          |
| No log        | 13.0  | 182  | 0.3376          |
| No log        | 14.0  | 196  | 0.2870          |
| No log        | 15.0  | 210  | 0.2984          |
| No log        | 16.0  | 224  | 0.2807          |
| No log        | 17.0  | 238  | 0.2889          |
| No log        | 18.0  | 252  | 0.2877          |
| No log        | 19.0  | 266  | 0.2820          |
| No log        | 20.0  | 280  | 0.2831          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
