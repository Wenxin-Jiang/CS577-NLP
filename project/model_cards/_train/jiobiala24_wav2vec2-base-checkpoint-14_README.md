---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-base-checkpoint-14
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-checkpoint-14

This model is a fine-tuned version of [jiobiala24/wav2vec2-base-checkpoint-13](https://huggingface.co/jiobiala24/wav2vec2-base-checkpoint-13) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2822
- Wer: 0.4068

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
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 0.1996        | 1.59  | 1000  | 0.7181          | 0.4079 |
| 0.1543        | 3.17  | 2000  | 0.7735          | 0.4113 |
| 0.1171        | 4.76  | 3000  | 0.8152          | 0.4045 |
| 0.0969        | 6.35  | 4000  | 0.8575          | 0.4142 |
| 0.082         | 7.94  | 5000  | 0.9005          | 0.4124 |
| 0.074         | 9.52  | 6000  | 0.9232          | 0.4151 |
| 0.0653        | 11.11 | 7000  | 0.9680          | 0.4223 |
| 0.0587        | 12.7  | 8000  | 1.0633          | 0.4232 |
| 0.0551        | 14.29 | 9000  | 1.0875          | 0.4171 |
| 0.0498        | 15.87 | 10000 | 1.0281          | 0.4105 |
| 0.0443        | 17.46 | 11000 | 1.2164          | 0.4274 |
| 0.0421        | 19.05 | 12000 | 1.1868          | 0.4191 |
| 0.0366        | 20.63 | 13000 | 1.1678          | 0.4173 |
| 0.0366        | 22.22 | 14000 | 1.2444          | 0.4187 |
| 0.0346        | 23.81 | 15000 | 1.2042          | 0.4169 |
| 0.0316        | 25.4  | 16000 | 1.3019          | 0.4127 |
| 0.0296        | 26.98 | 17000 | 1.2001          | 0.4081 |
| 0.0281        | 28.57 | 18000 | 1.2822          | 0.4068 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu111
- Datasets 1.13.3
- Tokenizers 0.10.3
