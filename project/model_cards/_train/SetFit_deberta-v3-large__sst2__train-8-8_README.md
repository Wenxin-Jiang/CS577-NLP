---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-8-8
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-8-8

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7414
- Accuracy: 0.5623

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
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.6597        | 1.0   | 3    | 0.7716          | 0.25     |
| 0.6376        | 2.0   | 6    | 0.7802          | 0.25     |
| 0.5857        | 3.0   | 9    | 0.6625          | 0.75     |
| 0.4024        | 4.0   | 12   | 0.5195          | 0.75     |
| 0.2635        | 5.0   | 15   | 0.4222          | 1.0      |
| 0.1714        | 6.0   | 18   | 0.4410          | 0.5      |
| 0.1267        | 7.0   | 21   | 0.7773          | 0.75     |
| 0.0582        | 8.0   | 24   | 0.9070          | 0.75     |
| 0.0374        | 9.0   | 27   | 0.9539          | 0.75     |
| 0.0204        | 10.0  | 30   | 1.0507          | 0.75     |
| 0.012         | 11.0  | 33   | 1.2802          | 0.5      |
| 0.0086        | 12.0  | 36   | 1.4272          | 0.5      |
| 0.0049        | 13.0  | 39   | 1.4803          | 0.5      |
| 0.0039        | 14.0  | 42   | 1.4912          | 0.5      |
| 0.0031        | 15.0  | 45   | 1.5231          | 0.5      |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
