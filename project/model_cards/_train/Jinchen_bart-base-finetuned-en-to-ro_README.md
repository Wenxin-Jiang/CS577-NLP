---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wmt16
model-index:
- name: bart-base-finetuned-en-to-ro
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-base-finetuned-en-to-ro

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on the wmt16 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9912

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: IPU
- gradient_accumulation_steps: 128
- total_train_batch_size: 512
- total_eval_batch_size: 24
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- training precision: Mixed Precision

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.5409        | 1.0   | 1192 | 1.9912          |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.10.0+cpu
- Datasets 2.4.0
- Tokenizers 0.12.1
