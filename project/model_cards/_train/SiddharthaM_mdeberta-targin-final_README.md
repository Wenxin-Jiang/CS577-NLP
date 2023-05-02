---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: mdeberta-targin-final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mdeberta-targin-final

This model is a fine-tuned version of [distilbert-base-multilingual-cased](https://huggingface.co/distilbert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5637
- Accuracy: 0.7091
- Precision: 0.6841
- Recall: 0.6557
- F1: 0.6617

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 1.0   | 296  | 0.6001          | 0.6435   | 0.6344    | 0.5087 | 0.4156 |
| 0.6011        | 2.0   | 592  | 0.5633          | 0.7091   | 0.6879    | 0.6464 | 0.6521 |
| 0.6011        | 3.0   | 888  | 0.5501          | 0.7234   | 0.6991    | 0.6841 | 0.6892 |
| 0.5401        | 4.0   | 1184 | 0.5558          | 0.7082   | 0.6818    | 0.6595 | 0.6652 |
| 0.5401        | 5.0   | 1480 | 0.5637          | 0.7091   | 0.6841    | 0.6557 | 0.6617 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
