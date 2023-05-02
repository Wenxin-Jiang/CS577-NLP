---
language:
- br
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Medium Breton
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 br
      type: mozilla-foundation/common_voice_11_0
      config: br
      split: test
      args: br
    metrics:
    - name: Wer
      type: wer
      value: 41.611670718999655
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium Breton

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the mozilla-foundation/common_voice_11_0 br dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8486
- Wer: 41.6117

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-06
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- distributed_type: multi-GPU
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 400
- training_steps: 5000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.0602        | 5.03  | 1000 | 0.7324          | 43.6957 |
| 0.0036        | 10.05 | 2000 | 0.8486          | 41.6117 |
| 0.001         | 15.08 | 3000 | 0.9033          | 42.0458 |
| 0.0004        | 20.1  | 4000 | 0.9351          | 41.6811 |
| 0.0003        | 25.13 | 5000 | 0.9468          | 41.7853 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.1+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
