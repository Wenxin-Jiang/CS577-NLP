---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: sagemaker-bert-mini-arabic
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sagemaker-bert-mini-arabic

This model is a fine-tuned version of [asafaya/bert-mini-arabic](https://huggingface.co/asafaya/bert-mini-arabic) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2531
- Accuracy: 0.8974

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 32
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.3385        | 1.0   | 1469 | 0.2707          | 0.8840   |
| 0.2416        | 2.0   | 2938 | 0.2531          | 0.8974   |


### Framework versions

- Transformers 4.12.3
- Pytorch 1.9.1
- Datasets 1.15.1
- Tokenizers 0.10.3
