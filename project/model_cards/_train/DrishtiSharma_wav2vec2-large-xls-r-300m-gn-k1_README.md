---
language:
- gn
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- gn
- robust-speech-event
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-gn-k1
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: gn
    metrics:
    - name: Test WER
      type: wer
      value: 0.711890243902439
    - name: Test CER
      type: cer
      value: 0.13311897106109324
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: gn
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

# wav2vec2-large-xls-r-300m-gn-k1

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - GN dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9220
- Wer: 0.6631

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-gn-k1 --dataset mozilla-foundation/common_voice_8_0 --config gn --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

NA

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.00018
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 600
- num_epochs: 200
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 15.9402       | 8.32   | 100  | 6.9185          | 1.0    |
| 4.6367        | 16.64  | 200  | 3.7416          | 1.0    |
| 3.4337        | 24.96  | 300  | 3.2581          | 1.0    |
| 3.2307        | 33.32  | 400  | 2.8008          | 1.0    |
| 1.3182        | 41.64  | 500  | 0.8359          | 0.8171 |
| 0.409         | 49.96  | 600  | 0.8470          | 0.8323 |
| 0.2573        | 58.32  | 700  | 0.7823          | 0.7576 |
| 0.1969        | 66.64  | 800  | 0.8306          | 0.7424 |
| 0.1469        | 74.96  | 900  | 0.9225          | 0.7713 |
| 0.1172        | 83.32  | 1000 | 0.7903          | 0.6951 |
| 0.1017        | 91.64  | 1100 | 0.8519          | 0.6921 |
| 0.0851        | 99.96  | 1200 | 0.8129          | 0.6646 |
| 0.071         | 108.32 | 1300 | 0.8614          | 0.7043 |
| 0.061         | 116.64 | 1400 | 0.8414          | 0.6921 |
| 0.0552        | 124.96 | 1500 | 0.8649          | 0.6905 |
| 0.0465        | 133.32 | 1600 | 0.8575          | 0.6646 |
| 0.0381        | 141.64 | 1700 | 0.8802          | 0.6723 |
| 0.0338        | 149.96 | 1800 | 0.8731          | 0.6845 |
| 0.0306        | 158.32 | 1900 | 0.9003          | 0.6585 |
| 0.0236        | 166.64 | 2000 | 0.9408          | 0.6616 |
| 0.021         | 174.96 | 2100 | 0.9353          | 0.6723 |
| 0.0212        | 183.32 | 2200 | 0.9269          | 0.6570 |
| 0.0191        | 191.64 | 2300 | 0.9277          | 0.6662 |
| 0.0161        | 199.96 | 2400 | 0.9220          | 0.6631 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
