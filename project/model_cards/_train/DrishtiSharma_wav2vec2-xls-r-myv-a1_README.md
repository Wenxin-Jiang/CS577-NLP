---
language:
- myv
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- myv
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-xls-r-myv-a1
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: myv
    metrics:
    - name: Test WER
      type: wer
      value: 0.6514672686230248
    - name: Test CER
      type: cer
      value: 0.17226131905088124
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: vot
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

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - MYV dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0356
- Wer: 0.6524

### Evaluation Commands

**1. To evaluate on mozilla-foundation/common_voice_8_0 with test split**

python eval.py  --model_id DrishtiSharma/wav2vec2-xls-r-myv-a1 --dataset mozilla-foundation/common_voice_8_0 --config myv --split test --log_outputs

**2. To evaluate on speech-recognition-community-v2/dev_data**

Erzya language not found in speech-recognition-community-v2/dev_data

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0004
- train_batch_size: 16
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 800
- num_epochs: 200.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step  | Validation Loss | Wer    |
|:-------------:|:------:|:-----:|:---------------:|:------:|
| 5.649         | 9.62   | 500   | 3.0038          | 1.0    |
| 1.6272        | 19.23  | 1000  | 0.7362          | 0.7819 |
| 1.1354        | 28.85  | 1500  | 0.6410          | 0.7111 |
| 1.0424        | 38.46  | 2000  | 0.6907          | 0.7431 |
| 0.9293        | 48.08  | 2500  | 0.7249          | 0.7102 |
| 0.8246        | 57.69  | 3000  | 0.7422          | 0.6966 |
| 0.7837        | 67.31  | 3500  | 0.7413          | 0.6813 |
| 0.7147        | 76.92  | 4000  | 0.7873          | 0.6930 |
| 0.6276        | 86.54  | 4500  | 0.8038          | 0.6677 |
| 0.6041        | 96.15  | 5000  | 0.8240          | 0.6831 |
| 0.5336        | 105.77 | 5500  | 0.8748          | 0.6749 |
| 0.4705        | 115.38 | 6000  | 0.9006          | 0.6497 |
| 0.43          | 125.0  | 6500  | 0.8954          | 0.6551 |
| 0.3859        | 134.62 | 7000  | 0.9074          | 0.6614 |
| 0.3342        | 144.23 | 7500  | 0.9693          | 0.6560 |
| 0.3155        | 153.85 | 8000  | 1.0073          | 0.6691 |
| 0.2673        | 163.46 | 8500  | 1.0170          | 0.6632 |
| 0.2409        | 173.08 | 9000  | 1.0304          | 0.6709 |
| 0.2189        | 182.69 | 9500  | 0.9965          | 0.6546 |
| 0.1973        | 192.31 | 10000 | 1.0360          | 0.6551 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0


### Evaluation Command

!python eval.py \
    --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-myv-v1 \
    --dataset mozilla-foundation/common_voice_8_0 --config myv --split test --log_outputs