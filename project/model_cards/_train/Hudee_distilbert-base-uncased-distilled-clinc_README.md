---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased-distilled-clinc
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-distilled-clinc

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0272
- Accuracy: 0.9287

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
- train_batch_size: 48
- eval_batch_size: 48
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 318  | 0.2337          | 0.6274   |
| 0.3698        | 2.0   | 636  | 0.1052          | 0.8458   |
| 0.3698        | 3.0   | 954  | 0.0650          | 0.8935   |
| 0.1216        | 4.0   | 1272 | 0.0476          | 0.9068   |
| 0.0727        | 5.0   | 1590 | 0.0386          | 0.9181   |
| 0.0727        | 6.0   | 1908 | 0.0336          | 0.9219   |
| 0.0556        | 7.0   | 2226 | 0.0305          | 0.9229   |
| 0.0477        | 8.0   | 2544 | 0.0287          | 0.9287   |
| 0.0477        | 9.0   | 2862 | 0.0276          | 0.9274   |
| 0.0441        | 10.0  | 3180 | 0.0272          | 0.9287   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Tokenizers 0.13.2
