---
language:
- mt
license: apache-2.0
tags:
- automatic-speech-recognition
- generated_from_trainer
- hf-asr-leaderboard
- model_for_talk
- mozilla-foundation/common_voice_8_0
- mt
- robust-speech-event
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: wav2vec2-large-xls-r-300m-maltese
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: mt
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-maltese

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - MT dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2994
- Wer: 0.2781

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7e-05
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1800
- num_epochs: 100.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 3.0174        | 9.01  | 1000  | 3.0552          | 1.0    |
| 1.0446        | 18.02 | 2000  | 0.6708          | 0.7577 |
| 0.7995        | 27.03 | 3000  | 0.4202          | 0.4770 |
| 0.6978        | 36.04 | 4000  | 0.3054          | 0.3494 |
| 0.6189        | 45.05 | 5000  | 0.2878          | 0.3154 |
| 0.5667        | 54.05 | 6000  | 0.3114          | 0.3286 |
| 0.5173        | 63.06 | 7000  | 0.3085          | 0.3021 |
| 0.4682        | 72.07 | 8000  | 0.3058          | 0.2969 |
| 0.451         | 81.08 | 9000  | 0.3146          | 0.2907 |
| 0.4213        | 90.09 | 10000 | 0.3030          | 0.2881 |
| 0.4005        | 99.1  | 11000 | 0.3001          | 0.2789 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0

### Evaluation Script

!python eval.py \
    --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-maltese \
    --dataset mozilla-foundation/common_voice_8_0 --config mt --split test --log_outputs