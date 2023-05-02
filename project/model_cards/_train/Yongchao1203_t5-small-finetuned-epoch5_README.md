---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: t5-small-finetuned-xsum
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-xsum

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0531
- Rouge1: 97.0969
- Rouge2: 95.8095
- Rougel: 96.7452
- Rougelsum: 96.7363
- Gen Len: 15.3151

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
| 1.033         | 1.0   | 519  | 0.2212          | 95.3952 | 91.6915 | 94.8024 | 94.7963   | 14.9826 |
| 0.2732        | 2.0   | 1038 | 0.1233          | 96.3758 | 94.121  | 95.9352 | 95.9297   | 15.2223 |
| 0.1814        | 3.0   | 1557 | 0.0940          | 96.7098 | 94.7563 | 96.2577 | 96.2413   | 15.2133 |
| 0.144         | 4.0   | 2076 | 0.0757          | 96.6801 | 95.0173 | 96.2782 | 96.2691   | 15.2679 |
| 0.1213        | 5.0   | 2595 | 0.0688          | 96.8498 | 95.2702 | 96.5014 | 96.485    | 15.2515 |
| 0.1043        | 6.0   | 3114 | 0.0620          | 96.8951 | 95.3824 | 96.5526 | 96.5419   | 15.2808 |
| 0.0938        | 7.0   | 3633 | 0.0561          | 97.0021 | 95.6205 | 96.6811 | 96.6711   | 15.3163 |
| 0.0877        | 8.0   | 4152 | 0.0546          | 97.016  | 95.7049 | 96.6736 | 96.6688   | 15.3044 |
| 0.0873        | 9.0   | 4671 | 0.0534          | 97.0697 | 95.7894 | 96.7221 | 96.7192   | 15.3123 |
| 0.0841        | 10.0  | 5190 | 0.0531          | 97.0969 | 95.8095 | 96.7452 | 96.7363   | 15.3151 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
