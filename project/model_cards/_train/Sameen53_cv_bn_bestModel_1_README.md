---
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: cv_bn_bestModel_1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# cv_bn_bestModel_1

This model is a fine-tuned version of [Sameen53/facebook_large_CV_bn3](https://huggingface.co/Sameen53/facebook_large_CV_bn3) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1780
- Wer: 0.2315

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-06
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 200
- num_epochs: 6
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.1588        | 1.3   | 1500 | 0.2097          | 0.2315 |
| 0.2126        | 2.6   | 3000 | 0.1941          | 0.2310 |
| 0.2242        | 3.9   | 4500 | 0.1834          | 0.2307 |
| 0.2303        | 5.2   | 6000 | 0.1780          | 0.2315 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
