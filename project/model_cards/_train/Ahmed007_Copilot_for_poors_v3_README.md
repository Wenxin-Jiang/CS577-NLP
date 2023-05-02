---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: Copilot_for_poors_v3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Copilot_for_poors_v3

This model is a fine-tuned version of [Ahmed007/Copilot_for_poors_v2](https://huggingface.co/Ahmed007/Copilot_for_poors_v2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3504

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
- train_batch_size: 12
- eval_batch_size: 12
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 25

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 57   | 1.4567          |
| No log        | 2.0   | 114  | 1.4510          |
| No log        | 3.0   | 171  | 1.4376          |
| No log        | 4.0   | 228  | 1.4255          |
| No log        | 5.0   | 285  | 1.4174          |
| No log        | 6.0   | 342  | 1.4122          |
| No log        | 7.0   | 399  | 1.4080          |
| No log        | 8.0   | 456  | 1.3981          |
| 1.7151        | 9.0   | 513  | 1.3923          |
| 1.7151        | 10.0  | 570  | 1.3870          |
| 1.7151        | 11.0  | 627  | 1.3801          |
| 1.7151        | 12.0  | 684  | 1.3769          |
| 1.7151        | 13.0  | 741  | 1.3706          |
| 1.7151        | 14.0  | 798  | 1.3687          |
| 1.7151        | 15.0  | 855  | 1.3665          |
| 1.7151        | 16.0  | 912  | 1.3613          |
| 1.7151        | 17.0  | 969  | 1.3613          |
| 1.5556        | 18.0  | 1026 | 1.3576          |
| 1.5556        | 19.0  | 1083 | 1.3550          |
| 1.5556        | 20.0  | 1140 | 1.3540          |
| 1.5556        | 21.0  | 1197 | 1.3530          |
| 1.5556        | 22.0  | 1254 | 1.3514          |
| 1.5556        | 23.0  | 1311 | 1.3517          |
| 1.5556        | 24.0  | 1368 | 1.3506          |
| 1.5556        | 25.0  | 1425 | 1.3504          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
