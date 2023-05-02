---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased__sst2__train-16-0
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased__sst2__train-16-0

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6903
- Accuracy: 0.5091

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
| 0.6934        | 1.0   | 7    | 0.7142          | 0.2857   |
| 0.6703        | 2.0   | 14   | 0.7379          | 0.2857   |
| 0.6282        | 3.0   | 21   | 0.7769          | 0.2857   |
| 0.5193        | 4.0   | 28   | 0.8799          | 0.2857   |
| 0.5104        | 5.0   | 35   | 0.8380          | 0.4286   |
| 0.2504        | 6.0   | 42   | 0.8622          | 0.4286   |
| 0.1794        | 7.0   | 49   | 0.9227          | 0.4286   |
| 0.1156        | 8.0   | 56   | 0.8479          | 0.4286   |
| 0.0709        | 9.0   | 63   | 1.0929          | 0.2857   |
| 0.0471        | 10.0  | 70   | 1.2189          | 0.2857   |
| 0.0288        | 11.0  | 77   | 1.2026          | 0.4286   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
