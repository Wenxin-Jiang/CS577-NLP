---
license: cc-by-4.0
tags:
- generated_from_trainer
model-index:
- name: herbert-base-cased-finetuned-squad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# herbert-base-cased-finetuned-squad

This model is a fine-tuned version of [allegro/herbert-base-cased](https://huggingface.co/allegro/herbert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2071

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 233  | 1.2474          |
| No log        | 2.0   | 466  | 1.1951          |
| 1.3459        | 3.0   | 699  | 1.2071          |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.0+cu111
- Datasets 1.17.0
- Tokenizers 0.10.3
