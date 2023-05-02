---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: distilbert-base-uncasedsexist_with_reddit_and_gab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncasedsexist_with_reddit_and_gab

This model is a fine-tuned version of [Wiebke/distilbert-base-uncasedsexist_baseline](https://huggingface.co/Wiebke/distilbert-base-uncasedsexist_baseline) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3249
- Accuracy: 0.8671
- F1: 0.8641

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.0285        | 0.2   | 500  | 0.3733          | 0.87     | 0.8613 |
| 0.0276        | 0.4   | 1000 | 0.3660          | 0.8386   | 0.8411 |
| 0.0245        | 0.6   | 1500 | 0.3575          | 0.865    | 0.8564 |
| 0.0239        | 0.81  | 2000 | 0.3249          | 0.8671   | 0.8641 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
