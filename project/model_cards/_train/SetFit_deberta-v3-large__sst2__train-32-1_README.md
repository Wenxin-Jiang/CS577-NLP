---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-32-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-32-1

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4201
- Accuracy: 0.8759

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
| 0.7162        | 1.0   | 13   | 0.6832          | 0.5385   |
| 0.6561        | 2.0   | 26   | 0.7270          | 0.4615   |
| 0.4685        | 3.0   | 39   | 1.0674          | 0.5385   |
| 0.2837        | 4.0   | 52   | 1.0841          | 0.5385   |
| 0.1129        | 5.0   | 65   | 0.3502          | 0.9231   |
| 0.0118        | 6.0   | 78   | 0.4829          | 0.9231   |
| 0.0022        | 7.0   | 91   | 0.7430          | 0.8462   |
| 0.0007        | 8.0   | 104  | 0.8219          | 0.8462   |
| 0.0005        | 9.0   | 117  | 0.8787          | 0.8462   |
| 0.0003        | 10.0  | 130  | 0.8713          | 0.8462   |
| 0.0003        | 11.0  | 143  | 0.8473          | 0.8462   |
| 0.0002        | 12.0  | 156  | 0.8482          | 0.8462   |
| 0.0002        | 13.0  | 169  | 0.8494          | 0.8462   |
| 0.0002        | 14.0  | 182  | 0.8638          | 0.8462   |
| 0.0002        | 15.0  | 195  | 0.8492          | 0.8462   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
