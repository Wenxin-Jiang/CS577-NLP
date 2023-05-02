---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-16-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-16-1

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6804
- Accuracy: 0.5497

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
| 0.7086        | 1.0   | 7    | 0.7176          | 0.2857   |
| 0.6897        | 2.0   | 14   | 0.7057          | 0.2857   |
| 0.6491        | 3.0   | 21   | 0.6582          | 0.8571   |
| 0.567         | 4.0   | 28   | 0.4480          | 0.8571   |
| 0.4304        | 5.0   | 35   | 0.5465          | 0.7143   |
| 0.0684        | 6.0   | 42   | 0.5408          | 0.8571   |
| 0.0339        | 7.0   | 49   | 0.6501          | 0.8571   |
| 0.0082        | 8.0   | 56   | 0.9152          | 0.8571   |
| 0.0067        | 9.0   | 63   | 2.5162          | 0.5714   |
| 0.0045        | 10.0  | 70   | 1.1136          | 0.8571   |
| 0.0012        | 11.0  | 77   | 1.1668          | 0.8571   |
| 0.0007        | 12.0  | 84   | 1.2071          | 0.8571   |
| 0.0005        | 13.0  | 91   | 1.2310          | 0.8571   |
| 0.0006        | 14.0  | 98   | 1.2476          | 0.8571   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
