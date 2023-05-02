---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-xls-r-300m-ar-6
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-300m-ar-6

This model is a fine-tuned version of [MeshalAlamr/wav2vec2-xls-r-300m-ar-6](https://huggingface.co/MeshalAlamr/wav2vec2-xls-r-300m-ar-6) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 78.2951
- Wer: 0.2040

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
- train_batch_size: 64
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| No log        | 1.0   | 85   | 75.3576         | 0.2131 |
| No log        | 2.0   | 170  | 75.3215         | 0.2150 |
| No log        | 3.0   | 255  | 75.5332         | 0.2201 |
| No log        | 4.0   | 340  | 81.2835         | 0.2315 |
| 94.75         | 5.0   | 425  | 78.3768         | 0.2422 |
| 94.75         | 6.0   | 510  | 82.9389         | 0.2520 |
| 94.75         | 7.0   | 595  | 76.7272         | 0.2496 |
| 94.75         | 8.0   | 680  | 79.9325         | 0.2506 |
| 94.75         | 9.0   | 765  | 82.2568         | 0.2507 |
| 124.0193      | 10.0  | 850  | 78.7011         | 0.2415 |
| 124.0193      | 11.0  | 935  | 81.2829         | 0.2396 |
| 124.0193      | 12.0  | 1020 | 77.2370         | 0.2357 |
| 124.0193      | 13.0  | 1105 | 77.4057         | 0.2347 |
| 124.0193      | 14.0  | 1190 | 74.4764         | 0.2271 |
| 112.7824      | 15.0  | 1275 | 78.7320         | 0.2355 |
| 112.7824      | 16.0  | 1360 | 79.0120         | 0.2294 |
| 112.7824      | 17.0  | 1445 | 82.3663         | 0.2240 |
| 112.7824      | 18.0  | 1530 | 79.2765         | 0.2236 |
| 98.8702       | 19.0  | 1615 | 78.1527         | 0.2242 |
| 98.8702       | 20.0  | 1700 | 75.7842         | 0.2198 |
| 98.8702       | 21.0  | 1785 | 78.2980         | 0.2217 |
| 98.8702       | 22.0  | 1870 | 79.3180         | 0.2168 |
| 98.8702       | 23.0  | 1955 | 77.7381         | 0.2155 |
| 84.537        | 24.0  | 2040 | 78.1512         | 0.2131 |
| 84.537        | 25.0  | 2125 | 80.4068         | 0.2116 |
| 84.537        | 26.0  | 2210 | 75.5718         | 0.2075 |
| 84.537        | 27.0  | 2295 | 78.4438         | 0.2078 |
| 84.537        | 28.0  | 2380 | 79.6891         | 0.2086 |
| 74.4149       | 29.0  | 2465 | 77.9115         | 0.2069 |
| 74.4149       | 30.0  | 2550 | 78.2951         | 0.2040 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0
- Datasets 1.18.4
- Tokenizers 0.11.6
