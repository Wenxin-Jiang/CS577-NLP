---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: t5-small-vanilla-cstop_artificial
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-vanilla-cstop_artificial

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1506
- Exact Match: 0.5725

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 32
- total_train_batch_size: 512
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 3000

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Exact Match |
|:-------------:|:------:|:----:|:---------------:|:-----------:|
| 1.4041        | 28.5   | 200  | 0.1008          | 0.4758      |
| 0.047         | 57.13  | 400  | 0.1029          | 0.5367      |
| 0.021         | 85.63  | 600  | 0.1077          | 0.5617      |
| 0.012         | 114.25 | 800  | 0.1214          | 0.5689      |
| 0.0079        | 142.75 | 1000 | 0.1273          | 0.5671      |
| 0.0809        | 171.38 | 1200 | 0.1192          | 0.5653      |
| 0.0063        | 199.88 | 1400 | 0.1329          | 0.5653      |
| 0.0042        | 228.5  | 1600 | 0.1402          | 0.5707      |
| 0.0036        | 257.13 | 1800 | 0.1335          | 0.5617      |
| 0.0029        | 285.63 | 2000 | 0.1423          | 0.5689      |
| 0.0023        | 314.25 | 2200 | 0.1515          | 0.5671      |
| 0.0019        | 342.75 | 2400 | 0.1569          | 0.5689      |
| 0.0018        | 371.38 | 2600 | 0.1517          | 0.5689      |
| 0.0016        | 399.88 | 2800 | 0.1527          | 0.5725      |
| 0.0016        | 428.5  | 3000 | 0.1506          | 0.5725      |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.13.0+cu117
- Datasets 2.7.0
- Tokenizers 0.13.2
