---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-16-6
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-16-6

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6846
- Accuracy: 0.5058

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
| 0.6673        | 1.0   | 7    | 0.7580          | 0.2857   |
| 0.5896        | 2.0   | 14   | 0.7885          | 0.5714   |
| 0.5294        | 3.0   | 21   | 1.0040          | 0.4286   |
| 0.3163        | 4.0   | 28   | 1.1761          | 0.5714   |
| 0.1315        | 5.0   | 35   | 1.4315          | 0.4286   |
| 0.0312        | 6.0   | 42   | 2.6115          | 0.2857   |
| 0.1774        | 7.0   | 49   | 2.1631          | 0.5714   |
| 0.0052        | 8.0   | 56   | 2.3838          | 0.4286   |
| 0.0043        | 9.0   | 63   | 2.6553          | 0.4286   |
| 0.0032        | 10.0  | 70   | 2.2774          | 0.4286   |
| 0.0015        | 11.0  | 77   | 1.9467          | 0.7143   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
