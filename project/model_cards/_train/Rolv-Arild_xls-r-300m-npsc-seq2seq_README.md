---
tags:
- generated_from_trainer
model-index:
- name: ''
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model was trained from scratch on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2965
- Wer: 0.3144

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
- gradient_accumulation_steps: 8
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 20.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 2.888         | 0.51  | 400   | 3.7320          | 0.9440 |
| 3.1636        | 1.02  | 800   | 2.9188          | 1.1916 |
| 2.773         | 1.53  | 1200  | 2.3347          | 1.0134 |
| 0.7198        | 2.04  | 1600  | 0.6678          | 0.4826 |
| 0.5255        | 2.55  | 2000  | 0.4605          | 0.4135 |
| 0.3961        | 3.06  | 2400  | 0.4266          | 0.3955 |
| 0.3424        | 3.57  | 2800  | 0.3786          | 0.3741 |
| 0.3858        | 4.08  | 3200  | 0.3161          | 0.3552 |
| 0.3218        | 4.59  | 3600  | 0.3029          | 0.3510 |
| 0.199         | 5.1   | 4000  | 0.2988          | 0.3418 |
| 0.2054        | 5.61  | 4400  | 0.2873          | 0.3434 |
| 0.1704        | 6.12  | 4800  | 0.3129          | 0.3432 |
| 0.1805        | 6.63  | 5200  | 0.2963          | 0.3413 |
| 0.2091        | 7.14  | 5600  | 0.2755          | 0.3329 |
| 0.1971        | 7.65  | 6000  | 0.2706          | 0.3309 |
| 0.1237        | 8.16  | 6400  | 0.2823          | 0.3270 |
| 0.123         | 8.67  | 6800  | 0.2754          | 0.3246 |
| 0.103         | 9.18  | 7200  | 0.2917          | 0.3272 |
| 0.1143        | 9.69  | 7600  | 0.2885          | 0.3305 |
| 0.156         | 10.2  | 8000  | 0.2810          | 0.3288 |
| 0.167         | 10.71 | 8400  | 0.2689          | 0.3232 |
| 0.0815        | 11.22 | 8800  | 0.2899          | 0.3236 |
| 0.0844        | 11.73 | 9200  | 0.2798          | 0.3225 |
| 0.0775        | 12.24 | 9600  | 0.2894          | 0.3224 |
| 0.0677        | 12.75 | 10000 | 0.2838          | 0.3204 |
| 0.1383        | 13.27 | 10400 | 0.2959          | 0.3211 |
| 0.1233        | 13.77 | 10800 | 0.2922          | 0.3213 |
| 0.0688        | 14.29 | 11200 | 0.2903          | 0.3209 |
| 0.0655        | 14.8  | 11600 | 0.2868          | 0.3182 |
| 0.0449        | 15.31 | 12000 | 0.2959          | 0.3172 |
| 0.0421        | 15.82 | 12400 | 0.2966          | 0.3180 |
| 0.0858        | 16.33 | 12800 | 0.2941          | 0.3164 |
| 0.0859        | 16.84 | 13200 | 0.2980          | 0.3165 |
| 0.0561        | 17.35 | 13600 | 0.2965          | 0.3165 |
| 0.0506        | 17.86 | 14000 | 0.2935          | 0.3148 |
| 0.0312        | 18.37 | 14400 | 0.2964          | 0.3154 |
| 0.0403        | 18.88 | 14800 | 0.2967          | 0.3160 |
| 0.0924        | 19.39 | 15200 | 0.2955          | 0.3147 |
| 0.0585        | 19.9  | 15600 | 0.2965          | 0.3144 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.0+cu113
- Datasets 1.18.1
- Tokenizers 0.11.0
