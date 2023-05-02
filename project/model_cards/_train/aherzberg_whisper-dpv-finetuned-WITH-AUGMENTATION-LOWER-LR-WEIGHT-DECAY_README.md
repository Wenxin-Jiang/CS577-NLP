---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: whisper-dpv-finetuned-WITH-AUGMENTATION-LOWER-LR-WEIGHT-DECAY
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-dpv-finetuned-WITH-AUGMENTATION-LOWER-LR-WEIGHT-DECAY

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-medium) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8435
- Wer: 35.0215

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
| 0.5839        | 0.62  | 1000 | 0.5726          | 37.4633 |
| 0.2068        | 1.25  | 2000 | 0.5799          | 36.4911 |
| 0.1451        | 1.87  | 3000 | 0.6284          | 36.0389 |
| 0.0606        | 2.49  | 4000 | 0.7208          | 36.4006 |
| 0.0081        | 3.12  | 5000 | 0.8024          | 34.9537 |
| 0.0131        | 3.74  | 6000 | 0.8435          | 35.0215 |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.12.1
- Datasets 2.7.1
- Tokenizers 0.13.2
