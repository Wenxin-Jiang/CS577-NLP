---
language:
- ar
- multilingual

license: apache-2.0
tags:
- automatic-speech-recognition
- hf-asr-leaderboard
- whisper-event
- generated_from_trainer
- Arabic
- multilingual
- STT
datasets:
- mozilla-foundation/common_voice_12_0
metrics:
- wer
model-index:

- name: Kalemat-Tech Arabic Speech Recognition Model (STT)
  results:
  - task:
      type: automatic-speech-recognition
      name: Speech Recognition
    dataset:
      type: mozilla-foundation/common_voice_12_0
      name: mozilla-foundation/common_voice_12_0
      config: ar
      split: test
      args: ar
    metrics:
    - type: wer
      value: 58.5848
      name: wer
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->
# Kalemat-Tech Arabic Speech Recognition Model (STT) - Mohamed Salama
# نموذج كلماتك للتعرف على الأصوات العربية الفصحى و تحويلها إلى نصوص

# KalemaTech-Arabic-STT-ASR-based-on-Whisper-Small

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on Common_Voice_Arabic_12.0_Augmented.
It achieves the following results on the evaluation set:
- Loss: 0.5362
- Wer: 58.5848

## Example of usage:
```
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq

processor = AutoProcessor.from_pretrained("Salama1429/KalemaTech-Arabic-STT-ASR-based-on-Whisper-Small")

model = AutoModelForSpeechSeq2Seq.from_pretrained("Salama1429/KalemaTech-Arabic-STT-ASR-based-on-Whisper-Small")
```
## Intended uses & limitations

Automatic Speech Recognition

## Training and evaluation data
```
Common_Voice_Arabic_12.0 and I made some augmentations to it as follows:
- 25% of the data TimeMasking
- 25% of the data SpecAugmentation
- 25% of the data WavAugmentation (AddGaussianNoise)
- The final dataset is the original common voice plus the augmented files
```
## Training procedure

### Training hyperparameters
```
The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 64
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 25
- mixed_precision_training: Native AMP
```
### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer     |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|
| 0.2728        | 1.01  | 1000  | 0.3063          | 60.4733 |
| 0.1442        | 2.01  | 2000  | 0.2878          | 55.6935 |
| 0.0648        | 3.02  | 3000  | 0.3009          | 59.2568 |
| 0.0318        | 4.03  | 4000  | 0.3278          | 59.2993 |
| 0.0148        | 5.04  | 5000  | 0.3539          | 61.0364 |
| 0.0088        | 6.04  | 6000  | 0.3714          | 56.9154 |
| 0.0061        | 7.05  | 7000  | 0.3920          | 57.5515 |
| 0.0041        | 8.06  | 8000  | 0.4149          | 61.6328 |
| 0.0033        | 9.06  | 9000  | 0.4217          | 58.0310 |
| 0.0033        | 10.07 | 10000 | 0.4376          | 59.9594 |
| 0.0021        | 11.08 | 11000 | 0.4485          | 56.7812 |
| 0.0015        | 12.08 | 12000 | 0.4577          | 57.6936 |
| 0.0013        | 13.09 | 13000 | 0.4671          | 60.6606 |
| 0.0011        | 14.1  | 14000 | 0.4686          | 59.8159 |
| 0.0008        | 15.11 | 15000 | 0.4856          | 60.7111 |
| 0.0011        | 16.11 | 16000 | 0.4851          | 59.5198 |
| 0.0005        | 17.12 | 17000 | 0.4936          | 59.2608 |
| 0.0004        | 18.13 | 18000 | 0.4995          | 57.9619 |
| 0.0003        | 19.13 | 19000 | 0.5085          | 58.3630 |
| 0.0002        | 20.14 | 20000 | 0.5155          | 58.0987 |
| 0.0001        | 21.15 | 21000 | 0.5251          | 58.8504 |
| 0.0001        | 22.16 | 22000 | 0.5268          | 58.4228 |
| 0.0001        | 23.16 | 23000 | 0.5317          | 59.0881 |
| 0.0001        | 24.17 | 24000 | 0.5362          | 58.5848 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu117
- Datasets 2.8.0
- Tokenizers 0.13.2
