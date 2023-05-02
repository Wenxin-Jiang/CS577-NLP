---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- opus_infopankki
model-index:
- name: t5-opus_infopankki-en-zh
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-opus_infopankki-en-zh

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the opus_infopankki dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3548

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
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 3.065         | 1.0   | 1496  | 2.7383          |
| 2.8459        | 2.0   | 2992  | 2.6077          |
| 2.7296        | 3.0   | 4488  | 2.5336          |
| 2.6639        | 4.0   | 5984  | 2.4761          |
| 2.6234        | 5.0   | 7480  | 2.4342          |
| 2.5847        | 6.0   | 8976  | 2.4038          |
| 2.5536        | 7.0   | 10472 | 2.3808          |
| 2.5213        | 8.0   | 11968 | 2.3663          |
| 2.5275        | 9.0   | 13464 | 2.3574          |
| 2.5215        | 10.0  | 14960 | 2.3548          |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
