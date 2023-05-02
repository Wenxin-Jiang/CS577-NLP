---
language:
- pa-IN
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- pa-IN
- robust-speech-event
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-pa-IN-dx1
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: pa-IN
    metrics:
    - name: Test WER
      type: wer
      value: 0.48725989807918463
    - name: Test CER
      type: cer
      value: 0.1687305197540224
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: pa-IN
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

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - PA-IN dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0855
- Wer: 0.4755


### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-pa-IN-dx1 --dataset mozilla-foundation/common_voice_8_0 --config pa-IN --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

Punjabi language isn't available in speech-recognition-community-v2/dev_data


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1200
- num_epochs: 100.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.4607        | 9.26  | 500  | 2.7746          | 1.0416 |
| 0.3442        | 18.52 | 1000 | 0.9114          | 0.5911 |
| 0.2213        | 27.78 | 1500 | 0.9687          | 0.5751 |
| 0.1242        | 37.04 | 2000 | 1.0204          | 0.5461 |
| 0.0998        | 46.3  | 2500 | 1.0250          | 0.5233 |
| 0.0727        | 55.56 | 3000 | 1.1072          | 0.5382 |
| 0.0605        | 64.81 | 3500 | 1.0588          | 0.5073 |
| 0.0458        | 74.07 | 4000 | 1.0818          | 0.5069 |
| 0.0338        | 83.33 | 4500 | 1.0948          | 0.5108 |
| 0.0223        | 92.59 | 5000 | 1.0986          | 0.4775 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0
