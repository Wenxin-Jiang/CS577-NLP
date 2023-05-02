---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- cuad
model-index:
- name: legal-roberta-base-cuad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# legal-roberta-base-cuad

This model is a fine-tuned version of [saibo/legal-roberta-base](https://huggingface.co/saibo/legal-roberta-base) on the cuad dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0260

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
- train_batch_size: 24
- eval_batch_size: 24
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 0.0393        | 1.0   | 51295  | 0.0261          |
| 0.0234        | 2.0   | 102590 | 0.0254          |
| 0.0234        | 3.0   | 153885 | 0.0260          |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
