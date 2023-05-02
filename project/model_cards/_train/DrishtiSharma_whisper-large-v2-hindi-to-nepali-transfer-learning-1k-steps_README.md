---
language:
- ne
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Large-V2 Nepali
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 ne-NP
      type: mozilla-foundation/common_voice_11_0
      config: ne-NP
      split: test
      args: ne-NP
    metrics:
    - name: Wer
      type: wer
      value: 9.75609756097561
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Large-V2 Nepali

This model is a fine-tuned version of [DrishtiSharma/whisper-large-v2-hindi-3k-steps](https://huggingface.co/DrishtiSharma/whisper-large-v2-hindi-3k-steps) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9961
- Wer: 9.7561

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- training_steps: 1000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 0.0           | 1000.0 | 1000 | 0.9961          | 9.7561 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu116
- Datasets 2.8.1.dev0
- Tokenizers 0.13.2