---
license: apache-2.0
language:
- hi
tags:
- automatic-speech-recognition
- Harveenchadha/indic-voice
- generated_from_trainer
model-index:
- name: Wav2Vec2_xls_r_openslr_Hi_V2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Wav2Vec2_xls_r_openslr_Hi_V2

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the [Harveenchadha/indic-voice](https://huggingface.co/datasets/Harveenchadha/indic-voice) dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3184
- Wer: 0.3104
- Cer: 0.0958

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 200
- num_epochs: 12
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Cer    | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:------:|:---------------:|:------:|
| 7.1097        | 0.48  | 300  | 0.9965 | 3.3989          | 1.0    |
| 3.0235        | 0.96  | 600  | 0.3163 | 1.3183          | 0.7977 |
| 1.1419        | 1.44  | 900  | 0.1913 | 0.6416          | 0.5543 |
| 0.8242        | 1.92  | 1200 | 0.1608 | 0.5063          | 0.4804 |
| 0.6876        | 2.56  | 1600 | 0.1387 | 0.4401          | 0.4280 |
| 0.5868        | 3.21  | 2000 | 0.1249 | 0.3940          | 0.3907 |
| 0.5285        | 3.85  | 2400 | 0.1200 | 0.3661          | 0.3763 |
| 0.5           | 4.49  | 2800 | 0.3528 | 0.3610          | 0.1136 |
| 0.4538        | 5.13  | 3200 | 0.3403 | 0.3485          | 0.1086 |
| 0.4165        | 5.77  | 3600 | 0.3335 | 0.3439          | 0.1062 |
| 0.3989        | 6.41  | 4000 | 0.3264 | 0.3340          | 0.1036 |
| 0.3679        | 7.05  | 4400 | 0.3256 | 0.3287          | 0.1013 |
| 0.3517        | 7.69  | 4800 | 0.3212 | 0.3223          | 0.1002 |
| 0.3357        | 8.33  | 5200 | 0.3173 | 0.3196          | 0.0986 |
| 0.3225        | 8.97  | 5600 | 0.3142 | 0.3177          | 0.0985 |
| 0.3057        | 9.62  | 6000 | 0.3199 | 0.3156          | 0.0975 |
| 0.2972        | 10.26 | 6400 | 0.3139 | 0.3128          | 0.0967 |
| 0.2881        | 10.9  | 6800 | 0.3184 | 0.3107          | 0.0957 |
| 0.2791        | 11.54 | 7200 | 0.3184 | 0.3104          | 0.0958 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0
