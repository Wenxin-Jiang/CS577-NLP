---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: scibert-cased-AstrID-tok
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# scibert-cased-AstrID-tok

This model is a fine-tuned version of [allenai/scibert_scivocab_cased](https://huggingface.co/allenai/scibert_scivocab_cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1843
- Precision: 0.7307
- Recall: 0.7575
- F1: 0.7439
- Accuracy: 0.9517

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
| No log        | 1.0   | 220  | 0.3141          | 0.6254    | 0.6518 | 0.6383 | 0.9182   |
| No log        | 2.0   | 440  | 0.1988          | 0.7002    | 0.7275 | 0.7136 | 0.9480   |
| 0.3514        | 3.0   | 660  | 0.1843          | 0.7307    | 0.7575 | 0.7439 | 0.9517   |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
