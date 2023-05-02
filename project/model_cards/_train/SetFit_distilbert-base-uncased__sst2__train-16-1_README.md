---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-16-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-16-1

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6012
- Accuracy: 0.6766

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.6983        | 1.0   | 7    | 0.7036          | 0.2857   |
| 0.6836        | 2.0   | 14   | 0.7181          | 0.2857   |
| 0.645         | 3.0   | 21   | 0.7381          | 0.2857   |
| 0.5902        | 4.0   | 28   | 0.7746          | 0.2857   |
| 0.5799        | 5.0   | 35   | 0.7242          | 0.5714   |
| 0.3584        | 6.0   | 42   | 0.6935          | 0.5714   |
| 0.2596        | 7.0   | 49   | 0.7041          | 0.5714   |
| 0.1815        | 8.0   | 56   | 0.5930          | 0.7143   |
| 0.0827        | 9.0   | 63   | 0.6976          | 0.7143   |
| 0.0613        | 10.0  | 70   | 0.7346          | 0.7143   |
| 0.0356        | 11.0  | 77   | 0.6992          | 0.5714   |
| 0.0158        | 12.0  | 84   | 0.7328          | 0.5714   |
| 0.013         | 13.0  | 91   | 0.7819          | 0.5714   |
| 0.0103        | 14.0  | 98   | 0.8589          | 0.5714   |
| 0.0087        | 15.0  | 105  | 0.9177          | 0.5714   |
| 0.0076        | 16.0  | 112  | 0.9519          | 0.5714   |
| 0.0078        | 17.0  | 119  | 0.9556          | 0.5714   |
| 0.006         | 18.0  | 126  | 0.9542          | 0.5714   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
