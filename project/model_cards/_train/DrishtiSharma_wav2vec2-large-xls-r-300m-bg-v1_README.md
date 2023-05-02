---
language:
- bg
license: apache-2.0
tags:
- automatic-speech-recognition
- bg
- generated_from_trainer
- hf-asr-leaderboard
- model_for_talk
- mozilla-foundation/common_voice_8_0
- robust-speech-event
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-bg-v1
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: bg
    metrics:
    - name: Test WER
      type: wer
      value: 0.4709579127785184
    - name: Test CER
      type: cer
      value: 0.10205125354383235
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: bg
    metrics:
    - name: Test WER
      type: wer
      value: 0.7053128872366791
    - name: Test CER
      type: cer
      value: 0.210804311998487
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: bg
    metrics:
    - name: Test WER
      type: wer
      value: 72.6
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - BG dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5197
- Wer: 0.4689

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-bg-v1 --dataset mozilla-foundation/common_voice_8_0 --config bg --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-bg-v1 --dataset speech-recognition-community-v2/dev_data --config bg --split validation --chunk_length_s 10 --stride_length_s 1

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7e-05
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 50.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 4.3711        | 2.61  | 300  | 4.3122          | 1.0    |
| 3.1653        | 5.22  | 600  | 3.1156          | 1.0    |
| 2.8904        | 7.83  | 900  | 2.8421          | 0.9918 |
| 0.9207        | 10.43 | 1200 | 0.9895          | 0.8689 |
| 0.6384        | 13.04 | 1500 | 0.6994          | 0.7700 |
| 0.5215        | 15.65 | 1800 | 0.5628          | 0.6443 |
| 0.4573        | 18.26 | 2100 | 0.5316          | 0.6174 |
| 0.3875        | 20.87 | 2400 | 0.4932          | 0.5779 |
| 0.3562        | 23.48 | 2700 | 0.4972          | 0.5475 |
| 0.3218        | 26.09 | 3000 | 0.4895          | 0.5219 |
| 0.2954        | 28.7  | 3300 | 0.5226          | 0.5192 |
| 0.287         | 31.3  | 3600 | 0.4957          | 0.5146 |
| 0.2587        | 33.91 | 3900 | 0.4944          | 0.4893 |
| 0.2496        | 36.52 | 4200 | 0.4976          | 0.4895 |
| 0.2365        | 39.13 | 4500 | 0.5185          | 0.4819 |
| 0.2264        | 41.74 | 4800 | 0.5152          | 0.4776 |
| 0.2224        | 44.35 | 5100 | 0.5031          | 0.4746 |
| 0.2096        | 46.96 | 5400 | 0.5062          | 0.4708 |
| 0.2038        | 49.57 | 5700 | 0.5217          | 0.4698 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0
