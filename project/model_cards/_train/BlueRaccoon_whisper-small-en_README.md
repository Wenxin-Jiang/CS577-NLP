---
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- google/fleurs
metrics:
- wer
model-index:
- name: Whisper Small English
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: google/fleurs en_us
      type: google/fleurs
      config: en_us
      split: test
      args: en_us
    metrics:
    - type: wer
      value: 7.990755655157924
      name: Wer
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0
      type: mozilla-foundation/common_voice_11_0
      config: en
      split: test
    metrics:
    - type: wer
      value: 18.21
      name: WER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small English

This model is a fine-tuned version of [openai/whisper-small.en](https://huggingface.co/openai/whisper-small.en) on the google/fleurs en_us dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6007
- Wer: 7.9908


## Model description

This model was created as part of the Whisper Fine-Tune Event. This is my first attempt at fine-tuning the Whisper neural network. 
Honestly, it's my second time ever trying anything related to training a neural network, and my first time was pretty bad (but I did
get a lot of rather funny images out of it, so perhaps it wasn't entirely fruitless?), and it seems like the WER only went up after step 2000,
so... I'm not sure if I did a good job or if I just wasted GPU cycles, but maybe I can try again and get a better score?

I'm learning.



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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 0.0005        | 24.0   | 1000 | 0.5092          | 7.5566 |
| 0.0002        | 48.01  | 2000 | 0.5528          | 7.7526 |
| 0.0001        | 73.0   | 3000 | 0.5785          | 7.8507 |
| 0.0001        | 97.0   | 4000 | 0.5936          | 7.9908 |
| 0.0001        | 121.01 | 5000 | 0.6007          | 7.9908 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
