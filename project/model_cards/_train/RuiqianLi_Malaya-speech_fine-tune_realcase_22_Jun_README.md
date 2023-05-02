---
tags:
- generated_from_trainer
datasets:
- uob_singlish
model-index:
- name: Malaya-speech_fine-tune_realcase_22_Jun
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Malaya-speech_fine-tune_realcase_22_Jun

This model is a fine-tuned version of [malay-huggingface/wav2vec2-xls-r-300m-mixed](https://huggingface.co/malay-huggingface/wav2vec2-xls-r-300m-mixed) on the uob_singlish dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9569
- Wer: 0.4062

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 2
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.6913        | 20.0  | 100  | 0.9569          | 0.4062 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3
