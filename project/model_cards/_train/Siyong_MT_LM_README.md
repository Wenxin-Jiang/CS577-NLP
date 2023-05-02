---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec-base-Millad_TIMIT
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec-base-Millad_TIMIT

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3772
- Wer: 0.6859
- Cer: 0.3217

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 5000
- num_epochs: 60
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|
| No log        | 2.36  | 2000  | 2.6233          | 1.0130 | 0.6241 |
| No log        | 4.73  | 4000  | 2.2206          | 0.9535 | 0.5032 |
| No log        | 7.09  | 6000  | 2.3036          | 0.9368 | 0.5063 |
| 1.235         | 9.46  | 8000  | 1.9932          | 0.9275 | 0.5032 |
| 1.235         | 11.82 | 10000 | 2.0207          | 0.8922 | 0.4498 |
| 1.235         | 14.18 | 12000 | 1.6171          | 0.7993 | 0.3976 |
| 1.235         | 16.55 | 14000 | 1.6729          | 0.8309 | 0.4209 |
| 0.2779        | 18.91 | 16000 | 1.7043          | 0.8141 | 0.4340 |
| 0.2779        | 21.28 | 18000 | 1.7426          | 0.7658 | 0.3960 |
| 0.2779        | 23.64 | 20000 | 1.5230          | 0.7361 | 0.3830 |
| 0.2779        | 26.0  | 22000 | 1.4286          | 0.7658 | 0.3794 |
| 0.1929        | 28.37 | 24000 | 1.4450          | 0.7379 | 0.3644 |
| 0.1929        | 30.73 | 26000 | 1.5922          | 0.7491 | 0.3826 |
| 0.1929        | 33.1  | 28000 | 1.4443          | 0.7454 | 0.3617 |
| 0.1929        | 35.46 | 30000 | 1.5450          | 0.7268 | 0.3621 |
| 0.1394        | 37.83 | 32000 | 1.9268          | 0.7491 | 0.3763 |
| 0.1394        | 40.19 | 34000 | 1.7094          | 0.7342 | 0.3783 |
| 0.1394        | 42.55 | 36000 | 1.4024          | 0.7082 | 0.3494 |
| 0.1394        | 44.92 | 38000 | 1.4467          | 0.6840 | 0.3395 |
| 0.104         | 47.28 | 40000 | 1.4145          | 0.6933 | 0.3407 |
| 0.104         | 49.65 | 42000 | 1.3901          | 0.6970 | 0.3403 |
| 0.104         | 52.01 | 44000 | 1.3589          | 0.6636 | 0.3348 |
| 0.104         | 54.37 | 46000 | 1.3716          | 0.6952 | 0.3340 |
| 0.0781        | 56.74 | 48000 | 1.4025          | 0.6896 | 0.3312 |
| 0.0781        | 59.1  | 50000 | 1.3772          | 0.6859 | 0.3217 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.0+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1
