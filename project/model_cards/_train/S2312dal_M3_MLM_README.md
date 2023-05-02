---
tags:
- generated_from_trainer
model-index:
- name: M3_MLM
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# M3_MLM

This model is a fine-tuned version of [SpanBERT/spanbert-base-cased](https://huggingface.co/SpanBERT/spanbert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 5.8186

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 9.6707        | 1.0   | 26   | 7.4412          |
| 6.9122        | 2.0   | 52   | 6.3385          |
| 6.2166        | 3.0   | 78   | 5.9148          |


### Framework versions

- Transformers 4.20.0
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
