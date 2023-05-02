---
license: apache-2.0
tags:
- generated_from_trainer
- automatic-speech-recognition
- NbAiLab/NPSC
- robust-speech-event
- "no"
- nn-NO
- hf-asr-leaderboard
datasets:
- NbAiLab/NPSC
language:
- nn-NO
model-index:
- name: wav2vec2-large-voxrex-npsc-nynorsk
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: NPSC
      type: NbAiLab/NPSC
      args: 16K_mp3_nynorsk
    metrics:
    - name: Test (Nynorsk) WER
      type: wer
      value: 0.12220762155059132
    - name: Test (Nynorsk) CER
      type: cer
      value: 0.04195612578778549
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-voxrex-npsc-nynorsk

This model is a fine-tuned version of [KBLab/wav2vec2-large-voxrex](https://huggingface.co/KBLab/wav2vec2-large-voxrex) on the NBAILAB/NPSC - 16K_MP3_NYNORSK dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4142
- Wer: 0.1576

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 40.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.086         | 2.17  | 500  | 3.0773          | 1.0    |
| 2.8532        | 4.35  | 1000 | 2.8393          | 1.0    |
| 0.9738        | 6.52  | 1500 | 0.7283          | 0.4890 |
| 0.6763        | 8.7   | 2000 | 0.5340          | 0.3662 |
| 0.5303        | 10.87 | 2500 | 0.4521          | 0.3140 |
| 0.4765        | 13.04 | 3000 | 0.4181          | 0.2853 |
| 0.4219        | 15.22 | 3500 | 0.4156          | 0.2934 |
| 0.3564        | 17.39 | 4000 | 0.3925          | 0.2509 |
| 0.3282        | 19.57 | 4500 | 0.3824          | 0.2420 |
| 0.3118        | 21.74 | 5000 | 0.3636          | 0.2354 |
| 0.2919        | 23.91 | 5500 | 0.3615          | 0.2281 |
| 0.2961        | 26.09 | 6000 | 0.3548          | 0.2255 |
| 0.284         | 28.26 | 6500 | 0.3526          | 0.2209 |
| 0.2566        | 30.43 | 7000 | 0.3526          | 0.2205 |
| 0.2422        | 32.61 | 7500 | 0.3569          | 0.2173 |
| 0.2472        | 34.78 | 8000 | 0.3592          | 0.2166 |
| 0.2337        | 36.96 | 8500 | 0.3625          | 0.2172 |
| 0.2315        | 39.13 | 9000 | 0.3580          | 0.2155 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3
