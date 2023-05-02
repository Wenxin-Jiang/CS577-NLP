---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xls-r-300m-ar-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-ar-2

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4764
- Wer: 0.3073

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
| 1.0851        | 1.18  | 400   | 0.5614          | 0.4888 |
| 0.691         | 2.35  | 800   | 0.6557          | 0.5558 |
| 0.6128        | 3.53  | 1200  | 0.5852          | 0.5070 |
| 0.543         | 4.71  | 1600  | 0.5591          | 0.4838 |
| 0.5185        | 5.88  | 2000  | 0.6649          | 0.5514 |
| 0.4816        | 7.06  | 2400  | 0.5598          | 0.4689 |
| 0.4336        | 8.24  | 2800  | 0.5384          | 0.4515 |
| 0.405         | 9.41  | 3200  | 0.4987          | 0.4138 |
| 0.3811        | 10.59 | 3600  | 0.5427          | 0.4644 |
| 0.3539        | 11.76 | 4000  | 0.4881          | 0.4159 |
| 0.3299        | 12.94 | 4400  | 0.5160          | 0.4198 |
| 0.3096        | 14.12 | 4800  | 0.5019          | 0.4077 |
| 0.2881        | 15.29 | 5200  | 0.5146          | 0.4140 |
| 0.2894        | 16.47 | 5600  | 0.4861          | 0.4026 |
| 0.2461        | 17.65 | 6000  | 0.4765          | 0.3742 |
| 0.2371        | 18.82 | 6400  | 0.4679          | 0.3672 |
| 0.2182        | 20.0  | 6800  | 0.4699          | 0.3603 |
| 0.1942        | 21.18 | 7200  | 0.4769          | 0.3519 |
| 0.1823        | 22.35 | 7600  | 0.4719          | 0.3497 |
| 0.1682        | 23.53 | 8000  | 0.4876          | 0.3456 |
| 0.1526        | 24.71 | 8400  | 0.4591          | 0.3300 |
| 0.137         | 25.88 | 8800  | 0.4819          | 0.3314 |
| 0.1283        | 27.06 | 9200  | 0.4823          | 0.3213 |
| 0.1174        | 28.24 | 9600  | 0.4879          | 0.3174 |
| 0.1104        | 29.41 | 10000 | 0.4764          | 0.3073 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0
- Datasets 1.18.4
- Tokenizers 0.11.6
