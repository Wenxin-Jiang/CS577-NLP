---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: farsi_lastname_classifier_4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# farsi_lastname_classifier_4

This model is a fine-tuned version of [microsoft/deberta-v3-small](https://huggingface.co/microsoft/deberta-v3-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2337
- Accuracy: 0.96

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 128
- eval_batch_size: 256
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 15
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 12   | 0.5673          | 0.836    |
| No log        | 2.0   | 24   | 0.4052          | 0.868    |
| No log        | 3.0   | 36   | 0.2211          | 0.932    |
| No log        | 4.0   | 48   | 0.2488          | 0.926    |
| No log        | 5.0   | 60   | 0.1490          | 0.954    |
| No log        | 6.0   | 72   | 0.1464          | 0.968    |
| No log        | 7.0   | 84   | 0.1923          | 0.954    |
| No log        | 8.0   | 96   | 0.2070          | 0.96     |
| No log        | 9.0   | 108  | 0.2055          | 0.962    |
| No log        | 10.0  | 120  | 0.2436          | 0.942    |
| No log        | 11.0  | 132  | 0.2173          | 0.96     |
| No log        | 12.0  | 144  | 0.2342          | 0.956    |
| No log        | 13.0  | 156  | 0.2337          | 0.962    |
| No log        | 14.0  | 168  | 0.2332          | 0.96     |
| No log        | 15.0  | 180  | 0.2337          | 0.96     |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.2
