---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: poem-gen-t5-small
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# poem-gen-t5-small

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.1066

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 3.67          | 0.32  | 5000  | 3.4705          |
| 3.573         | 0.63  | 10000 | 3.3747          |
| 3.5075        | 0.95  | 15000 | 3.3154          |
| 3.4486        | 1.26  | 20000 | 3.2704          |
| 3.4207        | 1.58  | 25000 | 3.2351          |
| 3.3933        | 1.89  | 30000 | 3.2069          |
| 3.3612        | 2.21  | 35000 | 3.1853          |
| 3.34          | 2.53  | 40000 | 3.1659          |
| 3.3422        | 2.84  | 45000 | 3.1503          |
| 3.3034        | 3.16  | 50000 | 3.1376          |
| 3.2886        | 3.47  | 55000 | 3.1283          |
| 3.2806        | 3.79  | 60000 | 3.1208          |
| 3.2745        | 4.1   | 65000 | 3.1141          |
| 3.2894        | 4.42  | 70000 | 3.1093          |
| 3.264         | 4.74  | 75000 | 3.1075          |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 1.18.4
- Tokenizers 0.11.6
