---
language: fi
datasets:
- mozilla-foundation/common_voice_7_0
metrics:
- wer
- cer
tags:
- generated_from_trainer
- mozilla-foundation/common_voice_7_0
- audio
- automatic-speech-recognition
- speech
- robust-speech-event
- hf-asr-leaderboard
model-index:
- name: XLS-R 1B Wav2Vec2 Finnish by Rasmus Toivanen
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 7
      type: mozilla-foundation/common_voice_7_0
      args: fi
    metrics:
    - name: Test WER
      type: wer
      value: 10.96
    - name: Test CER
      type: cer
      value: 2.81
---
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xlsr-fi-train-aug-lm-1B

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1499
- Wer: 0.1955

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.6473        | 0.29  | 400  | 0.2857          | 0.3825 |
| 0.6039        | 0.58  | 800  | 0.2459          | 0.3476 |
| 0.4757        | 0.87  | 1200 | 0.2338          | 0.3274 |
| 0.4473        | 1.15  | 1600 | 0.2246          | 0.3128 |
| 0.4322        | 1.44  | 2000 | 0.1962          | 0.2805 |
| 0.3961        | 1.73  | 2400 | 0.2070          | 0.2797 |
| 0.3642        | 2.02  | 2800 | 0.1790          | 0.2473 |
| 0.3561        | 2.31  | 3200 | 0.1769          | 0.2375 |
| 0.282         | 2.6   | 3600 | 0.1672          | 0.2263 |
| 0.2978        | 2.89  | 4000 | 0.1636          | 0.2192 |
| 0.2722        | 3.17  | 4400 | 0.1637          | 0.2102 |
| 0.2924        | 3.46  | 4800 | 0.1506          | 0.2021 |
| 0.2631        | 3.75  | 5200 | 0.1499          | 0.1955 |


### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.1+cu102
- Datasets 1.17.1.dev0
- Tokenizers 0.11.0
