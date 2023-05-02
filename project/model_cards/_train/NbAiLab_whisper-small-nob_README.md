---
language:
- no
license: apache-2.0
tags:
- whisper-event
- norwegian
datasets:
- NbAiLab/NCC_S
- NbAiLab/NPSC
- NbAiLab/NST
metrics:
- wer
model-index:
- name: Whisper Small Norwegian Bokmål
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: FLEURS
      type: google/fleurs
      config: nb_no
      split: validation
      args: nb_no
    metrics:
    - name: Wer
      type: wer
      value: 15.56
---

# Whisper Small Norwegian Bokmål

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) trained on several datasets.

It is currently in the middle of a large training. Currently it achieves the following results on the evaluation set:
- Loss: 0.3230
- Wer: 15.56

## Model description

The model is trained on a large corpus of roughly 5.000 hours of voice. The sources are subtitles from the Norwegian broadcaster NRK, transcribed speeches from the Norwegian parliament and voice recordings from Norsk Språkteknologi. 

## Intended uses & limitations

The model will be free for everyone to use when it is finished.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-06
- train_batch_size: 128
- gradient_accumulation_steps: 2
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: constant with warmup
- lr_scheduler_warmup_steps: 1000
- training_steps: 50.000 (currently @1.000)
- mixed_precision_training: fp16
- deepspeed: true

### Live Training results
See [Tensorboad Metrics](https://huggingface.co/NbAiLab/whisper-small-nob/tensorboard)




