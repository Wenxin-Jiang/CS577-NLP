---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: Fine_Tuned_XLSR_English
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Fine_Tuned_XLSR_English

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the [timit_asr](https://huggingface.co/datasets/timit_asr) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4033
- Wer: 0.3163

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
| 4.3757        | 1.0   | 500   | 3.1570          | 1.0    |
| 2.4891        | 2.01  | 1000  | 0.9252          | 0.8430 |
| 0.8725        | 3.01  | 1500  | 0.4581          | 0.4931 |
| 0.544         | 4.02  | 2000  | 0.3757          | 0.4328 |
| 0.4043        | 5.02  | 2500  | 0.3621          | 0.4087 |
| 0.3376        | 6.02  | 3000  | 0.3682          | 0.3931 |
| 0.2937        | 7.03  | 3500  | 0.3541          | 0.3743 |
| 0.2573        | 8.03  | 4000  | 0.3565          | 0.3593 |
| 0.2257        | 9.04  | 4500  | 0.3634          | 0.3654 |
| 0.215         | 10.04 | 5000  | 0.3695          | 0.3537 |
| 0.1879        | 11.04 | 5500  | 0.3690          | 0.3486 |
| 0.1599        | 12.05 | 6000  | 0.3743          | 0.3490 |
| 0.1499        | 13.05 | 6500  | 0.4108          | 0.3424 |
| 0.147         | 14.06 | 7000  | 0.4048          | 0.3400 |
| 0.1355        | 15.06 | 7500  | 0.3988          | 0.3357 |
| 0.1278        | 16.06 | 8000  | 0.3672          | 0.3384 |
| 0.1189        | 17.07 | 8500  | 0.4011          | 0.3340 |
| 0.1089        | 18.07 | 9000  | 0.3948          | 0.3300 |
| 0.1039        | 19.08 | 9500  | 0.4062          | 0.3317 |
| 0.0971        | 20.08 | 10000 | 0.4041          | 0.3252 |
| 0.0902        | 21.08 | 10500 | 0.4112          | 0.3301 |
| 0.0883        | 22.09 | 11000 | 0.4154          | 0.3292 |
| 0.0864        | 23.09 | 11500 | 0.3746          | 0.3189 |
| 0.0746        | 24.1  | 12000 | 0.3991          | 0.3230 |
| 0.0711        | 25.1  | 12500 | 0.3916          | 0.3200 |
| 0.0712        | 26.1  | 13000 | 0.4024          | 0.3193 |
| 0.0663        | 27.11 | 13500 | 0.3976          | 0.3184 |
| 0.0626        | 28.11 | 14000 | 0.4046          | 0.3168 |
| 0.0641        | 29.12 | 14500 | 0.4033          | 0.3163 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1
