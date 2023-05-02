---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: BERTClassificationBaseline
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERTClassificationBaseline

This model is a fine-tuned version of [allenai/scibert_scivocab_uncased](https://huggingface.co/allenai/scibert_scivocab_uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2709
- Accuracy: 0.4

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-06
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 157  | 1.3100          | 0.4286   |
| No log        | 2.0   | 314  | 1.2709          | 0.4      |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1
- Datasets 2.5.2
- Tokenizers 0.11.0
