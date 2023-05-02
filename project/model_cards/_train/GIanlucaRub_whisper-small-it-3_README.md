---
language:
- it
license: apache-2.0
tags:
- hf-asr-leaderboard
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small It - Gianluca Ruberto
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0
      type: mozilla-foundation/common_voice_11_0
      config: it
      split: test[:10%]
      args: 'config: hi, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 22.108985024958404
---


# Whisper Small It - Gianluca Ruberto

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.393979	
- Wer: 22.108985

## Model description

This model is the openai whisper small transformer adapted for Italian audio to text transcription.

## Intended uses & limitations

The model is available through its [HuggingFace web app](https://huggingface.co/spaces/GIanlucaRub/whisper-it)

## Training and evaluation data

Data used for training is the initial 10% of train and validation of [Italian Common Voice](https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0/viewer/it/train) 11.0 from Mozilla Foundation.
The dataset used for evaluation is the initial 10% of test of Italian Common Voice.

## Training procedure

After loading the pre trained model, it has been trained on the dataset.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 4000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.2545        | 0.95  | 1000 | 0.3872          | 24.8891 |
| 0.129         | 1.91  | 2000 | 0.3682          | 22.1991 |
| 0.0534        | 2.86  | 3000 | 0.3771          | 22.4695 |
| 0.0302        | 3.82  | 4000 | 0.3940          | 22.1090 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
