---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: mdeberta-profane-final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mdeberta-profane-final

This model is a fine-tuned version of [microsoft/mdeberta-v3-base](https://huggingface.co/microsoft/mdeberta-v3-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2269
- Accuracy: 0.9154
- Precision: 0.8684
- Recall: 0.8558
- F1: 0.8618

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 1.0   | 296  | 0.2324          | 0.9125   | 0.8672    | 0.8446 | 0.8552 |
| 0.3129        | 2.0   | 592  | 0.2081          | 0.9202   | 0.8814    | 0.8549 | 0.8673 |
| 0.3129        | 3.0   | 888  | 0.2155          | 0.9183   | 0.8747    | 0.8575 | 0.8657 |
| 0.2136        | 4.0   | 1184 | 0.2164          | 0.9154   | 0.8738    | 0.8464 | 0.8591 |
| 0.2136        | 5.0   | 1480 | 0.2269          | 0.9154   | 0.8684    | 0.8558 | 0.8618 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
