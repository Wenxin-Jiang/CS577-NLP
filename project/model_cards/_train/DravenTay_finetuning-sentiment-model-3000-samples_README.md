---
license: other
tags:
- generated_from_trainer
datasets:
- imdb
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
      name: imdb
      type: imdb
      config: plain_text
      split: train
      args: plain_text
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.92
    - name: F1
      type: f1
      value: 0.9205298013245033
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuning-sentiment-model-3000-samples

This model is a fine-tuned version of [Tianyi98/opt-350m-finetuned-cola](https://huggingface.co/Tianyi98/opt-350m-finetuned-cola) on the imdb dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4133
- Accuracy: 0.92
- F1: 0.9205

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results



### Framework versions

- Transformers 4.22.1
- Pytorch 1.10.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1
