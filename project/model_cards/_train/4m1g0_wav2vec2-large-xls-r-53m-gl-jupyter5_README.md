---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-large-xls-r-53m-gl-jupyter5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-53m-gl-jupyter5

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1025
- Wer: 0.0625

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 60
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 3.6862        | 3.36  | 400  | 0.2455          | 0.2344 |
| 0.1517        | 6.72  | 800  | 0.1195          | 0.1233 |
| 0.0772        | 10.08 | 1200 | 0.1219          | 0.1155 |
| 0.0472        | 13.44 | 1600 | 0.1162          | 0.1034 |
| 0.0357        | 16.8  | 2000 | 0.1070          | 0.1006 |
| 0.0307        | 20.17 | 2400 | 0.1131          | 0.1013 |
| 0.0258        | 23.53 | 2800 | 0.1163          | 0.0847 |
| 0.0229        | 26.89 | 3200 | 0.1100          | 0.0858 |
| 0.0183        | 30.25 | 3600 | 0.1062          | 0.0810 |
| 0.0182        | 33.61 | 4000 | 0.1068          | 0.0800 |
| 0.0151        | 36.97 | 4400 | 0.1088          | 0.0780 |
| 0.0138        | 40.33 | 4800 | 0.1062          | 0.0737 |
| 0.0121        | 43.69 | 5200 | 0.1061          | 0.0722 |
| 0.0088        | 47.06 | 5600 | 0.1055          | 0.0670 |
| 0.008         | 50.42 | 6000 | 0.1059          | 0.0646 |
| 0.007         | 53.78 | 6400 | 0.1020          | 0.0634 |
| 0.0065        | 57.14 | 6800 | 0.1025          | 0.0625 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.1+cu111
- Datasets 1.18.3
- Tokenizers 0.10.3
