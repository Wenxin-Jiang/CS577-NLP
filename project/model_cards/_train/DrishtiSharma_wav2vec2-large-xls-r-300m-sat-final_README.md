---
language:
- sat
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- sat
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-sat-final
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: sat
    metrics:
    - name: Test WER
      type: wer
      value: 0.3493975903614458
    - name: Test CER
      type: cer
      value: 0.13773314203730272
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: sat
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

# wav2vec2-large-xls-r-300m-sat-final

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - SAT dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8012
- Wer: 0.3815

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-sat-final --dataset mozilla-foundation/common_voice_8_0 --config sat --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-sat-final --dataset speech-recognition-community-v2/dev_data --config sat --split validation --chunk_length_s 10 --stride_length_s 1

**Note: Santali (Ol Chiki) language not found in speech-recognition-community-v2/dev_data**


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0004
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 170
- num_epochs: 200
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 10.6317       | 33.29  | 100  | 2.8629          | 1.0    |
| 2.047         | 66.57  | 200  | 0.9516          | 0.5703 |
| 0.4475        | 99.86  | 300  | 0.8539          | 0.3896 |
| 0.0716        | 133.29 | 400  | 0.8277          | 0.3454 |
| 0.047         | 166.57 | 500  | 0.7597          | 0.3655 |
| 0.0249        | 199.86 | 600  | 0.8012          | 0.3815 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
