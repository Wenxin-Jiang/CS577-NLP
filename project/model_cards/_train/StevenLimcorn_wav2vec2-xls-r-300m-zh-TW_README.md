---
language:
- zh-TW
license: apache-2.0
tags:
- automatic-speech-recognition
- common_voice
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: ''
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the COMMON_VOICE - ZH-TW dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1786
- Wer: 0.8594
- Cer: 0.2964

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 100.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|
| 64.6189       | 2.51  | 500   | 63.8077         | 1.0    | 1.0    |
| 8.0561        | 5.03  | 1000  | 6.8014          | 1.0    | 1.0    |
| 6.0427        | 7.54  | 1500  | 6.0745          | 1.0    | 1.0    |
| 5.9357        | 10.05 | 2000  | 5.8682          | 1.0    | 1.0    |
| 5.0489        | 12.56 | 2500  | 4.4032          | 0.9990 | 0.7750 |
| 4.6184        | 15.08 | 3000  | 3.8383          | 0.9983 | 0.6768 |
| 4.365         | 17.59 | 3500  | 3.4633          | 0.9959 | 0.6299 |
| 4.1026        | 20.1  | 4000  | 3.0732          | 0.9902 | 0.5814 |
| 3.8655        | 22.61 | 4500  | 2.7638          | 0.9868 | 0.5465 |
| 3.6991        | 25.13 | 5000  | 2.4759          | 0.9811 | 0.5088 |
| 3.4894        | 27.64 | 5500  | 2.2937          | 0.9746 | 0.4852 |
| 3.3983        | 30.15 | 6000  | 2.1684          | 0.9733 | 0.4674 |
| 3.2736        | 32.66 | 6500  | 2.0372          | 0.9659 | 0.4458 |
| 3.1884        | 35.18 | 7000  | 1.9267          | 0.9648 | 0.4329 |
| 3.1248        | 37.69 | 7500  | 1.8408          | 0.9591 | 0.4217 |
| 3.0381        | 40.2  | 8000  | 1.7531          | 0.9503 | 0.4074 |
| 2.9515        | 42.71 | 8500  | 1.6880          | 0.9459 | 0.3967 |
| 2.8704        | 45.23 | 9000  | 1.6264          | 0.9378 | 0.3884 |
| 2.8128        | 47.74 | 9500  | 1.5621          | 0.9341 | 0.3782 |
| 2.7386        | 50.25 | 10000 | 1.5011          | 0.9243 | 0.3664 |
| 2.6646        | 52.76 | 10500 | 1.4608          | 0.9192 | 0.3575 |
| 2.6072        | 55.28 | 11000 | 1.4251          | 0.9148 | 0.3501 |
| 2.569         | 57.79 | 11500 | 1.3837          | 0.9060 | 0.3462 |
| 2.5091        | 60.3  | 12000 | 1.3589          | 0.9070 | 0.3392 |
| 2.4588        | 62.81 | 12500 | 1.3261          | 0.8966 | 0.3284 |
| 2.4083        | 65.33 | 13000 | 1.3052          | 0.8982 | 0.3265 |
| 2.3787        | 67.84 | 13500 | 1.2997          | 0.8908 | 0.3243 |
| 2.3457        | 70.35 | 14000 | 1.2778          | 0.8898 | 0.3187 |
| 2.3099        | 72.86 | 14500 | 1.2661          | 0.8830 | 0.3172 |
| 2.2559        | 75.38 | 15000 | 1.2475          | 0.8851 | 0.3143 |
| 2.2264        | 77.89 | 15500 | 1.2319          | 0.8739 | 0.3085 |
| 2.196         | 80.4  | 16000 | 1.2218          | 0.8722 | 0.3049 |
| 2.1613        | 82.91 | 16500 | 1.2093          | 0.8719 | 0.3051 |
| 2.1455        | 85.43 | 17000 | 1.2055          | 0.8624 | 0.3005 |
| 2.1193        | 87.94 | 17500 | 1.1975          | 0.8600 | 0.2982 |
| 2.0911        | 90.45 | 18000 | 1.1960          | 0.8648 | 0.3003 |
| 2.0884        | 92.96 | 18500 | 1.1871          | 0.8638 | 0.2971 |
| 2.0766        | 95.48 | 19000 | 1.1814          | 0.8617 | 0.2967 |
| 2.0735        | 97.99 | 19500 | 1.1801          | 0.8621 | 0.2969 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0
