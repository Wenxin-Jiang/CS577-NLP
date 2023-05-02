---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- cuad
model-index:
- name: legal-bert-small-uncased-cuad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# legal-bert-small-uncased-cuad

This model is a fine-tuned version of [nlpaueb/legal-bert-small-uncased](https://huggingface.co/nlpaueb/legal-bert-small-uncased) on the cuad dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0371

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.0565        | 1.0   | 11081 | 0.0411          |
| 0.0489        | 2.0   | 22162 | 0.0364          |
| 0.0409        | 3.0   | 33243 | 0.0371          |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
