---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: SKYLy
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# SKYLy

This model is a fine-tuned version of [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7645
- Wer: 0.4083

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
| 4.4215        | 4.26  | 400  | 1.6323          | 0.9857 |
| 0.5716        | 8.51  | 800  | 0.6679          | 0.5107 |
| 0.1721        | 12.77 | 1200 | 0.6935          | 0.4632 |
| 0.1063        | 17.02 | 1600 | 0.7533          | 0.4432 |
| 0.0785        | 21.28 | 2000 | 0.7208          | 0.4255 |
| 0.0608        | 25.53 | 2400 | 0.7481          | 0.4117 |
| 0.0493        | 29.79 | 2800 | 0.7645          | 0.4083 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu113
- Datasets 2.1.0
- Tokenizers 0.10.3
