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
- name: Whisper Medium Italian
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
      value: 5.48054433340421
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium Italian

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the mozilla-foundation/common_voice_11_0 it dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1456
- Wer: 5.4805

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
- distributed_type: multi-GPU
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.1951        | 0.2   | 1000 | 0.1851          | 7.6268 |
| 0.1311        | 0.4   | 2000 | 0.1565          | 6.2885 |
| 0.0681        | 1.12  | 3000 | 0.1555          | 6.0394 |
| 0.067         | 1.32  | 4000 | 0.1470          | 5.6148 |
| 0.0336        | 2.05  | 5000 | 0.1456          | 5.4805 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.8.1.dev0
- Tokenizers 0.13.2
