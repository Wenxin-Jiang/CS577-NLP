---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: whisper-dpv-finetuned-WITH-AUGMENTATION-LOWER-LR
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-dpv-finetuned-WITH-AUGMENTATION-LOWER-LR

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5717
- Wer: 34.5241

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 4
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.6221        | 0.62  | 1000 | 0.5345          | 35.9711 |
| 0.4318        | 1.25  | 2000 | 0.5271          | 34.9537 |
| 0.3859        | 1.87  | 3000 | 0.5338          | 34.3658 |
| 0.3005        | 2.49  | 4000 | 0.5532          | 34.8858 |
| 0.2444        | 3.12  | 5000 | 0.5628          | 33.7102 |
| 0.315         | 3.74  | 6000 | 0.5717          | 34.5241 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.12.1
- Datasets 2.7.1
- Tokenizers 0.13.2
