---
license: apache-2.0
tags:
- generated_from_trainer
- automatic-speech-recognition
- NbAiLab/NPSC
- robust-speech-event
- false
- nb-NO
- hf-asr-leaderboard
datasets:
- NbAiLab/NPSC
language:
- nb-NO
model-index:
- name: wav2vec2-large-voxrex-npsc-bokmaal
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: NPSC
      type: NbAiLab/NPSC
      args: 16K_mp3_bokmaal
    metrics:
    - name: "Test (Bokm\xE5l) WER"
      type: wer
      value: 0.07028972259374369
    - name: "Test (Bokm\xE5l) CER"
      type: cer
      value: 0.026870600821650645
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-voxrex-npsc-bokmaal

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1311
- Wer: 0.1038

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 8.379967082059723e-06
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 0.1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.2127        | 0.32  | 500  | 0.1335          | 0.1047 |
| 0.1976        | 0.64  | 1000 | 0.1309          | 0.1039 |
| 0.1887        | 0.97  | 1500 | 0.1306          | 0.1040 |
| 0.18          | 1.29  | 2000 | 0.1311          | 0.1038 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu113
- Datasets 1.18.4.dev0
- Tokenizers 0.11.0
