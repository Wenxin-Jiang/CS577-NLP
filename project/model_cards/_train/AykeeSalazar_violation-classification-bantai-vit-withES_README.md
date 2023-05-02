---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- image_folder
model-index:
- name: violation-classification-bantai-vit-withES
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# violation-classification-bantai-vit-withES

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the image_folder dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.2234
- eval_accuracy: 0.9592
- eval_runtime: 64.9173
- eval_samples_per_second: 85.37
- eval_steps_per_second: 2.68
- epoch: 227.72
- step: 23000

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 500

### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1
