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
- name: hasoc19-microsoft-mdeberta-v3-base-targinsult1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hasoc19-microsoft-mdeberta-v3-base-targinsult1

This model is a fine-tuned version of [microsoft/mdeberta-v3-base](https://huggingface.co/microsoft/mdeberta-v3-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9030
- Accuracy: 0.6958
- Precision: 0.6536
- Recall: 0.6464
- F1: 0.6493

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
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| No log        | 1.0   | 263  | 0.5647          | 0.6858   | 0.6528    | 0.6609 | 0.6556 |
| 0.5745        | 2.0   | 526  | 0.5520          | 0.6987   | 0.6612    | 0.6626 | 0.6619 |
| 0.5745        | 3.0   | 789  | 0.6162          | 0.7139   | 0.6764    | 0.6733 | 0.6747 |
| 0.4908        | 4.0   | 1052 | 0.6262          | 0.7063   | 0.6698    | 0.6715 | 0.6706 |
| 0.4908        | 5.0   | 1315 | 0.6799          | 0.7067   | 0.6661    | 0.6568 | 0.6604 |
| 0.4069        | 6.0   | 1578 | 0.7646          | 0.7044   | 0.6635    | 0.6550 | 0.6584 |
| 0.4069        | 7.0   | 1841 | 0.7791          | 0.7029   | 0.6646    | 0.6633 | 0.6639 |
| 0.338         | 8.0   | 2104 | 0.8646          | 0.7029   | 0.6623    | 0.6554 | 0.6582 |
| 0.338         | 9.0   | 2367 | 0.9417          | 0.7006   | 0.6556    | 0.6317 | 0.6374 |
| 0.2847        | 10.0  | 2630 | 0.9030          | 0.6958   | 0.6536    | 0.6464 | 0.6493 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
