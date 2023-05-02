---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-xls-r-bengali_v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-xls-r-bengali_v1

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 3.2973
- Wer: 1.0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 6
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer |
|:-------------:|:-----:|:----:|:---------------:|:---:|
| 8.7896        | 0.8   | 500  | 3.8455          | 1.0 |
| 3.3871        | 1.6   | 1000 | 3.2862          | 1.0 |
| 3.3302        | 2.4   | 1500 | 3.3086          | 1.0 |
| 3.3259        | 3.2   | 2000 | 3.2973          | 1.0 |
| 3.325         | 4.0   | 2500 | 3.2973          | 1.0 |
| 3.3178        | 4.8   | 3000 | 3.2973          | 1.0 |
| 3.3226        | 5.6   | 3500 | 3.2973          | 1.0 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
