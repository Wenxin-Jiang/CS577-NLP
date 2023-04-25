---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-base-TPU-cv-fine-tune-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-TPU-cv-fine-tune-2

This model is a fine-tuned version of [jiobiala24/wav2vec2-base-TPU-cv-fine-tune](https://huggingface.co/jiobiala24/wav2vec2-base-TPU-cv-fine-tune) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6051
- Wer: 0.5484

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

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.522         | 6.45  | 400  | 1.2550          | 0.5649 |
| 0.2874        | 12.9  | 800  | 1.4235          | 0.6054 |
| 0.152         | 19.35 | 1200 | 1.5743          | 0.5806 |
| 0.0857        | 25.8  | 1600 | 1.6051          | 0.5484 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu111
- Datasets 1.13.3
- Tokenizers 0.10.3
