---
language:
- pl
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Small PL
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0
      type: mozilla-foundation/common_voice_11_0
      config: pl
      split: test
      args: pl
    metrics:
    - name: Wer
      type: wer
      value: 14.49425614099627
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small PL

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4444
- Wer: 14.4943

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
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.1639        | 0.1   | 500  | 0.3290          | 16.6413 |
| 0.0674        | 1.1   | 1000 | 0.3224          | 15.1782 |
| 0.0335        | 2.09  | 1500 | 0.3186          | 14.5394 |
| 0.0161        | 3.09  | 2000 | 0.3445          | 15.0026 |
| 0.0101        | 4.08  | 2500 | 0.3777          | 14.5260 |
| 0.0064        | 5.08  | 3000 | 0.3977          | 14.6264 |
| 0.0036        | 6.08  | 3500 | 0.4621          | 14.6180 |
| 0.0025        | 7.07  | 4000 | 0.4639          | 14.5193 |
| 0.0017        | 8.07  | 4500 | 0.4971          | 14.4725 |
| 0.0017        | 9.07  | 5000 | 0.4444          | 14.4943 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu117
- Datasets 2.7.1
- Tokenizers 0.13.2
