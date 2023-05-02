---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tweet_eval
metrics:
- f1
model-index:
- name: irony_trained_1234567
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: tweet_eval
      type: tweet_eval
      args: irony
    metrics:
    - name: F1
      type: f1
      value: 0.6765645067647214
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# irony_trained_1234567

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the tweet_eval dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6580
- F1: 0.6766

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2.6774391860025942e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 1234567
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.6608        | 1.0   | 716  | 0.6057          | 0.6704 |
| 0.5329        | 2.0   | 1432 | 0.8935          | 0.6621 |
| 0.3042        | 3.0   | 2148 | 1.3871          | 0.6822 |
| 0.1769        | 4.0   | 2864 | 1.6580          | 0.6766 |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.9.1
- Datasets 1.16.1
- Tokenizers 0.10.3
