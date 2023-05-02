---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
- accuracy
model-index:
- name: distilbert-base-uncased_research_articles_multilabel
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased_research_articles_multilabel

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1956
- F1: 0.8395
- Roc Auc: 0.8909
- Accuracy: 0.6977

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     | Roc Auc | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:------:|:-------:|:--------:|
| 0.3043        | 1.0   | 263  | 0.2199          | 0.8198 | 0.8686  | 0.6829   |
| 0.2037        | 2.0   | 526  | 0.1988          | 0.8355 | 0.8845  | 0.7010   |
| 0.1756        | 3.0   | 789  | 0.1956          | 0.8395 | 0.8909  | 0.6977   |
| 0.1579        | 4.0   | 1052 | 0.1964          | 0.8371 | 0.8902  | 0.6919   |
| 0.1461        | 5.0   | 1315 | 0.1991          | 0.8353 | 0.8874  | 0.6953   |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
