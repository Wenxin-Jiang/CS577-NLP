---
license: mit
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: outputs
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# outputs

This model is a fine-tuned version of [microsoft/deberta-v3-small](https://huggingface.co/microsoft/deberta-v3-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1299
- F1: 0.7010

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 8e-05
- train_batch_size: 256
- eval_batch_size: 512
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| No log        | 1.0   | 23   | 0.2190          | 0.7611 |
| No log        | 2.0   | 46   | 0.1212          | 0.2309 |
| No log        | 3.0   | 69   | 0.1235          | 0.6229 |
| No log        | 4.0   | 92   | 0.1299          | 0.7010 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
