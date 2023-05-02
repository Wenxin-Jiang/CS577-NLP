---
language:
- sr
license: apache-2.0
tags:
- automatic-speech-recognition
- generated_from_trainer
- hf-asr-leaderboard
- model_for_talk
- mozilla-foundation/common_voice_8_0
- robust-speech-event
- sr
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-sr-v4
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: sr
    metrics:
    - name: Test WER
      type: wer
      value: 0.303313
    - name: Test CER
      type: cer
      value: 0.1048951
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: sr
    metrics:
    - name: Test WER
      type: wer
      value: 0.9486784706184245
    - name: Test CER
      type: cer
      value: 0.8084369606584945
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: sr
    metrics:
    - name: Test WER
      type: wer
      value: 94.53
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-sr-v4

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - SR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5570
- Wer: 0.3038

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-sr-v4 --dataset mozilla-foundation/common_voice_8_0 --config sr --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-sr-v4 --dataset speech-recognition-community-v2/dev_data --config sr --split validation --chunk_length_s 10 --stride_length_s 1

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
- lr_scheduler_warmup_steps: 800
- num_epochs: 200
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 8.2934        | 7.5   | 300  | 2.9777          | 0.9995 |
| 1.5049        | 15.0  | 600  | 0.5036          | 0.4806 |
| 0.3263        | 22.5  | 900  | 0.5822          | 0.4055 |
| 0.2008        | 30.0  | 1200 | 0.5609          | 0.4032 |
| 0.1543        | 37.5  | 1500 | 0.5203          | 0.3710 |
| 0.1158        | 45.0  | 1800 | 0.6458          | 0.3985 |
| 0.0997        | 52.5  | 2100 | 0.6227          | 0.4013 |
| 0.0834        | 60.0  | 2400 | 0.6048          | 0.3836 |
| 0.0665        | 67.5  | 2700 | 0.6197          | 0.3686 |
| 0.0602        | 75.0  | 3000 | 0.5418          | 0.3453 |
| 0.0524        | 82.5  | 3300 | 0.5310          | 0.3486 |
| 0.0445        | 90.0  | 3600 | 0.5599          | 0.3374 |
| 0.0406        | 97.5  | 3900 | 0.5958          | 0.3327 |
| 0.0358        | 105.0 | 4200 | 0.6017          | 0.3262 |
| 0.0302        | 112.5 | 4500 | 0.5613          | 0.3248 |
| 0.0285        | 120.0 | 4800 | 0.5659          | 0.3462 |
| 0.0213        | 127.5 | 5100 | 0.5568          | 0.3206 |
| 0.0215        | 135.0 | 5400 | 0.6524          | 0.3472 |
| 0.0162        | 142.5 | 5700 | 0.6223          | 0.3458 |
| 0.0137        | 150.0 | 6000 | 0.6625          | 0.3313 |
| 0.0114        | 157.5 | 6300 | 0.5739          | 0.3336 |
| 0.0101        | 165.0 | 6600 | 0.5906          | 0.3285 |
| 0.008         | 172.5 | 6900 | 0.5982          | 0.3112 |
| 0.0076        | 180.0 | 7200 | 0.5399          | 0.3094 |
| 0.0071        | 187.5 | 7500 | 0.5387          | 0.2991 |
| 0.0057        | 195.0 | 7800 | 0.5570          | 0.3038 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.2
- Tokenizers 0.11.0
