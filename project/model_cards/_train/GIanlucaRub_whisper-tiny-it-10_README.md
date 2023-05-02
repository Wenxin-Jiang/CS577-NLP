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
- name: Whisper Tiny it 10
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0
      type: mozilla-foundation/common_voice_11_0
      config: it
      split: test[:10%]
      args: 'config: it, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 46.817804
---
# Whisper Tiny it 9
This model is a fine-tuned version of [openai/whisper-tiny](https://huggingface.co/openai/whisper-tiny) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.732505
- Wer: 45.327232
## Model description

This model is the openai whisper small transformer adapted for Italian audio to text transcription.

## Intended uses & limitations

The model is available through its [HuggingFace web app](https://huggingface.co/spaces/GIanlucaRub/whisper-it)

## Training and evaluation data

Data used for training is the initial 10% of train and validation of [Italian Common Voice](https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0/viewer/it/train) 11.0 from Mozilla Foundation.
The dataset used for evaluation is the initial 10% of test of Italian Common Voice.
The training data has been augmented with random noise, random pitching and change of the speed of the voice.

## Training procedure

After loading the pre trained model, it has been trained on the augmented dataset.

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
| 1.5103        | 0.95  | 1000 | 0.8238          | 52.6830 |
| 1.2030        | 1.91  | 2000 | 0.7581          | 49.4038 |
| 1.0094        | 2.86  | 3000 | 0.7364          | 47.7884 |
| 0.8973        | 3.82  | 4000 | 0.7325          | 46.8178
### Framework versions
- Transformers 4.26.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2