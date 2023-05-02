---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: bert-large-uncased-finetuned-JD_CV
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-large-uncased-finetuned-JD_CV

This model is a fine-tuned version of [bert-large-uncased](https://huggingface.co/bert-large-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 7.3896

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 1    | 8.2520          |
| No log        | 2.0   | 2    | 7.5931          |
| No log        | 3.0   | 3    | 7.3896          |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.2
