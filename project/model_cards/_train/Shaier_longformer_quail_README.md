---
tags:
- generated_from_trainer
datasets:
- quail
model-index:
- name: longformer_quail
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# longformer_quail

This model is a fine-tuned version of [allenai/longformer-base-4096](https://huggingface.co/allenai/longformer-base-4096) on the quail dataset.
It achieves the following results on the evaluation set:
- eval_loss: 1.9568
- eval_accuracy: 0.5791
- eval_runtime: 44.254
- eval_samples_per_second: 12.564
- eval_steps_per_second: 6.282
- epoch: 4.0
- step: 816

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 25
- total_train_batch_size: 50
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1
- Datasets 2.5.1
- Tokenizers 0.11.0
