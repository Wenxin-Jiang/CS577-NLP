---
tags:
- generated_from_trainer
datasets:
- uob_singlish
model-index:
- name: Malaya-speech_fine-tune_realcase_27_Jun
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Malaya-speech_fine-tune_realcase_27_Jun

This model is a fine-tuned version of [malay-huggingface/wav2vec2-xls-r-300m-mixed](https://huggingface.co/malay-huggingface/wav2vec2-xls-r-300m-mixed) on the uob_singlish dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9159
- Wer: 0.3819

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 1.3176        | 1.82  | 20   | 0.8928          | 0.3542 |
| 0.6716        | 3.64  | 40   | 0.9123          | 0.3681 |
| 0.3484        | 5.45  | 60   | 0.9509          | 0.3681 |
| 0.3064        | 7.27  | 80   | 0.9227          | 0.3958 |
| 0.3017        | 9.09  | 100  | 0.9159          | 0.3819 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3
