---
tags:
- automatic-speech-recognition
- abdusahmbzuai/arabic_speech_massive_300hrs
- generated_from_trainer
model-index:
- name: aradia-ctc-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# aradia-ctc-v1

This model is a fine-tuned version of [/l/users/abdulwahab.sahyoun/aradia/aradia-ctc-v1](https://huggingface.co//l/users/abdulwahab.sahyoun/aradia/aradia-ctc-v1) on the ABDUSAHMBZUAI/ARABIC_SPEECH_MASSIVE_300HRS - NA dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7171
- Wer: 0.3336

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 20.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| No log        | 0.22  | 100  | 5.1889          | 1.0    |
| No log        | 0.43  | 200  | 3.1129          | 1.0    |
| No log        | 0.65  | 300  | 3.0503          | 1.0    |
| No log        | 0.87  | 400  | 3.0279          | 1.0    |
| 6.2756        | 1.09  | 500  | 2.9965          | 1.0    |
| 6.2756        | 1.3   | 600  | 2.3618          | 0.9993 |
| 6.2756        | 1.52  | 700  | 1.2715          | 0.8758 |
| 6.2756        | 1.74  | 800  | 0.9971          | 0.7156 |
| 6.2756        | 1.96  | 900  | 0.8927          | 0.6382 |
| 1.712         | 2.17  | 1000 | 0.8252          | 0.5926 |
| 1.712         | 2.39  | 1100 | 0.7794          | 0.5434 |
| 1.712         | 2.61  | 1200 | 0.7557          | 0.5092 |
| 1.712         | 2.83  | 1300 | 0.7347          | 0.5203 |
| 1.712         | 3.04  | 1400 | 0.7189          | 0.4929 |
| 0.9305        | 3.26  | 1500 | 0.6820          | 0.4595 |
| 0.9305        | 3.48  | 1600 | 0.6792          | 0.4504 |
| 0.9305        | 3.69  | 1700 | 0.6596          | 0.4442 |
| 0.9305        | 3.91  | 1800 | 0.6756          | 0.4432 |
| 0.9305        | 4.13  | 1900 | 0.6663          | 0.4392 |
| 0.737         | 4.35  | 2000 | 0.6479          | 0.4372 |
| 0.737         | 4.56  | 2100 | 0.6353          | 0.4203 |
| 0.737         | 4.78  | 2200 | 0.6251          | 0.4088 |
| 0.737         | 5.0   | 2300 | 0.6209          | 0.4177 |
| 0.737         | 5.22  | 2400 | 0.6639          | 0.4094 |
| 0.6247        | 5.43  | 2500 | 0.6408          | 0.3970 |
| 0.6247        | 5.65  | 2600 | 0.6373          | 0.3932 |
| 0.6247        | 5.87  | 2700 | 0.6411          | 0.3928 |
| 0.6247        | 6.09  | 2800 | 0.6378          | 0.3897 |
| 0.6247        | 6.3   | 2900 | 0.6396          | 0.3929 |
| 0.5443        | 6.52  | 3000 | 0.6544          | 0.3864 |
| 0.5443        | 6.74  | 3100 | 0.6218          | 0.3786 |
| 0.5443        | 6.96  | 3200 | 0.6200          | 0.3784 |
| 0.5443        | 7.17  | 3300 | 0.6157          | 0.3791 |
| 0.5443        | 7.39  | 3400 | 0.6317          | 0.3798 |
| 0.4845        | 7.61  | 3500 | 0.6540          | 0.3771 |
| 0.4845        | 7.83  | 3600 | 0.6436          | 0.3670 |
| 0.4845        | 8.04  | 3700 | 0.6335          | 0.3695 |
| 0.4845        | 8.26  | 3800 | 0.6579          | 0.3610 |
| 0.4845        | 8.48  | 3900 | 0.6170          | 0.3613 |
| 0.4279        | 8.69  | 4000 | 0.6523          | 0.3617 |
| 0.4279        | 8.91  | 4100 | 0.6349          | 0.3577 |
| 0.4279        | 9.13  | 4200 | 0.6344          | 0.3673 |
| 0.4279        | 9.35  | 4300 | 0.6215          | 0.3641 |
| 0.4279        | 9.56  | 4400 | 0.6513          | 0.3608 |
| 0.3825        | 9.78  | 4500 | 0.6386          | 0.3605 |
| 0.3825        | 10.0  | 4600 | 0.6724          | 0.3549 |
| 0.3825        | 10.22 | 4700 | 0.6776          | 0.3602 |
| 0.3825        | 10.43 | 4800 | 0.6739          | 0.3544 |
| 0.3825        | 10.65 | 4900 | 0.6688          | 0.3557 |
| 0.3477        | 10.87 | 5000 | 0.6674          | 0.3564 |
| 0.3477        | 11.09 | 5100 | 0.6786          | 0.3476 |
| 0.3477        | 11.3  | 5200 | 0.6818          | 0.3478 |
| 0.3477        | 11.52 | 5300 | 0.6874          | 0.3470 |
| 0.3477        | 11.74 | 5400 | 0.6993          | 0.3424 |
| 0.3101        | 11.96 | 5500 | 0.6950          | 0.3404 |
| 0.3101        | 12.17 | 5600 | 0.6872          | 0.3406 |
| 0.3101        | 12.39 | 5700 | 0.6846          | 0.3424 |
| 0.3101        | 12.61 | 5800 | 0.7051          | 0.3405 |
| 0.3101        | 12.83 | 5900 | 0.7051          | 0.3378 |
| 0.2859        | 13.04 | 6000 | 0.6955          | 0.3403 |
| 0.2859        | 13.26 | 6100 | 0.7115          | 0.3390 |
| 0.2859        | 13.48 | 6200 | 0.7074          | 0.3384 |
| 0.2859        | 13.69 | 6300 | 0.7002          | 0.3376 |
| 0.2859        | 13.91 | 6400 | 0.7171          | 0.3360 |
| 0.2714        | 14.13 | 6500 | 0.7193          | 0.3341 |
| 0.2714        | 14.35 | 6600 | 0.7132          | 0.3347 |
| 0.2714        | 14.56 | 6700 | 0.7184          | 0.3353 |
| 0.2714        | 14.78 | 6800 | 0.7171          | 0.3331 |


### Framework versions

- Transformers 4.18.0.dev0
- Pytorch 1.10.2+cu113
- Datasets 1.18.4
- Tokenizers 0.11.6
