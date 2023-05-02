---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- amazon_polarity
metrics:
- accuracy
- f1
model-index:
- name: finetuning-sentiment-model-3000-samples
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: amazon_polarity
      type: amazon_polarity
      args: amazon_polarity
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9225
    - name: F1
      type: f1
      value: 0.9240816326530612
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuning-sentiment-model-3000-samples

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the amazon_polarity dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8170
- Accuracy: 0.9225
- F1: 0.9241

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results



### Framework versions

- Transformers 4.19.2
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
