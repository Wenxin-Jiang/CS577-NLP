---
tags:
- generated_from_trainer
model-index:
- name: Test-demo-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Test-demo-colab

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9479
- Wer: 0.6856

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 4.2676        | 1.0   | 500   | 2.2725          | 1.0013 |
| 2.0086        | 2.01  | 1000  | 1.2788          | 0.8053 |
| 1.6389        | 3.01  | 1500  | 1.1333          | 0.7458 |
| 1.4908        | 4.02  | 2000  | 1.0369          | 0.7356 |
| 1.4137        | 5.02  | 2500  | 0.9894          | 0.7111 |
| 1.3507        | 6.02  | 3000  | 0.9394          | 0.7098 |
| 1.3101        | 7.03  | 3500  | 0.9531          | 0.6966 |
| 1.2682        | 8.03  | 4000  | 0.9255          | 0.6892 |
| 1.239         | 9.04  | 4500  | 0.9222          | 0.6818 |
| 1.2161        | 10.04 | 5000  | 0.9079          | 0.6911 |
| 1.1871        | 11.04 | 5500  | 0.9100          | 0.7033 |
| 1.1688        | 12.05 | 6000  | 0.9080          | 0.6924 |
| 1.1383        | 13.05 | 6500  | 0.9097          | 0.6910 |
| 1.1304        | 14.06 | 7000  | 0.9052          | 0.6810 |
| 1.1181        | 15.06 | 7500  | 0.9025          | 0.6847 |
| 1.0905        | 16.06 | 8000  | 0.9296          | 0.6832 |
| 1.0744        | 17.07 | 8500  | 0.9120          | 0.6912 |
| 1.0675        | 18.07 | 9000  | 0.9039          | 0.6864 |
| 1.0511        | 19.08 | 9500  | 0.9157          | 0.7004 |
| 1.0401        | 20.08 | 10000 | 0.9259          | 0.6792 |
| 1.0319        | 21.08 | 10500 | 0.9478          | 0.6976 |
| 1.0194        | 22.09 | 11000 | 0.9438          | 0.6820 |
| 1.0117        | 23.09 | 11500 | 0.9577          | 0.6891 |
| 1.0038        | 24.1  | 12000 | 0.9670          | 0.6918 |
| 0.9882        | 25.1  | 12500 | 0.9579          | 0.6884 |
| 0.9979        | 26.1  | 13000 | 0.9502          | 0.6869 |
| 0.9767        | 27.11 | 13500 | 0.9537          | 0.6833 |
| 0.964         | 28.11 | 14000 | 0.9525          | 0.6880 |
| 0.9867        | 29.12 | 14500 | 0.9479          | 0.6856 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1
