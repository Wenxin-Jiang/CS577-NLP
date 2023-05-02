---
language:
- nl
license: apache-2.0
tags:
- automatic-speech-recognition
- common_voice
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-common_voice-nl-demo
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-common_voice-nl-demo

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the COMMON_VOICE - NL dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3523
- Wer: 0.2046

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 15.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.0536        | 1.12  | 500  | 0.5349          | 0.4338 |
| 0.2543        | 2.24  | 1000 | 0.3859          | 0.3029 |
| 0.1472        | 3.36  | 1500 | 0.3471          | 0.2818 |
| 0.1088        | 4.47  | 2000 | 0.3489          | 0.2731 |
| 0.0855        | 5.59  | 2500 | 0.3582          | 0.2558 |
| 0.0721        | 6.71  | 3000 | 0.3457          | 0.2471 |
| 0.0653        | 7.83  | 3500 | 0.3299          | 0.2357 |
| 0.0527        | 8.95  | 4000 | 0.3440          | 0.2334 |
| 0.0444        | 10.07 | 4500 | 0.3417          | 0.2289 |
| 0.0404        | 11.19 | 5000 | 0.3691          | 0.2204 |
| 0.0345        | 12.3  | 5500 | 0.3453          | 0.2102 |
| 0.0288        | 13.42 | 6000 | 0.3634          | 0.2089 |
| 0.027         | 14.54 | 6500 | 0.3532          | 0.2044 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3
- Tokenizers 0.11.0
