---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- tweet_eval
metrics:
- f1
model-index:
- name: presentation_irony_31415
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
      value: 0.6753923142373446
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# presentation_irony_31415

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the tweet_eval dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9694
- F1: 0.6754

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.1637764704815665e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 31415
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.6601        | 1.0   | 90   | 0.6298          | 0.6230 |
| 0.4887        | 2.0   | 180  | 0.6039          | 0.6816 |
| 0.2543        | 3.0   | 270  | 0.7362          | 0.6803 |
| 0.1472        | 4.0   | 360  | 0.9694          | 0.6754 |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.9.1
- Datasets 1.16.1
- Tokenizers 0.10.3
