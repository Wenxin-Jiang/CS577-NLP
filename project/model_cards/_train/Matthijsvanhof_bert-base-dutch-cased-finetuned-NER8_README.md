---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-base-dutch-cased-finetuned-NER8
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-dutch-cased-finetuned-NER8

This model is a fine-tuned version of [GroNLP/bert-base-dutch-cased](https://huggingface.co/GroNLP/bert-base-dutch-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1482
- Precision: 0.4716
- Recall: 0.4359
- F1: 0.4530
- Accuracy: 0.9569

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 68   | 0.1705          | 0.3582    | 0.3488 | 0.3535 | 0.9475   |
| No log        | 2.0   | 136  | 0.1482          | 0.4716    | 0.4359 | 0.4530 | 0.9569   |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.10.0+cu111
- Tokenizers 0.10.3
