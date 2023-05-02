---
language:
- tt
license: apache-2.0
tags:
- whisper-event
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Tiny Tatar - Kirill Milintsevich
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 tt
      type: mozilla-foundation/common_voice_11_0
      config: tt
      split: test
      args: tt
    metrics:
    - name: Wer
      type: wer
      value: 49.228482446206115
---

# Whisper Tiny Tatar - Kirill Milintsevich

This model is a fine-tuned version of [openai/whisper-tiny](https://huggingface.co/openai/whisper-tiny) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5106
- Wer: 49.2285

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 64
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP
### Training results
| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.4268        | 2.49  | 500  | 0.6232          | 63.6537 |
| 0.2331        | 4.98  | 1000 | 0.5044          | 52.3818 |
| 0.1332        | 7.46  | 1500 | 0.4927          | 50.2300 |
| 0.09          | 9.95  | 2000 | 0.5106          | 49.2285 |
| 0.048         | 12.44 | 2500 | 0.5526          | 49.7806 |
| 0.0346        | 14.93 | 3000 | 0.5850          | 50.0319 |
| 0.0181        | 17.41 | 3500 | 0.6276          | 50.5592 |
| 0.0122        | 19.9  | 4000 | 0.6494          | 50.3327 |
| 0.0086        | 22.39 | 4500 | 0.6737          | 50.6688 |
| 0.0077        | 24.88 | 5000 | 0.6777          | 50.6724 |