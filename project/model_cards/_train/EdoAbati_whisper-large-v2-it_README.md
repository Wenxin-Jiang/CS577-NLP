---
language:
- it
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Large v2 Italian
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 it
      type: mozilla-foundation/common_voice_11_0
      config: it
      split: test
      args: it
    metrics:
    - name: Wer
      type: wer
      value: 4.557596215181799
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Large v2 Italian

This model is a fine-tuned version of [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) on the mozilla-foundation/common_voice_11_0 it dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1332
- Wer: 4.5576

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
- distributed_type: multi-GPU
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 6000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.1684        | 0.17  | 1000 | 0.1620          | 6.4620 |
| 0.1174        | 0.33  | 2000 | 0.1418          | 5.5663 |
| 0.069         | 1.1   | 3000 | 0.1400          | 5.2865 |
| 0.0649        | 1.27  | 4000 | 0.1315          | 4.8932 |
| 0.0334        | 2.04  | 5000 | 0.1368          | 4.6845 |
| 0.037         | 2.21  | 6000 | 0.1332          | 4.5576 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.8.1.dev0
- Tokenizers 0.13.2
