---
language: et
datasets:
- mozilla-foundation/common_voice_8_0
metrics:
- wer
- cer
tags:
- generated_from_trainer
- mozilla-foundation/common_voice_8_0
- audio
- automatic-speech-recognition
- speech
- robust-speech-event
- hf-asr-leaderboard
model-index:
- name: XLS-R 1B Wav2Vec2 Estonian by Rasmus Toivanen
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: et
    metrics:
    - name: Test WER
      type: wer
      value: 20.12
    - name: Test CER
      type: cer
      value: 3.82
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: et
    metrics:
    - name: Test WER
      type: wer
      value: 40.77
    - name: Test CER
      type: cer
      value: 12.32
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: et
    metrics:
    - name: Test WER
      type: wer
      value: 41.97
---
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->
# wav2vec2-xlsr-et-lm-1B

This model was finetuned with mozilla_foundation/common_voice_8_0 et with train+other+validation splits.
It achieves the following results on the test set:
(Loss reported with last eval step at step 2000/2040 during training)
- Loss: 0.2150 
- Wer: 0.2012

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.00005
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 1
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results




### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0
