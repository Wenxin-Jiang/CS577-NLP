---
tags:
- generated_from_trainer
model-index:
- name: finetune_indian_asr
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetune_indian_asr

This model is a fine-tuned version of [Harveenchadha/vakyansh-wav2vec2-indian-english-enm-700](https://huggingface.co/Harveenchadha/vakyansh-wav2vec2-indian-english-enm-700) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4215
- Wer: 0.3403

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 5.0566        | 3.45  | 500  | 2.9944          | 1.0    |
| 2.7241        | 6.9   | 1000 | 1.4455          | 0.7654 |
| 0.9755        | 10.34 | 1500 | 0.4299          | 0.4034 |
| 0.4624        | 13.79 | 2000 | 0.3628          | 0.3297 |
| 0.3158        | 17.24 | 2500 | 0.3835          | 0.2952 |
| 0.2604        | 20.69 | 3000 | 0.3802          | 0.2877 |
| 0.2           | 24.14 | 3500 | 0.3842          | 0.2799 |
| 1.7441        | 27.59 | 4000 | 0.4215          | 0.3403 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
