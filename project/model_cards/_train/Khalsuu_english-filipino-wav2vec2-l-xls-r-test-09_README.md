---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- filipino_voice
model-index:
- name: english-filipino-wav2vec2-l-xls-r-test-09
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# english-filipino-wav2vec2-l-xls-r-test-09

This model is a fine-tuned version of [jonatasgrosman/wav2vec2-large-xlsr-53-english](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english) on the filipino_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0054
- Wer: 0.5750

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.002
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.001         | 2.09  | 400  | 1.3499          | 0.9595 |
| 0.8606        | 4.19  | 800  | 0.8159          | 0.6942 |
| 0.5819        | 6.28  | 1200 | 0.7372          | 0.6700 |
| 0.4751        | 8.38  | 1600 | 0.7310          | 0.6405 |
| 0.3777        | 10.47 | 2000 | 0.7841          | 0.6414 |
| 0.2918        | 12.57 | 2400 | 0.7898          | 0.5951 |
| 0.2209        | 14.66 | 2800 | 0.8558          | 0.5751 |
| 0.1671        | 16.75 | 3200 | 0.9881          | 0.5979 |
| 0.129         | 18.85 | 3600 | 1.0054          | 0.5750 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3
