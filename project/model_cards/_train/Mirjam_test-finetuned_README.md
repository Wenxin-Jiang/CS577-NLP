---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: test-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# test-finetuned

This model is a fine-tuned version of [yhavinga/t5-v1.1-base-dutch-cnn-test](https://huggingface.co/yhavinga/t5-v1.1-base-dutch-cnn-test) on the None dataset.

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
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 1    | nan             | 33.8462 | 31.746 | 30.7692 | 30.7692   | 86.0    |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1
- Datasets 1.15.1
- Tokenizers 0.10.3
