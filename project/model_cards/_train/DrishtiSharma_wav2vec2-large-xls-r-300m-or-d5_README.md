---
language:
- or
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- or
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-or-d5
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: or
    metrics:
    - name: Test WER
      type: wer
      value: 0.579136690647482
    - name: Test CER
      type: cer
      value: 0.1572148018392818
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: or
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

# wav2vec2-large-xls-r-300m-or-d5

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - OR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9571
- Wer: 0.5450

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-or-d5 --dataset mozilla-foundation/common_voice_8_0 --config or --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-or-d5 --dataset speech-recognition-community-v2/dev_data --config or --split validation --chunk_length_s 10 --stride_length_s 1

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.000111
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
| 9.2958        | 12.5  | 300  | 4.9014          | 1.0    |
| 3.4065        | 25.0  | 600  | 3.5150          | 1.0    |
| 1.5402        | 37.5  | 900  | 0.8356          | 0.7249 |
| 0.6049        | 50.0  | 1200 | 0.7754          | 0.6349 |
| 0.4074        | 62.5  | 1500 | 0.7994          | 0.6217 |
| 0.3097        | 75.0  | 1800 | 0.8815          | 0.5985 |
| 0.2593        | 87.5  | 2100 | 0.8532          | 0.5754 |
| 0.2097        | 100.0 | 2400 | 0.9077          | 0.5648 |
| 0.1784        | 112.5 | 2700 | 0.9047          | 0.5668 |
| 0.1567        | 125.0 | 3000 | 0.9019          | 0.5728 |
| 0.1315        | 137.5 | 3300 | 0.9295          | 0.5827 |
| 0.1125        | 150.0 | 3600 | 0.9256          | 0.5681 |
| 0.1035        | 162.5 | 3900 | 0.9148          | 0.5496 |
| 0.0901        | 175.0 | 4200 | 0.9480          | 0.5483 |
| 0.0817        | 187.5 | 4500 | 0.9799          | 0.5516 |
| 0.079         | 200.0 | 4800 | 0.9571          | 0.5450 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0



