---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-base-casedepoch3_sexist_baseline_with_reddit_and_gab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-casedepoch3_sexist_baseline_with_reddit_and_gab

This model is a fine-tuned version of [Wiebke/bert-base-casedepoch3_sexist_baseline](https://huggingface.co/Wiebke/bert-base-casedepoch3_sexist_baseline) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4434
- Accuracy: 0.8707
- F1: 0.8699

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
| 0.0279        | 0.16  | 500  | 0.5257          | 0.8564   | 0.8540 |
| 0.0273        | 0.31  | 1000 | 0.4614          | 0.8607   | 0.8607 |
| 0.0235        | 0.47  | 1500 | 0.4873          | 0.8657   | 0.8620 |
| 0.0201        | 0.63  | 2000 | 0.4544          | 0.8729   | 0.8694 |
| 0.0215        | 0.78  | 2500 | 0.4597          | 0.865    | 0.8653 |
| 0.0184        | 0.94  | 3000 | 0.4434          | 0.8707   | 0.8699 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
