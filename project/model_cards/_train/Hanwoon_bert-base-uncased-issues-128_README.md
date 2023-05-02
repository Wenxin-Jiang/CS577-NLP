---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: bert-base-uncased-issues-128
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-issues-128

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2449

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
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 16

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.099         | 1.0   | 291  | 1.6946          |
| 1.6396        | 2.0   | 582  | 1.4288          |
| 1.4875        | 3.0   | 873  | 1.3893          |
| 1.399         | 4.0   | 1164 | 1.3812          |
| 1.341         | 5.0   | 1455 | 1.2004          |
| 1.2803        | 6.0   | 1746 | 1.2738          |
| 1.2397        | 7.0   | 2037 | 1.2645          |
| 1.199         | 8.0   | 2328 | 1.2092          |
| 1.166         | 9.0   | 2619 | 1.1871          |
| 1.1406        | 10.0  | 2910 | 1.2244          |
| 1.1293        | 11.0  | 3201 | 1.2061          |
| 1.1037        | 12.0  | 3492 | 1.1621          |
| 1.0824        | 13.0  | 3783 | 1.2540          |
| 1.0738        | 14.0  | 4074 | 1.1703          |
| 1.0625        | 15.0  | 4365 | 1.1195          |
| 1.0628        | 16.0  | 4656 | 1.2449          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
