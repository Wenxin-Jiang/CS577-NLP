---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wsj0-5percent-supervised
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wsj0-5percent-supervised

This model is a fine-tuned version of [facebook/wav2vec2-large-lv60](https://huggingface.co/facebook/wav2vec2-large-lv60) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3883
- Wer: 0.1555

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
- train_batch_size: 12
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 300
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 6.0248        | 16.67  | 500  | 2.9406          | 1.0    |
| 2.0466        | 33.33  | 1000 | 0.3935          | 0.3300 |
| 0.1486        | 50.0   | 1500 | 0.3091          | 0.1931 |
| 0.052         | 66.67  | 2000 | 0.3562          | 0.2052 |
| 0.0309        | 83.33  | 2500 | 0.3252          | 0.1773 |
| 0.0228        | 100.0  | 3000 | 0.3360          | 0.1652 |
| 0.0177        | 116.67 | 3500 | 0.3423          | 0.1603 |
| 0.0142        | 133.33 | 4000 | 0.3416          | 0.1611 |
| 0.0119        | 150.0  | 4500 | 0.3663          | 0.1583 |
| 0.0094        | 166.67 | 5000 | 0.3617          | 0.1567 |
| 0.0093        | 183.33 | 5500 | 0.3738          | 0.1668 |
| 0.0079        | 200.0  | 6000 | 0.3881          | 0.1652 |
| 0.0065        | 216.67 | 6500 | 0.3752          | 0.1611 |
| 0.0056        | 233.33 | 7000 | 0.3798          | 0.1603 |
| 0.0057        | 250.0  | 7500 | 0.3944          | 0.1624 |
| 0.0047        | 266.67 | 8000 | 0.4038          | 0.1583 |
| 0.0041        | 283.33 | 8500 | 0.3928          | 0.1547 |
| 0.0036        | 300.0  | 9000 | 0.3883          | 0.1555 |


### Framework versions

- Transformers 4.14.1
- Pytorch 1.10.2
- Datasets 1.18.2
- Tokenizers 0.10.3
