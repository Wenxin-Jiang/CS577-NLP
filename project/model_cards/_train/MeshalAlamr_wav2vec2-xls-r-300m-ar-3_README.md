---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-xls-r-300m-ar-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-300m-ar-3

This model is a fine-tuned version of [MeshalAlamr/wav2vec2-xls-r-300m-ar-2](https://huggingface.co/MeshalAlamr/wav2vec2-xls-r-300m-ar-2) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5567
- Wer: 0.3115

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 0.1654        | 1.18  | 400   | 0.5815          | 0.4237 |
| 0.3412        | 2.35  | 800   | 0.5534          | 0.4479 |
| 0.4661        | 1.77  | 1200  | 0.6339          | 0.4915 |
| 0.441         | 2.36  | 1600  | 0.6435          | 0.5016 |
| 0.3273        | 5.88  | 2000  | 0.5338          | 0.4361 |
| 0.3099        | 7.06  | 2400  | 0.5570          | 0.4303 |
| 0.2833        | 8.24  | 2800  | 0.5731          | 0.4427 |
| 0.2714        | 9.41  | 3200  | 0.5551          | 0.4212 |
| 0.2598        | 10.59 | 3600  | 0.5757          | 0.4214 |
| 0.2458        | 11.76 | 4000  | 0.5269          | 0.4065 |
| 0.2316        | 12.94 | 4400  | 0.5469          | 0.4053 |
| 0.219         | 14.12 | 4800  | 0.5539          | 0.3912 |
| 0.2022        | 15.29 | 5200  | 0.5773          | 0.3887 |
| 0.1771        | 16.47 | 5600  | 0.5374          | 0.3623 |
| 0.176         | 17.65 | 6000  | 0.5545          | 0.3763 |
| 0.1645        | 18.82 | 6400  | 0.5332          | 0.3580 |
| 0.1501        | 20.0  | 6800  | 0.5496          | 0.3614 |
| 0.1372        | 21.18 | 7200  | 0.5716          | 0.3608 |
| 0.1325        | 22.35 | 7600  | 0.5476          | 0.3475 |
| 0.1233        | 23.53 | 8000  | 0.5657          | 0.3412 |
| 0.1148        | 24.71 | 8400  | 0.5399          | 0.3324 |
| 0.1058        | 25.88 | 8800  | 0.5678          | 0.3323 |
| 0.1004        | 27.06 | 9200  | 0.5648          | 0.3252 |
| 0.0953        | 28.24 | 9600  | 0.5594          | 0.3159 |
| 0.0875        | 29.41 | 10000 | 0.5567          | 0.3115 |


### Framework versions

- Transformers 4.14.1
- Pytorch 1.11.0
- Datasets 1.18.3
- Tokenizers 0.10.3
