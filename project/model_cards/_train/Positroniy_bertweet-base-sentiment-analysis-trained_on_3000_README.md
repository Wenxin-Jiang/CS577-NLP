---
tags:
- generated_from_trainer
datasets:
- imdb
metrics:
- accuracy
- f1
model-index:
- name: bertweet-base-sentiment-analysis-trained_on_3000
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: imdb
      type: imdb
      config: plain_text
      split: train
      args: plain_text
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.85
    - name: F1
      type: f1
      value: 0.8504983388704319
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bertweet-base-sentiment-analysis-trained_on_3000

This model is a fine-tuned version of [finiteautomata/bertweet-base-sentiment-analysis](https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis) on the imdb dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3948
- Accuracy: 0.85
- F1: 0.8505

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
- num_epochs: 2

### Training results



### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
