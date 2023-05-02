---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-16-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-16-2

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6959
- Accuracy: 0.5008

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
| 0.7079        | 1.0   | 7    | 0.7361          | 0.2857   |
| 0.6815        | 2.0   | 14   | 0.7659          | 0.2857   |
| 0.6938        | 3.0   | 21   | 0.7944          | 0.2857   |
| 0.4584        | 4.0   | 28   | 1.2441          | 0.2857   |
| 0.4949        | 5.0   | 35   | 1.2285          | 0.5714   |
| 0.0574        | 6.0   | 42   | 1.7796          | 0.5714   |
| 0.0156        | 7.0   | 49   | 2.6027          | 0.5714   |
| 0.0051        | 8.0   | 56   | 2.8717          | 0.5714   |
| 0.0017        | 9.0   | 63   | 2.8491          | 0.5714   |
| 0.0023        | 10.0  | 70   | 1.7149          | 0.7143   |
| 0.001         | 11.0  | 77   | 1.1101          | 0.7143   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
