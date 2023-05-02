---
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: bertweet-finetuned-rbam
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bertweet-finetuned-rbam

This model is a fine-tuned version of [vinai/bertweet-base](https://huggingface.co/vinai/bertweet-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3971
- F1: 0.6620

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.7138        | 1.0   | 1632 | 0.7529          | 0.6814 |
| 0.5692        | 2.0   | 3264 | 0.8473          | 0.6803 |
| 0.4126        | 3.0   | 4896 | 1.0029          | 0.6617 |
| 0.2854        | 4.0   | 6528 | 1.2167          | 0.6635 |
| 0.2007        | 5.0   | 8160 | 1.3971          | 0.6620 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
