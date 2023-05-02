---
language:
- tr
license: apache-2.0
tags:
- automatic-speech-recognition
- common_voice
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-common_voice-tr-demo
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-common_voice-tr-demo

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the COMMON_VOICE - TR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3798
- Wer: 0.3448

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 15.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| No log        | 0.92  | 100  | 3.5932          | 1.0    |
| No log        | 1.83  | 200  | 3.0185          | 0.9999 |
| No log        | 2.75  | 300  | 0.9357          | 0.8007 |
| No log        | 3.67  | 400  | 0.5945          | 0.6318 |
| 3.1829        | 4.59  | 500  | 0.4931          | 0.5265 |
| 3.1829        | 5.5   | 600  | 0.4757          | 0.4784 |
| 3.1829        | 6.42  | 700  | 0.4282          | 0.4540 |
| 3.1829        | 7.34  | 800  | 0.3995          | 0.4252 |
| 3.1829        | 8.26  | 900  | 0.4046          | 0.4149 |
| 0.2215        | 9.17  | 1000 | 0.4048          | 0.3951 |
| 0.2215        | 10.09 | 1100 | 0.3944          | 0.3865 |
| 0.2215        | 11.01 | 1200 | 0.3853          | 0.3643 |
| 0.2215        | 11.93 | 1300 | 0.3950          | 0.3632 |
| 0.2215        | 12.84 | 1400 | 0.3836          | 0.3506 |
| 0.1009        | 13.76 | 1500 | 0.3808          | 0.3510 |
| 0.1009        | 14.68 | 1600 | 0.3807          | 0.3456 |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.12.1+cu102
- Datasets 2.4.0
- Tokenizers 0.12.1
