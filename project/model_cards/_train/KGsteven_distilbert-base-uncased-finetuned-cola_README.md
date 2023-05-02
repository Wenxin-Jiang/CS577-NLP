---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- matthews_correlation
model-index:
- name: distilbert-base-uncased-finetuned-cola
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-cola

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3038
- Matthews Correlation: 0.9198

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Matthews Correlation |
|:-------------:|:-----:|:----:|:---------------:|:--------------------:|
| 1.2169        | 1.0   | 626  | 0.6782          | 0.8605               |
| 0.5513        | 2.0   | 1252 | 0.4085          | 0.8998               |
| 0.343         | 3.0   | 1878 | 0.3346          | 0.9122               |
| 0.1642        | 4.0   | 2504 | 0.3106          | 0.9165               |
| 0.1216        | 5.0   | 3130 | 0.3038          | 0.9198               |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Tokenizers 0.13.1
