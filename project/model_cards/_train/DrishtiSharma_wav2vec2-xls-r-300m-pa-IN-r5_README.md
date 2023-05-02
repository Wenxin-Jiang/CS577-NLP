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
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-xls-r-300m-pa-IN-r5
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
      value: 0.4186593492747942
    - name: Test CER
      type: cer
      value: 0.13301322550753938
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
- Loss: 0.8881
- Wer: 0.4175

### Evaluation Commands


1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-xls-r-300m-pa-IN-r5 --dataset mozilla-foundation/common_voice_8_0 --config pa-IN --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

Punjabi language isn't available in speech-recognition-community-v2/dev_data


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.000111
- train_batch_size: 16
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 200.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 10.695        | 18.52  | 500  | 3.5681          | 1.0    |
| 3.2718        | 37.04  | 1000 | 2.3081          | 0.9643 |
| 0.8727        | 55.56  | 1500 | 0.7227          | 0.5147 |
| 0.3349        | 74.07  | 2000 | 0.7498          | 0.4959 |
| 0.2134        | 92.59  | 2500 | 0.7779          | 0.4720 |
| 0.1445        | 111.11 | 3000 | 0.8120          | 0.4594 |
| 0.1057        | 129.63 | 3500 | 0.8225          | 0.4610 |
| 0.0826        | 148.15 | 4000 | 0.8307          | 0.4351 |
| 0.0639        | 166.67 | 4500 | 0.8967          | 0.4316 |
| 0.0528        | 185.19 | 5000 | 0.8875          | 0.4238 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0
