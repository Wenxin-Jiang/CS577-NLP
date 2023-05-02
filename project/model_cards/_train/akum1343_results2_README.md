---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: results2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# results2

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the None dataset.

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
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 27   | 6.1310          | 11.5882 | 3.2614 | 10.0378 | 11.2317   | 17.2    |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cpu
- Datasets 2.6.1
- Tokenizers 0.12.1
