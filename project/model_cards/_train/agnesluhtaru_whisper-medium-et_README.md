---
license: apache-2.0
tags:
- generated_from_trainer
- whisper-event
metrics:
- wer
model-index:
- name: agnesluhtaru/whisper-medium-et
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0
      type: mozilla-foundation/common_voice_11_0
      config: et
      split: test
    metrics:
    - type: wer
      value: 28.6
      name: WER
---

# whisper-medium-et

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the following datasets: Common Voice 11, VoxPopuli and FLEURS.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

Estonian data from Common Voice 11, VoxPopuli and FLEURS corpora as both training and validation sets. Tested on Common Voice 11 test set. 

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

### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.12.1+rocm5.1.1
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2