---
language:
  - nl
license: apache-2.0
tags:
  - whisper-event
  - hf-asr-leaderboard
datasets:
  - mozilla-foundation/common_voice_11_0
metrics:
  - wer
model-index:
  - name: Whisper Medium nl - GeoffVdr
    results:
      - task:
          name: Automatic Speech Recognition
          type: automatic-speech-recognition
        dataset:
          name: mozilla-foundation/common_voice_11_0
          type: mozilla-foundation/common_voice_11_0
          config: nl
          split: test
          args: nl
        metrics:
          - name: Wer
            type: wer
            value: 7.514
co2_eq_emissions:
  emissions: 2930
  source: https://mlco2.github.io/impact/
  training_type: fine-tuning
  geographical_location: Ghent, Belgium
  hardware_used: 1 v100 GPU
---

# Whisper Medium nl - GeoffVdr

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the Common Voice 11.0 dataset.

## Model description
More information needed
## Intended uses & limitations
More information needed
## Training and evaluation data
- Training: Mozilla CommonVoice 11 Dutch train+validation set
- Evaluation: Mozilla CommonVoice 11 Dutch test set
## Training procedure

## Training Hyperparameters
- learning_rate: 1e-5
- train_batch_size: 8
- eval_batch_size: 8
- gradient_accumulation_steps: 2
- lr_scheduler_warmup_steps: 500
- training_steps: 12000

## Training Results

| Training Loss | Epoch | Step | WER  |
|:-------------:|:-----:|:----:|:----:|
| 0.1111        | 0.39  | 1000 | 9.89 |
| 0.0884        | 0.78  | 2000 | 9.26 |
| 0.0362        | 1.17  | 3000 | 8.64 |
| 0.0359        | 1.56  | 4000 | 8.60 |
| 0.0375        | 1.95  | 5000 | 8.24 |
:
:
| 0.0015        | 4.68  | 12000| 7.51 |


### Framework versions