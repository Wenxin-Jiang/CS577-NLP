---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: Copilot_for_poors_v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Copilot_for_poors_v2

This model is a fine-tuned version of [Ahmed007/Copilot_for_poors](https://huggingface.co/Ahmed007/Copilot_for_poors) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5072

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 14   | 1.5951          |
| No log        | 2.0   | 28   | 1.5887          |
| No log        | 3.0   | 42   | 1.5792          |
| No log        | 4.0   | 56   | 1.5684          |
| No log        | 5.0   | 70   | 1.5601          |
| No log        | 6.0   | 84   | 1.5525          |
| No log        | 7.0   | 98   | 1.5462          |
| No log        | 8.0   | 112  | 1.5401          |
| No log        | 9.0   | 126  | 1.5335          |
| No log        | 10.0  | 140  | 1.5293          |
| No log        | 11.0  | 154  | 1.5257          |
| No log        | 12.0  | 168  | 1.5220          |
| No log        | 13.0  | 182  | 1.5182          |
| No log        | 14.0  | 196  | 1.5151          |
| No log        | 15.0  | 210  | 1.5124          |
| No log        | 16.0  | 224  | 1.5110          |
| No log        | 17.0  | 238  | 1.5096          |
| No log        | 18.0  | 252  | 1.5083          |
| No log        | 19.0  | 266  | 1.5074          |
| No log        | 20.0  | 280  | 1.5072          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
