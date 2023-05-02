---
language:
- cy
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small Welsh - Robust
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 cy
      type: mozilla-foundation/common_voice_11_0
      config: cy
      split: test
      args: cy
    metrics:
    - type: wer
      value: 23.073562122656497
      name: Wer
    - type: wer
      value: 20.33
      name: WER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small Welsh - Robust

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the mozilla-foundation/common_voice_11_0 cy dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4569
- Wer: 23.0736

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
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
| 0.0597        | 6.1   | 1000 | 0.4690          | 29.4666 |
| 0.0107        | 12.2  | 2000 | 0.4707          | 26.2671 |
| 0.0026        | 18.29 | 3000 | 0.4643          | 24.6763 |
| 0.0007        | 24.39 | 4000 | 0.4629          | 23.8024 |
| 0.0004        | 30.49 | 5000 | 0.4610          | 23.0616 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.8.0
- Tokenizers 0.13.2
