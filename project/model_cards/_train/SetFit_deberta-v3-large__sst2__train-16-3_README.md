---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-16-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-16-3

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6286
- Accuracy: 0.7068

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
| 0.6955        | 1.0   | 7    | 0.7370          | 0.2857   |
| 0.6919        | 2.0   | 14   | 0.6855          | 0.4286   |
| 0.6347        | 3.0   | 21   | 0.5872          | 0.7143   |
| 0.4016        | 4.0   | 28   | 0.6644          | 0.7143   |
| 0.3097        | 5.0   | 35   | 0.5120          | 0.7143   |
| 0.0785        | 6.0   | 42   | 0.5845          | 0.7143   |
| 0.024         | 7.0   | 49   | 0.6951          | 0.7143   |
| 0.0132        | 8.0   | 56   | 0.8972          | 0.7143   |
| 0.0037        | 9.0   | 63   | 1.5798          | 0.7143   |
| 0.0034        | 10.0  | 70   | 1.5178          | 0.7143   |
| 0.003         | 11.0  | 77   | 1.3511          | 0.7143   |
| 0.0012        | 12.0  | 84   | 1.1346          | 0.7143   |
| 0.0007        | 13.0  | 91   | 0.9752          | 0.7143   |
| 0.0008        | 14.0  | 98   | 0.8531          | 0.7143   |
| 0.0007        | 15.0  | 105  | 0.8149          | 0.7143   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
