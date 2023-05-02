---
language:
- ha
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- robust-speech-event
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: ''
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8.0
      type: mozilla-foundation/common_voice_8_0
      args: ha
    metrics:
    - name: Test WER
      type: wer
      value: 51.31
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - HA dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4998
- Wer: 0.5153

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 9.6e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 80.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.0021        | 8.33  | 500  | 2.9059          | 1.0    |
| 2.6604        | 16.66 | 1000 | 2.6402          | 0.9892 |
| 1.2216        | 24.99 | 1500 | 0.6051          | 0.6851 |
| 1.0754        | 33.33 | 2000 | 0.5408          | 0.6464 |
| 0.9582        | 41.66 | 2500 | 0.5521          | 0.5935 |
| 0.8653        | 49.99 | 3000 | 0.5156          | 0.5550 |
| 0.7867        | 58.33 | 3500 | 0.5439          | 0.5606 |
| 0.7265        | 66.66 | 4000 | 0.4863          | 0.5255 |
| 0.6699        | 74.99 | 4500 | 0.5050          | 0.5169 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu113
- Datasets 1.18.4.dev0
- Tokenizers 0.11.0
