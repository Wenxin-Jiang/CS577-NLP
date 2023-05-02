---
language:
- tr
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_11_0
- generated_from_trainer
datasets:
- common_voice_11_0
metrics:
- wer
model-index:
- name: wav2vec2-xls-r-300m-tr
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: MOZILLA-FOUNDATION/COMMON_VOICE_11_0 - TR
      type: common_voice_11_0
      config: tr
      split: test
      args: 'Config: tr, Training split: train+validation, Eval split: test'
    metrics:
    - name: Wer
      type: wer
      value: 0.2862633203284225
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-300m-tr

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_11_0 - TR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3179
- Wer: 0.2863
- Cer: 0.0681

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
- train_batch_size: 64
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|
| No log        | 0.71  | 400   | 1.7290          | 0.9804 | 0.4797 |
| 4.5435        | 1.42  | 800   | 0.4810          | 0.5774 | 0.1450 |
| 0.523         | 2.12  | 1200  | 0.3859          | 0.4812 | 0.1156 |
| 0.3449        | 2.83  | 1600  | 0.3492          | 0.4498 | 0.1095 |
| 0.2814        | 3.54  | 2000  | 0.3660          | 0.4466 | 0.1099 |
| 0.2814        | 4.25  | 2400  | 0.3766          | 0.4235 | 0.1043 |
| 0.2463        | 4.96  | 2800  | 0.3416          | 0.4119 | 0.1010 |
| 0.2296        | 5.66  | 3200  | 0.3322          | 0.4013 | 0.0979 |
| 0.2143        | 6.37  | 3600  | 0.3370          | 0.3956 | 0.0972 |
| 0.1955        | 7.08  | 4000  | 0.3401          | 0.4033 | 0.0998 |
| 0.1955        | 7.79  | 4400  | 0.3375          | 0.3889 | 0.0962 |
| 0.1845        | 8.5   | 4800  | 0.3455          | 0.3752 | 0.0923 |
| 0.1752        | 9.2   | 5200  | 0.3336          | 0.3718 | 0.0925 |
| 0.1705        | 9.91  | 5600  | 0.3145          | 0.3653 | 0.0892 |
| 0.1585        | 10.62 | 6000  | 0.3410          | 0.3737 | 0.0922 |
| 0.1585        | 11.33 | 6400  | 0.3296          | 0.3664 | 0.0899 |
| 0.1474        | 12.04 | 6800  | 0.3492          | 0.3590 | 0.0899 |
| 0.1485        | 12.74 | 7200  | 0.3176          | 0.3506 | 0.0867 |
| 0.137         | 13.45 | 7600  | 0.3532          | 0.3600 | 0.0890 |
| 0.1291        | 14.16 | 8000  | 0.3318          | 0.3571 | 0.0873 |
| 0.1291        | 14.87 | 8400  | 0.3353          | 0.3548 | 0.0883 |
| 0.1274        | 15.58 | 8800  | 0.3235          | 0.3396 | 0.0823 |
| 0.1198        | 16.28 | 9200  | 0.3259          | 0.3389 | 0.0832 |
| 0.1164        | 16.99 | 9600  | 0.3263          | 0.3411 | 0.0844 |
| 0.1119        | 17.7  | 10000 | 0.3254          | 0.3377 | 0.0824 |
| 0.1119        | 18.41 | 10400 | 0.3243          | 0.3331 | 0.0812 |
| 0.1054        | 19.12 | 10800 | 0.3223          | 0.3239 | 0.0790 |
| 0.1017        | 19.82 | 11200 | 0.3054          | 0.3190 | 0.0774 |
| 0.0964        | 20.53 | 11600 | 0.3278          | 0.3237 | 0.0785 |
| 0.0903        | 21.24 | 12000 | 0.3167          | 0.3177 | 0.0774 |
| 0.0903        | 21.95 | 12400 | 0.3331          | 0.3124 | 0.0766 |
| 0.0886        | 22.65 | 12800 | 0.3099          | 0.3089 | 0.0745 |
| 0.0836        | 23.36 | 13200 | 0.3171          | 0.3048 | 0.0731 |
| 0.0796        | 24.07 | 13600 | 0.3158          | 0.3041 | 0.0733 |
| 0.0739        | 24.78 | 14000 | 0.3203          | 0.3003 | 0.0721 |
| 0.0739        | 25.49 | 14400 | 0.3138          | 0.2974 | 0.0713 |
| 0.0742        | 26.19 | 14800 | 0.3197          | 0.2959 | 0.0711 |
| 0.07          | 26.9  | 15200 | 0.3232          | 0.2952 | 0.0703 |
| 0.0654        | 27.61 | 15600 | 0.3243          | 0.2939 | 0.0701 |
| 0.0631        | 28.32 | 16000 | 0.3213          | 0.2876 | 0.0688 |
| 0.0631        | 29.03 | 16400 | 0.3151          | 0.2880 | 0.0685 |
| 0.0607        | 29.73 | 16800 | 0.3184          | 0.2867 | 0.0681 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.8.1.dev0
- Tokenizers 0.13.2
