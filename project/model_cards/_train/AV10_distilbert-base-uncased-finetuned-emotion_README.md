---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- emotion
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased-finetuned-emotion
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: emotion
      type: emotion
      config: split
      split: train
      args: split
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.936
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-emotion

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the emotion dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1529
- F1 Score: 0.9362
- Accuracy: 0.936

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1 Score | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| 0.5258        | 1.0   | 250  | 0.1909          | 0.9255   | 0.9265   |
| 0.145         | 2.0   | 500  | 0.1529          | 0.9362   | 0.936    |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
