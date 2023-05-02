---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-base-devices-sum-ver2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-devices-sum-ver2

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1919
- Rouge1: 95.2959
- Rouge2: 72.5788
- Rougel: 95.292
- Rougelsum: 95.3437
- Gen Len: 4.5992

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

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 91   | 0.4308          | 87.5009 | 61.4165 | 87.6082 | 87.6628   | 4.3897  |
| No log        | 2.0   | 182  | 0.2945          | 91.7111 | 66.9023 | 91.706  | 91.7348   | 4.4965  |
| No log        | 3.0   | 273  | 0.2515          | 93.0416 | 68.8046 | 93.063  | 93.0907   | 4.516   |
| No log        | 4.0   | 364  | 0.2259          | 94.2097 | 70.862  | 94.2438 | 94.2767   | 4.6283  |
| No log        | 5.0   | 455  | 0.2148          | 94.7732 | 71.4693 | 94.78   | 94.8274   | 4.5936  |
| 0.4603        | 6.0   | 546  | 0.2030          | 95.0207 | 71.7789 | 95.0212 | 95.0887   | 4.5798  |
| 0.4603        | 7.0   | 637  | 0.1964          | 95.1482 | 72.3333 | 95.1651 | 95.202    | 4.6227  |
| 0.4603        | 8.0   | 728  | 0.1929          | 95.3279 | 72.551  | 95.3459 | 95.3972   | 4.5825  |
| 0.4603        | 9.0   | 819  | 0.1935          | 95.2413 | 72.5801 | 95.2372 | 95.3121   | 4.5992  |
| 0.4603        | 10.0  | 910  | 0.1919          | 95.2959 | 72.5788 | 95.292  | 95.3437   | 4.5992  |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
