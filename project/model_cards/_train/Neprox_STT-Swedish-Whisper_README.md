---
language:
- sv
license: apache-2.0
tags:
- hf-asr-leaderboard
- generated_from_trainer
metrics:
- wer
model-index:
- name: Whisper Small - Swedish
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small - Swedish

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Common Voice 11.0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4312
- Wer: 19.0503

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
- train_batch_size: 4
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 18000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer     |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|
| 0.0887        | 1.71  | 2000  | 0.2817          | 21.0831 |
| 0.0168        | 3.41  | 4000  | 0.3108          | 19.6338 |
| 0.0027        | 5.12  | 6000  | 0.3421          | 19.8731 |
| 0.0012        | 6.83  | 8000  | 0.3713          | 19.1229 |
| 0.0005        | 8.53  | 10000 | 0.3844          | 19.2036 |
| 0.0004        | 10.24 | 12000 | 0.3900          | 19.0369 |
| 0.0008        | 11.94 | 14000 | 0.4161          | 19.9511 |
| 0.0002        | 13.65 | 16000 | 0.4201          | 19.1283 |
| 0.0001        | 15.36 | 18000 | 0.4312          | 19.0503 |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1
- Datasets 2.7.1
- Tokenizers 0.13.2
