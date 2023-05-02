---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-base-timit-demo-google-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-timit-demo-google-colab

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4770
- Wer: 0.3360

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
| 3.6401        | 1.0   | 500   | 2.4138          | 1.0    |
| 0.9717        | 2.01  | 1000  | 0.6175          | 0.5531 |
| 0.4393        | 3.01  | 1500  | 0.4309          | 0.4414 |
| 0.2976        | 4.02  | 2000  | 0.4167          | 0.4162 |
| 0.2345        | 5.02  | 2500  | 0.4273          | 0.3927 |
| 0.1919        | 6.02  | 3000  | 0.3983          | 0.3886 |
| 0.1565        | 7.03  | 3500  | 0.5581          | 0.3928 |
| 0.1439        | 8.03  | 4000  | 0.4509          | 0.3821 |
| 0.1266        | 9.04  | 4500  | 0.4733          | 0.3774 |
| 0.1091        | 10.04 | 5000  | 0.4755          | 0.3808 |
| 0.1001        | 11.04 | 5500  | 0.4435          | 0.3689 |
| 0.0911        | 12.05 | 6000  | 0.4962          | 0.3897 |
| 0.0813        | 13.05 | 6500  | 0.5031          | 0.3622 |
| 0.0729        | 14.06 | 7000  | 0.4853          | 0.3597 |
| 0.0651        | 15.06 | 7500  | 0.5180          | 0.3577 |
| 0.0608        | 16.06 | 8000  | 0.5251          | 0.3630 |
| 0.0592        | 17.07 | 8500  | 0.4915          | 0.3591 |
| 0.0577        | 18.07 | 9000  | 0.4724          | 0.3656 |
| 0.0463        | 19.08 | 9500  | 0.4536          | 0.3546 |
| 0.0475        | 20.08 | 10000 | 0.5107          | 0.3546 |
| 0.0464        | 21.08 | 10500 | 0.4829          | 0.3464 |
| 0.0369        | 22.09 | 11000 | 0.4844          | 0.3448 |
| 0.0327        | 23.09 | 11500 | 0.4865          | 0.3437 |
| 0.0337        | 24.1  | 12000 | 0.4825          | 0.3488 |
| 0.0271        | 25.1  | 12500 | 0.4824          | 0.3445 |
| 0.0236        | 26.1  | 13000 | 0.4747          | 0.3397 |
| 0.0243        | 27.11 | 13500 | 0.4840          | 0.3397 |
| 0.0226        | 28.11 | 14000 | 0.4716          | 0.3354 |
| 0.0235        | 29.12 | 14500 | 0.4770          | 0.3360 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1
