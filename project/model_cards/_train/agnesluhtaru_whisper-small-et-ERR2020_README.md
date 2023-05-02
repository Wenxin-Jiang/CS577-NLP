---
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
metrics:
- wer
model-index:
- name: whisper-small-et-ERR2020
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-small-et-ERR2020

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5321
- Wer: 22.8462

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
- train_batch_size: 64
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- training_steps: 10000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer     |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|
| 0.3387        | 0.1   | 1000  | 0.5383          | 33.8216 |
| 0.1393        | 0.2   | 2000  | 0.4897          | 27.7546 |
| 0.0982        | 0.3   | 3000  | 0.5477          | 26.7815 |
| 0.0912        | 1.02  | 4000  | 0.5195          | 24.8816 |
| 0.0811        | 1.12  | 5000  | 0.5373          | 25.9282 |
| 0.0649        | 1.22  | 6000  | 0.5422          | 23.7285 |
| 0.0618        | 1.32  | 7000  | 0.5504          | 23.5179 |
| 0.0558        | 2.03  | 8000  | 0.5321          | 22.8462 |
| 0.0452        | 2.13  | 9000  | 0.5543          | 23.5813 |
| 0.0462        | 2.23  | 10000 | 0.5424          | 22.8830 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.12.1+rocm5.1.1
- Datasets 2.7.1.dev0
- Tokenizers 0.13.2
