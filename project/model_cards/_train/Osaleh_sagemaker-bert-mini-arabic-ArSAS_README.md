---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: sagemaker-bert-mini-arabic-ArSAS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sagemaker-bert-mini-arabic-ArSAS

This model is a fine-tuned version of [asafaya/bert-mini-arabic](https://huggingface.co/asafaya/bert-mini-arabic) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3163
- Accuracy: 0.8771

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
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 291  | 0.3761          | 0.8368   |
| 0.4722        | 2.0   | 582  | 0.3163          | 0.8771   |


### Framework versions

- Transformers 4.12.3
- Pytorch 1.9.1
- Datasets 1.15.1
- Tokenizers 0.10.3
