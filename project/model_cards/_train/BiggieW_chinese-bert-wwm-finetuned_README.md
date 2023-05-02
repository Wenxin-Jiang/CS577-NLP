---
license: apache-2.0
tags:
- generated_from_trainer
widget:
- '今天的天气真[MASK]。'
model-index:
- name: chinese-bert-wwm-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# chinese-bert-wwm-finetuned

This model is a fine-tuned version of [hfl/chinese-bert-wwm](https://huggingface.co/hfl/chinese-bert-wwm) on a very small subset of TNEWS dataset.
It achieves the following results on the evaluation set:
- Loss: 4.2495

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
- train_batch_size: 3
- eval_batch_size: 3
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 4.4411        | 1.0   | 11   | 3.7846          |
| 3.3828        | 2.0   | 22   | 3.6168          |
| 3.5233        | 3.0   | 33   | 3.9919          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
