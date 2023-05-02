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
- Loss: 1.2456

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
| 2.0986        | 1.0   | 291  | 1.6929          |
| 1.6401        | 2.0   | 582  | 1.4304          |
| 1.4881        | 3.0   | 873  | 1.3916          |
| 1.4           | 4.0   | 1164 | 1.3796          |
| 1.3416        | 5.0   | 1455 | 1.2012          |
| 1.2807        | 6.0   | 1746 | 1.2733          |
| 1.2396        | 7.0   | 2037 | 1.2646          |
| 1.1993        | 8.0   | 2328 | 1.2098          |
| 1.1661        | 9.0   | 2619 | 1.1862          |
| 1.1406        | 10.0  | 2910 | 1.2223          |
| 1.1294        | 11.0  | 3201 | 1.2056          |
| 1.1042        | 12.0  | 3492 | 1.1655          |
| 1.0827        | 13.0  | 3783 | 1.2525          |
| 1.0738        | 14.0  | 4074 | 1.1685          |
| 1.0626        | 15.0  | 4365 | 1.1182          |
| 1.0629        | 16.0  | 4656 | 1.2456          |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.13.0+cu116
- Datasets 1.16.1
- Tokenizers 0.10.3
