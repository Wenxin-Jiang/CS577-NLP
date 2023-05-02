---
tags:
- generated_from_trainer
datasets:
- imdb
metrics:
- accuracy
model-index:
- name: distilbert_for_text_classification
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
      value: 0.93232
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert_for_text_classification

This model is a fine-tuned version of [RavenK/distilbert](https://huggingface.co/RavenK/distilbert) on the imdb dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2352
- Accuracy: 0.9323

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

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.2327        | 1.0   | 1563 | 0.1868          | 0.9279   |
| 0.1472        | 2.0   | 3126 | 0.2352          | 0.9323   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
