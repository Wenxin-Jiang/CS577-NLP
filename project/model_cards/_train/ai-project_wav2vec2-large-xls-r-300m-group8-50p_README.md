---
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xls-r-300m-vi-25p
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-vi-25p

This model was trained from scratch on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8293
- Wer: 0.4109

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.9542        | 1.31  | 400  | 1.4443          | 0.5703 |
| 1.276         | 2.62  | 800  | 1.4606          | 0.5736 |
| 1.1311        | 3.93  | 1200 | 1.4552          | 0.5186 |
| 0.9519        | 5.25  | 1600 | 1.4477          | 0.5300 |
| 0.8293        | 6.56  | 2000 | 1.4166          | 0.5097 |
| 0.7555        | 7.87  | 2400 | 1.4100          | 0.4906 |
| 0.6724        | 9.18  | 2800 | 1.4982          | 0.4880 |
| 0.6038        | 10.49 | 3200 | 1.4524          | 0.4945 |
| 0.5338        | 11.8  | 3600 | 1.4995          | 0.4798 |
| 0.4988        | 13.11 | 4000 | 1.6715          | 0.4653 |
| 0.461         | 14.43 | 4400 | 1.5699          | 0.4552 |
| 0.4154        | 15.74 | 4800 | 1.5762          | 0.4557 |
| 0.3822        | 17.05 | 5200 | 1.5978          | 0.4471 |
| 0.3466        | 18.36 | 5600 | 1.6579          | 0.4512 |
| 0.3226        | 19.67 | 6000 | 1.6825          | 0.4378 |
| 0.2885        | 20.98 | 6400 | 1.7376          | 0.4421 |
| 0.2788        | 22.29 | 6800 | 1.7150          | 0.4300 |
| 0.249         | 23.61 | 7200 | 1.7073          | 0.4263 |
| 0.2317        | 24.92 | 7600 | 1.7349          | 0.4200 |
| 0.2171        | 26.23 | 8000 | 1.7419          | 0.4186 |
| 0.1963        | 27.54 | 8400 | 1.8438          | 0.4144 |
| 0.1906        | 28.85 | 8800 | 1.8293          | 0.4109 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3
