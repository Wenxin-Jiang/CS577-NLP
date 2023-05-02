---
tags:
- generated_from_trainer
model-index:
- name: nezha-chinese-base-finetuned-product
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# nezha-chinese-base-finetuned-product

This model is a fine-tuned version of [peterchou/nezha-chinese-base](https://huggingface.co/peterchou/nezha-chinese-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0004

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
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.0309        | 1.0   | 6473  | 0.0037          |
| 0.0033        | 2.0   | 12946 | 0.0006          |
| 0.0017        | 3.0   | 19419 | 0.0004          |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.6.0
- Datasets 2.0.0
- Tokenizers 0.11.6
