---
license: mit
tags:
- generated_from_trainer
model-index:
- name: bert-base-historic-english-cased-squad-en
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-historic-english-cased-squad-en

This model is a fine-tuned version of [dbmdz/bert-base-historic-english-cased](https://huggingface.co/dbmdz/bert-base-historic-english-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7739

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.2
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.2943        | 1.0   | 4686 | 1.9503          |
| 2.0811        | 2.0   | 9372 | 1.7739          |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1
- Tokenizers 0.13.2
