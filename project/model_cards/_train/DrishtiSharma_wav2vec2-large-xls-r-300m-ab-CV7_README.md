---
language:
- ab
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_7_0
- generated_from_trainer
- ab
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_7_0
model-index:
- name: wav2vec2-large-xls-r-300m-ab-CV7
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 7
      type: mozilla-foundation/common_voice_7_0
      args: ab
    metrics:
    - name: Test WER
      type: wer
      value: 0.5291160452450775
    - name: Test CER
      type: cer
      value: 0.10630270750110964
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: ab
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

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 - AB dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5620
- Wer: 0.5651

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-ab-CV7 --dataset mozilla-foundation/common_voice_7_0 --config ab --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

NA



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
- lr_scheduler_warmup_steps: 2000
- num_epochs: 100.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 9.6445        | 13.64 | 300  | 4.3963          | 1.0    |
| 3.6459        | 27.27 | 600  | 3.2267          | 1.0    |
| 3.0978        | 40.91 | 900  | 3.0927          | 1.0    |
| 2.8357        | 54.55 | 1200 | 2.1462          | 1.0029 |
| 1.2723        | 68.18 | 1500 | 0.6747          | 0.6996 |
| 0.6528        | 81.82 | 1800 | 0.5928          | 0.6422 |
| 0.4905        | 95.45 | 2100 | 0.5587          | 0.5681 |


### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.17.1.dev0
- Tokenizers 0.11.0
