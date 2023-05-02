---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- emotion
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased-fine-tuned-emotions
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: emotion
      type: emotion
      args: split
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.9335
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-fine-tuned-emotions

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the emotion dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1377
- Accuracy: 0.9335
- F1 Score: 0.9338

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 128
- eval_batch_size: 128
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1 Score |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:--------:|
| 0.478         | 1.0   | 125  | 0.1852          | 0.931    | 0.9309   |
| 0.1285        | 2.0   | 250  | 0.1377          | 0.9335   | 0.9338   |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.8.1+cu101
- Datasets 2.7.1
- Tokenizers 0.10.1
