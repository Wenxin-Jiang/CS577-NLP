---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: BERT_Mod_3
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: glue
      type: glue
      args: mnli
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.8198675496688742
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# BERT_Mod_3

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the glue dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6760
- Accuracy: 0.8199

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
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.5167        | 1.0   | 24544 | 0.4953          | 0.8077   |
| 0.414         | 2.0   | 49088 | 0.4802          | 0.8148   |
| 0.2933        | 3.0   | 73632 | 0.5783          | 0.8186   |
| 0.2236        | 4.0   | 98176 | 0.6760          | 0.8199   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0
- Datasets 2.4.0
- Tokenizers 0.12.1
