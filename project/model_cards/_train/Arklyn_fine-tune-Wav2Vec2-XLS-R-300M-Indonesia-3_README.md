---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice_10_0
model-index:
- name: fine-tune-Wav2Vec2-XLS-R-300M-Indonesia-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# fine-tune-Wav2Vec2-XLS-R-300M-Indonesia-3

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice_10_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2856
- Wer: 0.1931

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
- train_batch_size: 36
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 72
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 60
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 2.8503        | 4.0   | 460  | 1.2215          | 0.8013 |
| 0.2917        | 8.0   | 920  | 0.2824          | 0.3055 |
| 0.1487        | 12.0  | 1380 | 0.2719          | 0.2593 |
| 0.0904        | 16.0  | 1840 | 0.2536          | 0.2448 |
| 0.0741        | 20.0  | 2300 | 0.2620          | 0.2325 |
| 0.0635        | 24.0  | 2760 | 0.2953          | 0.2354 |
| 0.0541        | 28.0  | 3220 | 0.2683          | 0.2184 |
| 0.048         | 32.0  | 3680 | 0.2707          | 0.2097 |
| 0.0435        | 36.0  | 4140 | 0.2764          | 0.2111 |
| 0.0377        | 40.0  | 4600 | 0.2874          | 0.2048 |
| 0.0352        | 44.0  | 5060 | 0.2758          | 0.1999 |
| 0.0304        | 48.0  | 5520 | 0.2808          | 0.1969 |
| 0.0285        | 52.0  | 5980 | 0.2860          | 0.1943 |
| 0.0258        | 56.0  | 6440 | 0.2867          | 0.1943 |
| 0.0239        | 60.0  | 6900 | 0.2856          | 0.1931 |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.10.0+cu113
- Datasets 2.5.2
- Tokenizers 0.12.1
