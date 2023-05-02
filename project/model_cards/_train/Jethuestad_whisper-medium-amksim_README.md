---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: whisper-medium-amksim
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-medium-amksim

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9089
- Wer: 40.3433

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 2
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 5
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 4.6349        | 0.83  | 5    | 3.7729          | 73.3906 |
| 3.2338        | 1.67  | 10   | 1.4978          | 69.0987 |
| 1.1335        | 2.5   | 15   | 1.1606          | 97.4249 |
| 0.6838        | 3.33  | 20   | 1.0211          | 66.0944 |
| 0.4383        | 4.17  | 25   | 0.9845          | 65.2361 |
| 0.2514        | 5.0   | 30   | 0.9885          | 61.3734 |
| 0.2053        | 5.83  | 35   | 0.9796          | 76.3948 |
| 0.1353        | 6.67  | 40   | 0.9758          | 49.3562 |
| 0.1142        | 7.5   | 45   | 0.9109          | 60.9442 |
| 0.0889        | 8.33  | 50   | 0.9045          | 41.2017 |
| 0.0854        | 9.17  | 55   | 0.9085          | 42.4893 |
| 0.069         | 10.0  | 60   | 0.9089          | 40.3433 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.13.0
- Datasets 2.6.1
- Tokenizers 0.12.1
