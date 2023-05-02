---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: whisper-small-ar
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-small-ar

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.8342
- Wer: 82.3706

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 4000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.6454        | 5.0   | 1000 | 1.8790          | 86.8695 |
| 0.0408        | 10.0  | 2000 | 2.4389          | 80.5579 |
| 0.0043        | 15.0  | 3000 | 2.7456          | 82.2767 |
| 0.002         | 20.0  | 4000 | 2.8342          | 82.3706 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
