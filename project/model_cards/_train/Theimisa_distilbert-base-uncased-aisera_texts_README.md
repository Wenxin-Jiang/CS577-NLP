---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: distilbert-base-uncased-aisera_texts
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-aisera_texts

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8283

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 2.0694        | 1.0   | 7790  | 1.9868          |
| 1.9054        | 2.0   | 15580 | 1.8646          |
| 1.8701        | 3.0   | 23370 | 1.8283          |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0
- Tokenizers 0.12.1
