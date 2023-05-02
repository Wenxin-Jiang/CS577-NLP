---
language:
- as
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- as
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-as-g1
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: as
    metrics:
    - name: Test WER
      type: wer
      value: 0.6540934419202743
    - name: Test CER
      type: cer
      value: 0.21454042646095625
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: as
    metrics:
    - name: Test WER
      type: wer
      value: NA
    - name: Test CER
      type: cer
      value: NA
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-as-g1

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - AS dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3327
- Wer: 0.5744

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-as-g1 --dataset mozilla-foundation/common_voice_8_0 --config as --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

Assamese language isn't available in speech-recognition-community-v2/dev_data

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 200
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 14.1958       | 5.26   | 100  | 7.1919          | 1.0    |
| 5.0035        | 10.51  | 200  | 3.9362          | 1.0    |
| 3.6193        | 15.77  | 300  | 3.4451          | 1.0    |
| 3.4852        | 21.05  | 400  | 3.3536          | 1.0    |
| 2.8489        | 26.31  | 500  | 1.6451          | 0.9100 |
| 0.9568        | 31.56  | 600  | 1.0514          | 0.7561 |
| 0.4865        | 36.82  | 700  | 1.0434          | 0.7184 |
| 0.322         | 42.1   | 800  | 1.0825          | 0.7210 |
| 0.2383        | 47.36  | 900  | 1.1304          | 0.6897 |
| 0.2136        | 52.62  | 1000 | 1.1150          | 0.6854 |
| 0.179         | 57.87  | 1100 | 1.2453          | 0.6875 |
| 0.1539        | 63.15  | 1200 | 1.2211          | 0.6704 |
| 0.1303        | 68.41  | 1300 | 1.2859          | 0.6747 |
| 0.1183        | 73.67  | 1400 | 1.2775          | 0.6721 |
| 0.0994        | 78.92  | 1500 | 1.2321          | 0.6404 |
| 0.0991        | 84.21  | 1600 | 1.2766          | 0.6524 |
| 0.0887        | 89.46  | 1700 | 1.3026          | 0.6344 |
| 0.0754        | 94.72  | 1800 | 1.3199          | 0.6704 |
| 0.0693        | 99.97  | 1900 | 1.3044          | 0.6361 |
| 0.0568        | 105.26 | 2000 | 1.3541          | 0.6254 |
| 0.0536        | 110.51 | 2100 | 1.3320          | 0.6249 |
| 0.0529        | 115.77 | 2200 | 1.3370          | 0.6271 |
| 0.048         | 121.05 | 2300 | 1.2757          | 0.6031 |
| 0.0419        | 126.31 | 2400 | 1.2661          | 0.6172 |
| 0.0349        | 131.56 | 2500 | 1.2897          | 0.6048 |
| 0.0309        | 136.82 | 2600 | 1.2688          | 0.5962 |
| 0.0278        | 142.1  | 2700 | 1.2885          | 0.5954 |
| 0.0254        | 147.36 | 2800 | 1.2988          | 0.5915 |
| 0.0223        | 152.62 | 2900 | 1.3153          | 0.5941 |
| 0.0216        | 157.87 | 3000 | 1.2936          | 0.5937 |
| 0.0186        | 163.15 | 3100 | 1.2906          | 0.5877 |
| 0.0156        | 168.41 | 3200 | 1.3476          | 0.5962 |
| 0.0158        | 173.67 | 3300 | 1.3363          | 0.5847 |
| 0.0142        | 178.92 | 3400 | 1.3367          | 0.5847 |
| 0.0153        | 184.21 | 3500 | 1.3105          | 0.5757 |
| 0.0119        | 189.46 | 3600 | 1.3255          | 0.5705 |
| 0.0115        | 194.72 | 3700 | 1.3340          | 0.5787 |
| 0.0103        | 199.97 | 3800 | 1.3327          | 0.5744 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
