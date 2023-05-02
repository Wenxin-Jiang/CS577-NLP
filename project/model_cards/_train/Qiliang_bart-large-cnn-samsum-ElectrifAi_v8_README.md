---
license: mit
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bart-large-cnn-samsum-ElectrifAi_v8
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-large-cnn-samsum-ElectrifAi_v8

This model is a fine-tuned version of [philschmid/bart-large-cnn-samsum](https://huggingface.co/philschmid/bart-large-cnn-samsum) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5051
- Rouge1: 51.3789
- Rouge2: 27.7926
- Rougel: 38.0256
- Rougelsum: 50.0685
- Gen Len: 104.4

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len  |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:--------:|
| No log        | 1.0   | 27   | 1.4978          | 54.3415 | 30.2195 | 39.7514 | 52.7012   | 103.2667 |
| No log        | 2.0   | 54   | 1.5002          | 51.6735 | 28.1006 | 37.5005 | 49.9317   | 117.8    |
| No log        | 3.0   | 81   | 1.5051          | 51.3789 | 27.7926 | 38.0256 | 50.0685   | 104.4    |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1
- Datasets 2.6.1
- Tokenizers 0.13.2
