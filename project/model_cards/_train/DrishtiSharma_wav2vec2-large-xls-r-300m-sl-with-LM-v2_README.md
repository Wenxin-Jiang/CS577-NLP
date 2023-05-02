---
language:
- sl
license: apache-2.0
tags:
- automatic-speech-recognition
- generated_from_trainer
- hf-asr-leaderboard
- model_for_talk
- mozilla-foundation/common_voice_8_0
- robust-speech-event
- sl
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-sl-with-LM-v2
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: sl
    metrics:
    - name: Test WER
      type: wer
      value: 0.21695212999560826
    - name: Test CER
      type: cer
      value: 0.052850080572474256
    - name: Test WER (+LM)
      type: wer
      value: 0.14551310203484116
    - name: Test CER (+LM)
      type: cer
      value: 0.03927566711277415
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: sl
    metrics:
    - name: Dev WER
      type: wer
      value: 0.560722380639029
    - name: Dev CER
      type: cer
      value: 0.2279626093074681
    - name: Dev WER (+LM)
      type: wer
      value: 0.46486802661402354
    - name: Dev CER (+LM)
      type: cer
      value: 0.21105136194592422
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: sl
    metrics:
    - name: Test WER
      type: wer
      value: 46.69
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - SL dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2855
- Wer: 0.2401

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-sl-with-LM-v2 --dataset mozilla-foundation/common_voice_8_0 --config sl --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-sl-with-LM-v2 --dataset speech-recognition-community-v2/dev_data --config sl --split validation --chunk_length_s 10 --stride_length_s 1

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 100.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 6.9294        | 6.1   | 500  | 2.9712          | 1.0    |
| 2.8305        | 12.2  | 1000 | 1.7073          | 0.9479 |
| 1.4795        | 18.29 | 1500 | 0.5756          | 0.6397 |
| 1.3433        | 24.39 | 2000 | 0.4968          | 0.5424 |
| 1.1766        | 30.49 | 2500 | 0.4185          | 0.4743 |
| 1.0017        | 36.59 | 3000 | 0.3303          | 0.3578 |
| 0.9358        | 42.68 | 3500 | 0.3003          | 0.3051 |
| 0.8358        | 48.78 | 4000 | 0.3045          | 0.2884 |
| 0.7647        | 54.88 | 4500 | 0.2866          | 0.2677 |
| 0.7482        | 60.98 | 5000 | 0.2829          | 0.2585 |
| 0.6943        | 67.07 | 5500 | 0.2782          | 0.2478 |
| 0.6586        | 73.17 | 6000 | 0.2911          | 0.2537 |
| 0.6425        | 79.27 | 6500 | 0.2817          | 0.2462 |
| 0.6067        | 85.37 | 7000 | 0.2910          | 0.2436 |
| 0.5974        | 91.46 | 7500 | 0.2875          | 0.2430 |
| 0.5812        | 97.56 | 8000 | 0.2852          | 0.2396 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0
