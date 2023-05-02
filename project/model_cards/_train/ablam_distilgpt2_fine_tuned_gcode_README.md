---
tags:
- generated_from_trainer
model-index:
- name: distilgpt2_fine_tuned_gcode
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilgpt2_fine_tuned_gcode

This model is a fine-tuned version of [congcongwang/distilgpt2_fine_tuned_coder](https://huggingface.co/congcongwang/distilgpt2_fine_tuned_coder) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.1670

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.1
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 4.1754        | 1.0   | 52144 | 4.1670          |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1
- Datasets 2.1.0
- Tokenizers 0.10.3
