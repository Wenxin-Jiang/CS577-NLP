---
license: apache-2.0
tags:
- generated_from_trainer
datasets: Gustavosta/Stable-Diffusion-Prompts
widget:
- text: A detective of wolfhound
model-index:
- name: distilgpt2-sd-prompts
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilgpt2-sd-prompts

This model is a fine-tuned version of [distilgpt2](https://huggingface.co/distilgpt2) on [Stable-Diffusion-Prompts](https://huggingface.co/datasets/Gustavosta/Stable-Diffusion-Prompts).
It achieves the following results on the evaluation set:
- Loss: 0.9450

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 500
- num_epochs: 8
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.5122        | 1.93  | 500  | 1.5211          |
| 1.2912        | 3.86  | 1000 | 1.1045          |
| 0.9313        | 5.79  | 1500 | 0.9704          |
| 0.7744        | 7.72  | 2000 | 0.9450          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
