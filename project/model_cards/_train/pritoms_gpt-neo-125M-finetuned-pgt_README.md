---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- null
model-index:
- name: gpt-neo-125M-finetuned-pgt
  results:
  - task:
      name: Causal Language Modeling
      type: text-generation
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt-neo-125M-finetuned-pgt

This model is a fine-tuned version of [pritoms/gpt-neo-125M-finetuned-pgt](https://huggingface.co/pritoms/gpt-neo-125M-finetuned-pgt) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6026

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 26   | 1.5947          |
| No log        | 2.0   | 52   | 1.5963          |
| No log        | 3.0   | 78   | 1.6026          |


### Framework versions

- Transformers 4.10.0
- Pytorch 1.9.0+cu102
- Datasets 1.11.0
- Tokenizers 0.10.3
