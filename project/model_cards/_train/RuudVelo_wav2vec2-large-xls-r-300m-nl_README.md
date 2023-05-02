---
language:
- nl
license: apache-2.0
tags:
- automatic-speech-recognition
- common_voice
- generated_from_trainer
- hf-asr-leaderboard
- model_for_talk
- nl
- robust-speech-event
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xls-r-300m-nl
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: common_voice
      type: common_voice
      args: nl
    metrics:
    - name: Test WER
      type: wer
      value: 17.17
    - name: Test CER
      type: cer
      value: 5.13
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: nl
    metrics:
    - name: Test WER
      type: wer
      value: 35.76
    - name: Test CER
      type: cer
      value: 13.99
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: nl
    metrics:
    - name: Test WER
      type: wer
      value: 37.19
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-nl

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the test set:
- Loss: 0.3923
- Wer: 0.1748

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 1.5787        | 0.89  | 400   | 0.6354          | 0.5643 |
| 0.3036        | 1.78  | 800   | 0.3690          | 0.3552 |
| 0.188         | 2.67  | 1200  | 0.3239          | 0.2958 |
| 0.1434        | 3.56  | 1600  | 0.3093          | 0.2515 |
| 0.1245        | 4.44  | 2000  | 0.3024          | 0.2433 |
| 0.1095        | 5.33  | 2400  | 0.3249          | 0.2643 |
| 0.0979        | 6.22  | 2800  | 0.3191          | 0.2281 |
| 0.0915        | 7.11  | 3200  | 0.3152          | 0.2216 |
| 0.0829        | 8.0   | 3600  | 0.3419          | 0.2218 |
| 0.0777        | 8.89  | 4000  | 0.3432          | 0.2132 |
| 0.073         | 9.78  | 4400  | 0.3223          | 0.2131 |
| 0.0688        | 10.67 | 4800  | 0.3094          | 0.2152 |
| 0.0647        | 11.56 | 5200  | 0.3411          | 0.2152 |
| 0.0639        | 12.44 | 5600  | 0.3762          | 0.2135 |
| 0.0599        | 13.33 | 6000  | 0.3790          | 0.2137 |
| 0.0572        | 14.22 | 6400  | 0.3693          | 0.2118 |
| 0.0563        | 15.11 | 6800  | 0.3495          | 0.2139 |
| 0.0521        | 16.0  | 7200  | 0.3800          | 0.2023 |
| 0.0508        | 16.89 | 7600  | 0.3678          | 0.2033 |
| 0.0513        | 17.78 | 8000  | 0.3845          | 0.1987 |
| 0.0476        | 18.67 | 8400  | 0.3511          | 0.2037 |
| 0.045         | 19.56 | 8800  | 0.3794          | 0.1994 |
| 0.044         | 20.44 | 9200  | 0.3525          | 0.2050 |
| 0.043         | 21.33 | 9600  | 0.4082          | 0.2007 |
| 0.0409        | 22.22 | 10000 | 0.3866          | 0.2004 |
| 0.0393        | 23.11 | 10400 | 0.3899          | 0.2008 |
| 0.0382        | 24.0  | 10800 | 0.3626          | 0.1951 |
| 0.039         | 24.89 | 11200 | 0.3936          | 0.1953 |
| 0.0361        | 25.78 | 11600 | 0.4262          | 0.1928 |
| 0.0362        | 26.67 | 12000 | 0.3796          | 0.1934 |
| 0.033         | 27.56 | 12400 | 0.3616          | 0.1934 |
| 0.0321        | 28.44 | 12800 | 0.3742          | 0.1933 |
| 0.0325        | 29.33 | 13200 | 0.3582          | 0.1869 |
| 0.0309        | 30.22 | 13600 | 0.3717          | 0.1874 |
| 0.029         | 31.11 | 14000 | 0.3814          | 0.1894 |
| 0.0296        | 32.0  | 14400 | 0.3698          | 0.1877 |
| 0.0281        | 32.89 | 14800 | 0.3976          | 0.1899 |
| 0.0275        | 33.78 | 15200 | 0.3854          | 0.1858 |
| 0.0264        | 34.67 | 15600 | 0.4021          | 0.1889 |
| 0.0261        | 35.56 | 16000 | 0.3850          | 0.1830 |
| 0.0242        | 36.44 | 16400 | 0.4091          | 0.1878 |
| 0.0245        | 37.33 | 16800 | 0.4012          | 0.1846 |
| 0.0243        | 38.22 | 17200 | 0.3996          | 0.1833 |
| 0.0223        | 39.11 | 17600 | 0.3962          | 0.1815 |
| 0.0223        | 40.0  | 18000 | 0.3898          | 0.1832 |
| 0.0219        | 40.89 | 18400 | 0.4019          | 0.1822 |
| 0.0211        | 41.78 | 18800 | 0.4035          | 0.1809 |
| 0.021         | 42.67 | 19200 | 0.3915          | 0.1826 |
| 0.0208        | 43.56 | 19600 | 0.3934          | 0.1784 |
| 0.0188        | 44.44 | 20000 | 0.3912          | 0.1787 |
| 0.0195        | 45.33 | 20400 | 0.3989          | 0.1766 |
| 0.0186        | 46.22 | 20800 | 0.3887          | 0.1773 |
| 0.0188        | 47.11 | 21200 | 0.3982          | 0.1758 |
| 0.0175        | 48.0  | 21600 | 0.3933          | 0.1755 |
| 0.0172        | 48.89 | 22000 | 0.3921          | 0.1749 |
| 0.0187        | 49.78 | 22400 | 0.3923          | 0.1748 |


### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.17.1.dev0
- Tokenizers 0.11.0
