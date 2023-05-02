---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: bert-base-uncased-transformers-github-128
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-transformers-github-128

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2348

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 16

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.0247        | 1.0   | 582  | 1.6457          |
| 1.5989        | 2.0   | 1164 | 1.4157          |
| 1.4449        | 3.0   | 1746 | 1.3494          |
| 1.3579        | 4.0   | 2328 | 1.3774          |
| 1.3039        | 5.0   | 2910 | 1.1908          |
| 1.2428        | 6.0   | 3492 | 1.2780          |
| 1.19          | 7.0   | 4074 | 1.2569          |
| 1.1544        | 8.0   | 4656 | 1.1927          |
| 1.126         | 9.0   | 5238 | 1.1703          |
| 1.0893        | 10.0  | 5820 | 1.2100          |
| 1.0631        | 11.0  | 6402 | 1.1988          |
| 1.0417        | 12.0  | 6984 | 1.1643          |
| 1.0252        | 13.0  | 7566 | 1.2202          |
| 1.0101        | 14.0  | 8148 | 1.1678          |
| 0.9972        | 15.0  | 8730 | 1.0999          |
| 0.995         | 16.0  | 9312 | 1.2348          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
