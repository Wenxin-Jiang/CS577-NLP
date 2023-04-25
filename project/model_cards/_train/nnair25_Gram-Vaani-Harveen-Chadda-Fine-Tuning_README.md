---
license: mit
tags:
- generated_from_trainer
model-index:
  name: Gram-Vaani-Harveen-Chadda-Fine-Tuning
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Gram-Vaani-Harveen-Chadda-Fine-Tuning

This model is a fine-tuned version of [Harveenchadha/vakyansh-wav2vec2-hindi-him-4200](https://huggingface.co/Harveenchadha/vakyansh-wav2vec2-hindi-him-4200) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8934
- Wer: 0.359

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

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer   |
|:-------------:|:-----:|:----:|:---------------:|:-----:|
| 4.5558        | 21.05 | 400  | 0.8934          | 0.359 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.10.3
