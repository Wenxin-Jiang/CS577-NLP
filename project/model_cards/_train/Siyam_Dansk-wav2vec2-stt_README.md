---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: Dansk-wav2vec2-stt
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Dansk-wav2vec2-stt

This model is a fine-tuned version of [Siyam/Dansk-wav2vec21](https://huggingface.co/Siyam/Dansk-wav2vec21) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7500
- Wer: 0.3929

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
| 0.0298        | 4.26  | 400  | 0.8420          | 0.4579 |
| 0.0479        | 8.51  | 800  | 0.8713          | 0.4461 |
| 0.0387        | 12.77 | 1200 | 0.8307          | 0.4404 |
| 0.0336        | 17.02 | 1600 | 0.8322          | 0.4144 |
| 0.0322        | 21.28 | 2000 | 0.7493          | 0.4081 |
| 0.0288        | 25.53 | 2400 | 0.7361          | 0.3951 |
| 0.0264        | 29.79 | 2800 | 0.7500          | 0.3929 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 2.1.0
- Tokenizers 0.10.3
