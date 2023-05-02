---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-8-0
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-8-0

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7088
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
| 0.6705        | 1.0   | 3    | 0.7961          | 0.25     |
| 0.6571        | 2.0   | 6    | 0.8092          | 0.25     |
| 0.7043        | 3.0   | 9    | 0.7977          | 0.25     |
| 0.6207        | 4.0   | 12   | 0.8478          | 0.25     |
| 0.5181        | 5.0   | 15   | 0.9782          | 0.25     |
| 0.4136        | 6.0   | 18   | 1.3151          | 0.25     |
| 0.3702        | 7.0   | 21   | 1.8633          | 0.25     |
| 0.338         | 8.0   | 24   | 2.2119          | 0.25     |
| 0.2812        | 9.0   | 27   | 2.3058          | 0.25     |
| 0.2563        | 10.0  | 30   | 2.3353          | 0.25     |
| 0.2132        | 11.0  | 33   | 2.5921          | 0.25     |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
