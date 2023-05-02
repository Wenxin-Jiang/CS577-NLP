---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- amazon_reviews_multi
model-index:
- name: reviews-generator
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# reviews-generator

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on the amazon_reviews_multi dataset.
It achieves the following results on the evaluation set:
- Loss: 3.4989

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- training_steps: 1000

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 3.7955        | 0.08  | 500  | 3.5578          |
| 3.7486        | 0.16  | 1000 | 3.4989          |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
