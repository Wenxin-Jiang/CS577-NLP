---
language:
- tr
license: apache-2.0
tags:
- whisper
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small Turkish
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 tr
      type: mozilla-foundation/common_voice_11_0
      config: tr
      split: test
      args: tr
    metrics:
    - name: Wer
      type: wer
      value: 17.275280898876407
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Turkish

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the mozilla-foundation/common_voice_11_0 tr dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2799
- Wer: 17.2753
- Cer: 4.5335

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
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|
| 0.1044        | 1.07  | 1000 | 0.2777          | 18.4046 | 4.8810 |
| 0.0469        | 3.02  | 2000 | 0.2799          | 17.2753 | 4.5335 |
| 0.014         | 4.09  | 3000 | 0.3202          | 18.0800 | 4.9039 |
| 0.0039        | 6.04  | 4000 | 0.3326          | 18.2964 | 5.0192 |
| 0.0022        | 7.11  | 5000 | 0.3453          | 18.0307 | 4.9470 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.8.1.dev0
- Tokenizers 0.13.2
