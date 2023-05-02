---
tags:
- generated_from_trainer
model-index:
- name: gpt2-xl-ft-value_it-1k-0_on_1k-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-xl-ft-value_it-1k-0_on_1k-1

This model is a fine-tuned version of [newtonkwan/gpt2-xl-ft-0](https://huggingface.co/newtonkwan/gpt2-xl-ft-0) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8666

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 2022
- gradient_accumulation_steps: 32
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100.0
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 0.96  | 3    | 1.9325          |
| No log        | 1.96  | 6    | 1.9178          |
| No log        | 2.96  | 9    | 1.8947          |
| No log        | 3.96  | 12   | 1.8666          |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6


### Perplexity
Score: 17.54938316345215