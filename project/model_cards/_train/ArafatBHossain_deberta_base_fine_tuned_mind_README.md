---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta_base_fine_tuned_mind
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta_base_fine_tuned_mind

This model is a fine-tuned version of [microsoft/deberta-base](https://huggingface.co/microsoft/deberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3914
- Accuracy: 0.9085

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.7244        | 1.0   | 3054 | 0.5959          | 0.8013   |
| 0.5036        | 2.0   | 6108 | 0.3817          | 0.8805   |
| 0.3064        | 3.0   | 9162 | 0.3914          | 0.9085   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
