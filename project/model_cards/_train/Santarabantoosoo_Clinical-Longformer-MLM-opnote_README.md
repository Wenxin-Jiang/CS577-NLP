---
tags:
- generated_from_trainer
model-index:
- name: Clinical-Longformer-MLM-opnote
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Clinical-Longformer-MLM-opnote

This model is a fine-tuned version of [yikuan8/Clinical-Longformer](https://huggingface.co/yikuan8/Clinical-Longformer) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8286

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
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 4
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 266  | 0.9606          |
| 1.1655        | 2.0   | 532  | 0.8677          |
| 1.1655        | 3.0   | 798  | 0.8195          |


### Framework versions

- Transformers 4.19.1
- Pytorch 1.10.1
- Datasets 2.2.1
- Tokenizers 0.12.1
