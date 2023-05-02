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
- name: Whisper Large Norwegian Bokmål
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
      value: 10.718635559082031
---

# Whisper Large Norwegian Bokmål

This model is a fine-tuned version of [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) trained on several datasets.

It is currently in the middle of a large training. Currently it achieves the following results on the evaluation set:
- Loss: 0.2477
- Wer: 10.718635559082031

## Model description

The model is trained on a large corpus of roughly 5.000 hours of voice. The sources are subtitles from the Norwegian broadcaster NRK, transcribed speeches from the Norwegian parliament and voice recordings from Norsk Språkteknologi. 

## Intended uses & limitations

The model will be free for everyone to use when it is finished.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-06
- train_batch_size: 64
- gradient_accumulation_steps: 2
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: constant with warmpu
- lr_scheduler_warmup_steps: 1000
- training_steps: 50.000 (currently @1.000)
- mixed_precision_training: fp16
- deepspeed: true

### Live Training results
See [Tensorboad Metrics](https://huggingface.co/NbAiLab/whisper-large-v2-nob/tensorboard)




