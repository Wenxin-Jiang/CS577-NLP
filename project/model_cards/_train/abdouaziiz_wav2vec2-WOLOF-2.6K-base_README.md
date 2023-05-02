---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wolof
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wolof

This model is a fine-tuned version of [LeBenchmark/wav2vec2-FR-2.6K-base](https://huggingface.co/LeBenchmark/wav2vec2-FR-2.6K-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2816
- Wer: 0.3897

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
- train_batch_size: 20
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 2.9468        | 1.67  | 1500 | 0.7036          | 0.6418 |
| 0.5506        | 3.33  | 3000 | 0.4129          | 0.5018 |
| 0.3817        | 5.0   | 4500 | 0.3414          | 0.4519 |
| 0.2885        | 6.67  | 6000 | 0.3181          | 0.4305 |
| 0.2275        | 8.33  | 7500 | 0.2920          | 0.4011 |
| 0.1852        | 10.0  | 9000 | 0.2816          | 0.3897 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu102
- Datasets 2.1.0
- Tokenizers 0.12.1
