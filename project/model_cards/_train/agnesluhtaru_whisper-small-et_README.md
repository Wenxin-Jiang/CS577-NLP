---
license: apache-2.0
tags:
- generated_from_trainer
- whisper-event
metrics:
- wer
model-index:
- name: whisper-small-et
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_11_0
      type: mozilla-foundation/common_voice_11_0
      config: et
      split: test
    metrics:
    - type: wer
      value: 43.69
      name: WER
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-small-et

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the following datasets: Common Voice 11, VoxPopuli and FLEURS.

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

Estonian data from Common Voice 11, VoxPopuli and FLEURS corpora as both training and validation sets. Tested on Common Voice 11 test set. 

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
- training_steps: 2000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 1.1285        | 1.03  | 200  | 1.0640          | 53.4934 |
| 0.5163        | 2.05  | 400  | 0.6450          | 41.2428 |
| 0.2005        | 4.01  | 600  | 0.5600          | 36.6797 |
| 0.1188        | 5.03  | 800  | 0.5718          | 35.2847 |
| 0.0487        | 6.06  | 1000 | 0.5999          | 34.7500 |
| 0.0216        | 8.01  | 1200 | 0.6479          | 38.1906 |
| 0.016         | 9.04  | 1400 | 0.6655          | 39.5034 |
| 0.0085        | 10.06 | 1600 | 0.7027          | 33.9038 |
| 0.0079        | 12.02 | 1800 | 0.7207          | 39.5723 |
| 0.009         | 13.04 | 2000 | 0.7261          | 34.5973 |

### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.12.1+rocm5.1.1
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
