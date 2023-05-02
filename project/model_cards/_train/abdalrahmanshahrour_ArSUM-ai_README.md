---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- xlsum
model-index:
- name: ArSUM-ai
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# ArSUM-ai

This model is a fine-tuned version of [abdalrahmanshahrour/arabartsummarization](https://huggingface.co/abdalrahmanshahrour/arabartsummarization) on the xlsum dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5951

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 2.3947        | 1.0   | 9380  | 2.4121          |
| 2.182         | 2.0   | 18760 | 2.4303          |
| 1.9303        | 3.0   | 28140 | 2.4727          |
| 1.7455        | 4.0   | 37520 | 2.5470          |
| 1.5804        | 5.0   | 46900 | 2.5951          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
