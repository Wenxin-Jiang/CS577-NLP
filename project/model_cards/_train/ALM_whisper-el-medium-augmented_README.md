---
language:
- el
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Medium Greek - Robust
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0 el
      type: mozilla-foundation/common_voice_11_0
      config: el
      split: test
      args: el
    metrics:
    - type: wer
      value: 17.709881129271917
      name: Wer
    - type: wer
      value: 13.25
      name: WER
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: google/fleurs
      type: google/fleurs
      config: el_gr
      split: test
    metrics:
    - type: wer
      value: 39.59
      name: WER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Medium Greek - Robust

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the mozilla-foundation/common_voice_11_0 el dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2807
- Wer: 17.7099

**IMPORTANT** The model has been trained using *data augmentation* to improve its generalization capabilities and robustness. 
The results on the eval set during training are biased towards data augmentation applied to evaluation data.

**Results on eval set**

- Mozilla CV 11.0 - Greek: 13.250 WER (using official script)
- Google Fluers - Greek: 39.59 WER (using official script)
 
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
- train_batch_size: 8
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 20000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer     |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|
| 0.0407        | 4.69  | 2000  | 0.2484          | 20.8767 |
| 0.0128        | 9.39  | 4000  | 0.2795          | 21.2017 |
| 0.0041        | 14.08 | 6000  | 0.2744          | 19.1308 |
| 0.0017        | 18.78 | 8000  | 0.2759          | 17.9978 |
| 0.0005        | 23.47 | 10000 | 0.2751          | 18.5457 |
| 0.0015        | 28.17 | 12000 | 0.2928          | 19.2051 |
| 0.0004        | 32.86 | 14000 | 0.2819          | 18.2857 |
| 0.0002        | 37.56 | 16000 | 0.2831          | 17.7285 |
| 0.0007        | 42.25 | 18000 | 0.2776          | 17.8399 |
| 0.0           | 46.95 | 20000 | 0.2792          | 17.0970 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.11.0+cu113
- Datasets 2.7.1
- Tokenizers 0.12.1
