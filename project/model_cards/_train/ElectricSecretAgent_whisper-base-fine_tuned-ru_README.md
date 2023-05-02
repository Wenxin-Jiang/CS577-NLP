---
language:
- ru
license: apache-2.0
tags:
- hf-asr-leaderboard
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: whisper-base-fine_tuned-ru
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: common_voice_11_0
      type: mozilla-foundation/common_voice_11_0
      args: 'config: ru, split: test'
    metrics:
    - name: Wer
      type: wer
      value: 41.216909250757055
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-base-fine_tuned-ru

This model is a fine-tuned version of [openai/whisper-base](https://huggingface.co/openai/whisper-base) on the [common_voice_11_0](https://huggingface.co/datasets/mozilla-foundation/common_voice_11_0) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4553
- Wer: 41.2169

## Model description

Same as original model (see [whisper-base](https://huggingface.co/openai/whisper-base)). ***But! This model has been fine-tuned for the task of transcribing the Russian language.***

## Intended uses & limitations

Same as original model (see [whisper-base](https://huggingface.co/openai/whisper-base)).

## Training and evaluation data

More information needed

## Training procedure

The model is fine-tuned using the following notebook (available only in the Russian version): https://github.com/blademoon/Whisper_Train

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 250
- training_steps: 20000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer     |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|
| 0.702         | 0.25  | 500   | 0.8245          | 71.6653 |
| 0.5699        | 0.49  | 1000  | 0.6640          | 55.7048 |
| 0.5261        | 0.74  | 1500  | 0.6127          | 50.6215 |
| 0.4997        | 0.98  | 2000  | 0.5834          | 47.4541 |
| 0.4681        | 1.23  | 2500  | 0.5638          | 46.6262 |
| 0.4651        | 1.48  | 3000  | 0.5497          | 47.5090 |
| 0.4637        | 1.72  | 3500  | 0.5379          | 46.5700 |
| 0.4185        | 1.97  | 4000  | 0.5274          | 45.3160 |
| 0.3856        | 2.22  | 4500  | 0.5205          | 45.5871 |
| 0.4078        | 2.46  | 5000  | 0.5122          | 45.7190 |
| 0.4132        | 2.71  | 5500  | 0.5066          | 45.5004 |
| 0.3914        | 2.96  | 6000  | 0.4998          | 47.0011 |
| 0.3822        | 3.2   | 6500  | 0.4959          | 44.9570 |
| 0.3596        | 3.45  | 7000  | 0.4916          | 45.5578 |
| 0.3877        | 3.69  | 7500  | 0.4870          | 45.2476 |
| 0.3687        | 3.94  | 8000  | 0.4832          | 45.2159 |
| 0.3514        | 4.19  | 8500  | 0.4809          | 46.0254 |
| 0.3202        | 4.43  | 9000  | 0.4779          | 48.1306 |
| 0.3229        | 4.68  | 9500  | 0.4751          | 45.5724 |
| 0.3285        | 4.93  | 10000 | 0.4717          | 45.9436 |
| 0.3286        | 5.17  | 10500 | 0.4705          | 45.0510 |
| 0.3294        | 5.42  | 11000 | 0.4689          | 47.2111 |
| 0.3384        | 5.66  | 11500 | 0.4666          | 47.3393 |
| 0.316         | 5.91  | 12000 | 0.4650          | 43.2536 |
| 0.2988        | 6.16  | 12500 | 0.4638          | 42.9789 |
| 0.3046        | 6.4   | 13000 | 0.4629          | 42.4331 |
| 0.2962        | 6.65  | 13500 | 0.4614          | 40.2437 |
| 0.3008        | 6.9   | 14000 | 0.4602          | 39.5734 |
| 0.2749        | 7.14  | 14500 | 0.4593          | 40.1497 |
| 0.3001        | 7.39  | 15000 | 0.4588          | 42.6248 |
| 0.3054        | 7.64  | 15500 | 0.4580          | 40.3707 |
| 0.2926        | 7.88  | 16000 | 0.4574          | 39.4232 |
| 0.2938        | 8.13  | 16500 | 0.4569          | 40.9532 |
| 0.3105        | 8.37  | 17000 | 0.4566          | 40.4379 |
| 0.2799        | 8.62  | 17500 | 0.4562          | 40.3622 |
| 0.2793        | 8.87  | 18000 | 0.4557          | 41.3451 |
| 0.2819        | 9.11  | 18500 | 0.4555          | 41.4184 |
| 0.2907        | 9.36  | 19000 | 0.4555          | 39.9348 |
| 0.3113        | 9.61  | 19500 | 0.4553          | 41.0289 |
| 0.2867        | 9.85  | 20000 | 0.4553          | 41.2169 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.1
- Datasets 2.7.1
- Tokenizers 0.13.1
