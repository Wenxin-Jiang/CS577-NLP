---
tags:
- generated_from_trainer
datasets:
- null
model-index:
- name: bert-base-multilingual-cased-urgency
  results:
  - task:
      name: Masked Language Modeling
      type: fill-mask
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-multilingual-cased-urgency

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/) on the mWACH NEO dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2797

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
| 4.1408        | 1.0   | 5659  | 3.6705          |
| 2.8777        | 2.0   | 11318 | 2.5536          |
| 2.561         | 3.0   | 16977 | 2.2740          |


### Framework versions

- Transformers 4.10.0
- Pytorch 1.9.0+cu102
- Datasets 1.11.0
- Tokenizers 0.10.3
