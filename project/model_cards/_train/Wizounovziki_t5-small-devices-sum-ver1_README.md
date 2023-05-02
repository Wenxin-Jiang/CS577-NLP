---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-small-devices-sum-ver1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-devices-sum-ver1

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2335
- Rouge1: 93.7171
- Rouge2: 73.3058
- Rougel: 93.7211
- Rougelsum: 93.689
- Gen Len: 4.7246

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
| No log        | 1.0   | 185  | 0.6517          | 83.2503 | 55.7516 | 83.254  | 83.2722   | 4.4729  |
| No log        | 2.0   | 370  | 0.4239          | 89.2246 | 65.7477 | 89.2223 | 89.2288   | 4.5575  |
| 1.0224        | 3.0   | 555  | 0.3459          | 91.0524 | 68.4783 | 91.0222 | 91.0312   | 4.6685  |
| 1.0224        | 4.0   | 740  | 0.3023          | 91.9741 | 70.1066 | 91.9886 | 91.9525   | 4.6549  |
| 1.0224        | 5.0   | 925  | 0.2797          | 92.667  | 71.3468 | 92.6706 | 92.6611   | 4.6969  |
| 0.3678        | 6.0   | 1110 | 0.2616          | 93.229  | 72.2805 | 93.222  | 93.1935   | 4.7179  |
| 0.3678        | 7.0   | 1295 | 0.2469          | 93.362  | 72.6985 | 93.3651 | 93.3294   | 4.7111  |
| 0.3678        | 8.0   | 1480 | 0.2401          | 93.5689 | 73.009  | 93.582  | 93.5377   | 4.7192  |
| 0.2902        | 9.0   | 1665 | 0.2350          | 93.7013 | 73.2685 | 93.7256 | 93.684    | 4.724   |
| 0.2902        | 10.0  | 1850 | 0.2335          | 93.7171 | 73.3058 | 93.7211 | 93.689    | 4.7246  |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
