---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- filipino_voice
model-index:
- name: english-filipino-wav2vec2-l-xls-r-test-05
  results: []
---
# english-filipino-wav2vec2-l-xls-r-test-05

## Model description

This model is a fine-tuned version of [jonatasgrosman/wav2vec2-large-xlsr-53-english](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english) on the filipino_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4738
- Wer: 0.2684

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
| 3.3328        | 2.09  | 400  | 2.2174          | 0.9733 |
| 0.6432        | 4.19  | 800  | 0.3735          | 0.3896 |
| 0.2741        | 6.28  | 1200 | 0.3639          | 0.3425 |
| 0.1877        | 8.38  | 1600 | 0.3506          | 0.3425 |
| 0.1408        | 10.47 | 2000 | 0.3644          | 0.3181 |
| 0.1133        | 12.57 | 2400 | 0.3837          | 0.3047 |
| 0.0953        | 14.66 | 2800 | 0.4415          | 0.3103 |
| 0.0814        | 16.75 | 3200 | 0.3940          | 0.3092 |
| 0.0707        | 18.85 | 3600 | 0.4164          | 0.3013 |
| 0.059         | 20.94 | 4000 | 0.4488          | 0.2983 |
| 0.0545        | 23.04 | 4400 | 0.4803          | 0.3028 |
| 0.0482        | 25.13 | 4800 | 0.4731          | 0.2811 |
| 0.0426        | 27.23 | 5200 | 0.4606          | 0.2757 |
| 0.0395        | 29.32 | 5600 | 0.4738          | 0.2684 |

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 1.18.3
- Tokenizers 0.10.3
