---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-base-casedepoch3_sexist_baseline_with_reddit_and_gab_equal
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-casedepoch3_sexist_baseline_with_reddit_and_gab_equal

This model is a fine-tuned version of [Wiebke/bert-base-casedepoch3_sexist_baseline](https://huggingface.co/Wiebke/bert-base-casedepoch3_sexist_baseline) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4692
- Accuracy: 0.865
- F1: 0.8655

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
| 0.0428        | 0.31  | 500  | 0.5614          | 0.8393   | 0.8433 |
| 0.0377        | 0.61  | 1000 | 0.4765          | 0.8536   | 0.8558 |
| 0.0324        | 0.92  | 1500 | 0.4692          | 0.865    | 0.8655 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
