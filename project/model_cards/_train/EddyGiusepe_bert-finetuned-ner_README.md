---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0602
- Precision: 0.9335
- Recall: 0.9517
- F1: 0.9425
- Accuracy: 0.9864

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0852        | 1.0   | 1756 | 0.0685          | 0.9208    | 0.9367 | 0.9287 | 0.9829   |
| 0.0336        | 2.0   | 3512 | 0.0612          | 0.9281    | 0.9495 | 0.9387 | 0.9856   |
| 0.0181        | 3.0   | 5268 | 0.0602          | 0.9335    | 0.9517 | 0.9425 | 0.9864   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Tokenizers 0.13.1
