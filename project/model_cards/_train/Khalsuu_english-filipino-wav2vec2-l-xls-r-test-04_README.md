---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- filipino_voice
model-index:
- name: english-filipino-wav2vec2-l-xls-r-test-04
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# english-filipino-wav2vec2-l-xls-r-test-04

This model is a fine-tuned version of [jonatasgrosman/wav2vec2-large-xlsr-53-english](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english) on the filipino_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0713
- Wer: 0.5078

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
- num_epochs: 40
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 2.2131        | 2.09  | 400  | 0.7100          | 0.6832 |
| 0.6539        | 4.19  | 800  | 0.8307          | 0.6602 |
| 0.5081        | 6.28  | 1200 | 0.7120          | 0.6297 |
| 0.42          | 8.38  | 1600 | 0.7309          | 0.6299 |
| 0.3482        | 10.47 | 2000 | 0.7665          | 0.6148 |
| 0.293         | 12.57 | 2400 | 0.7091          | 0.5840 |
| 0.265         | 14.66 | 2800 | 0.8170          | 0.6102 |
| 0.2294        | 16.75 | 3200 | 0.9715          | 0.6216 |
| 0.1872        | 18.85 | 3600 | 0.8516          | 0.5837 |
| 0.1644        | 20.94 | 4000 | 0.8408          | 0.5767 |
| 0.1495        | 23.04 | 4400 | 0.9188          | 0.5717 |
| 0.1276        | 25.13 | 4800 | 1.0149          | 0.5451 |
| 0.116         | 27.23 | 5200 | 1.0220          | 0.5683 |
| 0.1017        | 29.32 | 5600 | 0.9319          | 0.5253 |
| 0.0899        | 31.41 | 6000 | 0.9949          | 0.5435 |
| 0.0861        | 33.51 | 6400 | 1.1029          | 0.5467 |
| 0.0766        | 35.6  | 6800 | 1.0219          | 0.5193 |
| 0.065         | 37.7  | 7200 | 1.0836          | 0.5214 |
| 0.0588        | 39.79 | 7600 | 1.0713          | 0.5078 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3
