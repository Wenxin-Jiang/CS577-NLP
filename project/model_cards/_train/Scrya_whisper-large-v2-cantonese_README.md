---
language:
- yue
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
model-index:
- name: Whisper Large V2 - Cantonese - Augmented
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0
      type: mozilla-foundation/common_voice_11_0
      config: yue
      split: test
    metrics:
    - type: cer
      value: 6.213317142278891
      name: CER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Large V2 - Cantonese - Augmented

This model is a fine-tuned version of [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) on the mozilla-foundation/common_voice_11_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1828
- Cer: 6.2133

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

Training:
- [mozilla-foundation/common_voice_11_0](https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0) (train+validation)

Evaluation:
- [mozilla-foundation/common_voice_11_0](https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0) (test)

## Training procedure

Datasets were augmented on-the-fly using [audiomentations](https://github.com/iver56/audiomentations) via PitchShift and TimeStretch transformations at `p=0.3`.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 8
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- training_steps: 1000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.1126        | 1.21  | 200  | 0.1666          | 7.3103 |
| 0.0467        | 2.42  | 400  | 0.1610          | 6.9419 |
| 0.0217        | 3.63  | 600  | 0.1621          | 6.3874 |
| 0.008         | 4.85  | 800  | 0.1699          | 6.3064 |
| 0.0023        | 6.06  | 1000 | 0.1828          | 6.2133 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.8.1.dev0
- Tokenizers 0.13.2
