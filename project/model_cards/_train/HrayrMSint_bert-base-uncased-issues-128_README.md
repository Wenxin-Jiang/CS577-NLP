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
- Loss: 1.2432

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
| 2.0987        | 1.0   | 291  | 1.6066          |
| 1.631         | 2.0   | 582  | 1.4775          |
| 1.4933        | 3.0   | 873  | 1.4646          |
| 1.3984        | 4.0   | 1164 | 1.3314          |
| 1.3377        | 5.0   | 1455 | 1.3122          |
| 1.274         | 6.0   | 1746 | 1.2062          |
| 1.2538        | 7.0   | 2037 | 1.2626          |
| 1.192         | 8.0   | 2328 | 1.1832          |
| 1.1612        | 9.0   | 2619 | 1.2055          |
| 1.1489        | 10.0  | 2910 | 1.1605          |
| 1.1262        | 11.0  | 3201 | 1.1925          |
| 1.1022        | 12.0  | 3492 | 1.1309          |
| 1.0892        | 13.0  | 3783 | 1.1692          |
| 1.0812        | 14.0  | 4074 | 1.2384          |
| 1.0666        | 15.0  | 4365 | 1.0822          |
| 1.0533        | 16.0  | 4656 | 1.2432          |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.10.0
- Datasets 2.2.2
- Tokenizers 0.10.3
