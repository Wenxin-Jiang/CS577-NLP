---
license: cc-by-nc-sa-4.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: test-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# test-finetuned-ner

This model is a fine-tuned version of [hfl/chinese-pert-large](https://huggingface.co/hfl/chinese-pert-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1687
- Precision: 0.7449
- Recall: 0.7717
- F1: 0.7581
- Accuracy: 0.9546

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
- train_batch_size: 3
- eval_batch_size: 3
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1234        | 1.0   | 9387  | 0.1513          | 0.6954    | 0.7365 | 0.7153 | 0.9505   |
| 0.0841        | 2.0   | 18774 | 0.1462          | 0.7248    | 0.7630 | 0.7434 | 0.9533   |
| 0.0542        | 3.0   | 28161 | 0.1687          | 0.7449    | 0.7717 | 0.7581 | 0.9546   |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.8.0+cu111
- Datasets 2.4.0
- Tokenizers 0.10.3
