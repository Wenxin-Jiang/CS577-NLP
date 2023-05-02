---
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
model-index:
- name: Whisper Medium TW - Augmented
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0
      type: mozilla-foundation/common_voice_11_0
      config: zh-TW
      split: test
    metrics:
    - type: wer
      value: 7.4864742410916545
      name: WER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium TW - Augmented

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the mozilla-foundation/common_voice_11_0 dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.0951
- eval_wer: 7.4865
- eval_runtime: 2823.6824
- eval_samples_per_second: 1.668
- eval_steps_per_second: 0.834
- epoch: 1.7
- step: 600

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

- Datasets were augmented on-the-fly using [audiomentations](https://github.com/iver56/audiomentations) via PitchShift and TimeStretch transformations at `p=0.3`.
- A space is added between each Chinese character, as demonstrated in the original paper. Effectively, WER == CER in this case.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- training_steps: 1000
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
