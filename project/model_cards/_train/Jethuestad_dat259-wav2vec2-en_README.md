---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice_1_0
model-index:
- name: dat259-wav2vec2-en
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dat259-wav2vec2-en

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the common_voice_1_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5042
- Wer: 0.5793

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 200
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 4.2531        | 1.82  | 200  | 3.0566          | 1.0    |
| 2.1194        | 3.64  | 400  | 1.6370          | 0.7706 |
| 0.6464        | 5.45  | 600  | 1.3950          | 0.6694 |
| 0.3891        | 7.27  | 800  | 1.4443          | 0.6525 |
| 0.2783        | 9.09  | 1000 | 1.4309          | 0.6152 |
| 0.2088        | 10.91 | 1200 | 1.3592          | 0.5960 |
| 0.1685        | 12.73 | 1400 | 1.4690          | 0.6031 |
| 0.1397        | 14.55 | 1600 | 1.4691          | 0.5819 |
| 0.1209        | 16.36 | 1800 | 1.5004          | 0.5840 |
| 0.1122        | 18.18 | 2000 | 1.5069          | 0.5806 |
| 0.1025        | 20.0  | 2200 | 1.5042          | 0.5793 |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu102
- Datasets 2.4.0
- Tokenizers 0.12.1
