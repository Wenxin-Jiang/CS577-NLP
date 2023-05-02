---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- ag_news
metrics:
- accuracy
model-index:
- name: distilroberta-base-finetuned-topic-news
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: ag_news
      type: ag_news
      config: default
      split: train
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9431578947368421
widget:
- text: "Climate change has become an increasingly important concern among NATO countries"
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilroberta-base-finetuned-topic-news

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on the ag_news dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2729
- Accuracy: 0.9432

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.2661        | 1.0   | 15000 | 0.2656          | 0.9372   |
| 0.2032        | 2.0   | 30000 | 0.2439          | 0.9411   |
| 0.1516        | 3.0   | 45000 | 0.2682          | 0.9426   |
| 0.108         | 4.0   | 60000 | 0.2729          | 0.9432   |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.1
- Tokenizers 0.12.1
