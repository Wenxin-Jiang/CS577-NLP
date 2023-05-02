---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- matthews_correlation
model-index:
- name: distilbert-base-uncased-finetuned-cola-v3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-cola-v3

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9655
- Matthews Correlation: 0.7369

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
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | Matthews Correlation |
|:-------------:|:-----:|:----:|:---------------:|:--------------------:|
| No log        | 1.0   | 8    | 1.9112          | 0.1486               |
| No log        | 2.0   | 16   | 1.8626          | 0.1273               |
| No log        | 3.0   | 24   | 1.7793          | 0.1947               |
| No log        | 4.0   | 32   | 1.6722          | 0.1681               |
| No log        | 5.0   | 40   | 1.5578          | 0.3876               |
| No log        | 6.0   | 48   | 1.4463          | 0.5551               |
| No log        | 7.0   | 56   | 1.3280          | 0.5498               |
| No log        | 8.0   | 64   | 1.2302          | 0.5936               |
| No log        | 9.0   | 72   | 1.1408          | 0.6998               |
| No log        | 10.0  | 80   | 1.0765          | 0.6601               |
| No log        | 11.0  | 88   | 1.0145          | 0.6988               |
| No log        | 12.0  | 96   | 0.9655          | 0.7369               |
| No log        | 13.0  | 104  | 0.9389          | 0.6992               |
| No log        | 14.0  | 112  | 0.9258          | 0.6992               |
| No log        | 15.0  | 120  | 0.9209          | 0.6992               |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
