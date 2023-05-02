---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- image_folder
model-index:
- name: vc-bantai-vit-withoutAMBI
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vc-bantai-vit-withoutAMBI

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the image_folder dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.2578
- eval_accuracy: 0.9533
- eval_runtime: 31.6691
- eval_samples_per_second: 130.443
- eval_steps_per_second: 2.052
- epoch: 270.26
- step: 10000

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 500

### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1