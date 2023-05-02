---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-8-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-8-3

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6421
- Accuracy: 0.6310

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
| 0.6696        | 1.0   | 3    | 0.7917          | 0.25     |
| 0.6436        | 2.0   | 6    | 0.8107          | 0.25     |
| 0.6923        | 3.0   | 9    | 0.8302          | 0.25     |
| 0.5051        | 4.0   | 12   | 0.9828          | 0.25     |
| 0.3688        | 5.0   | 15   | 0.7402          | 0.25     |
| 0.2671        | 6.0   | 18   | 0.5820          | 0.75     |
| 0.1935        | 7.0   | 21   | 0.8356          | 0.5      |
| 0.0815        | 8.0   | 24   | 1.0431          | 0.25     |
| 0.0591        | 9.0   | 27   | 0.9679          | 0.75     |
| 0.0276        | 10.0  | 30   | 1.0659          | 0.75     |
| 0.0175        | 11.0  | 33   | 0.9689          | 0.75     |
| 0.0152        | 12.0  | 36   | 0.8820          | 0.75     |
| 0.006         | 13.0  | 39   | 0.8337          | 0.75     |
| 0.0041        | 14.0  | 42   | 0.7650          | 0.75     |
| 0.0036        | 15.0  | 45   | 0.6960          | 0.75     |
| 0.0034        | 16.0  | 48   | 0.6548          | 0.75     |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
