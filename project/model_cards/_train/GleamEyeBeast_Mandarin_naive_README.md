---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: Mandarin_naive
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Mandarin_naive

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4584
- Wer: 0.3999

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
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 4.8963        | 3.67  | 400  | 1.0645          | 0.8783 |
| 0.5506        | 7.34  | 800  | 0.5032          | 0.5389 |
| 0.2111        | 11.01 | 1200 | 0.4765          | 0.4712 |
| 0.1336        | 14.68 | 1600 | 0.4815          | 0.4511 |
| 0.0974        | 18.35 | 2000 | 0.4956          | 0.4370 |
| 0.0748        | 22.02 | 2400 | 0.4881          | 0.4235 |
| 0.0584        | 25.69 | 2800 | 0.4732          | 0.4193 |
| 0.0458        | 29.36 | 3200 | 0.4584          | 0.3999 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
