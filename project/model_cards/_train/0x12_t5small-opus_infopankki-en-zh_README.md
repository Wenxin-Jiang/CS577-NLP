---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- opus_infopankki
model-index:
- name: t5small-opus_infopankki-en-zh
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5small-opus_infopankki-en-zh

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the opus_infopankki dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0385

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 25
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 3.0853        | 1.0   | 1496  | 2.7074          |
| 2.8378        | 2.0   | 2992  | 2.5717          |
| 2.7637        | 3.0   | 4488  | 2.4829          |
| 2.6622        | 4.0   | 5984  | 2.4156          |
| 2.5986        | 5.0   | 7480  | 2.3649          |
| 2.5488        | 6.0   | 8976  | 2.3184          |
| 2.486         | 7.0   | 10472 | 2.2808          |
| 2.4566        | 8.0   | 11968 | 2.2485          |
| 2.4413        | 9.0   | 13464 | 2.2181          |
| 2.3806        | 10.0  | 14960 | 2.1939          |
| 2.3741        | 11.0  | 16456 | 2.1711          |
| 2.3419        | 12.0  | 17952 | 2.1511          |
| 2.3197        | 13.0  | 19448 | 2.1318          |
| 2.3229        | 14.0  | 20944 | 2.1170          |
| 2.2885        | 15.0  | 22440 | 2.1032          |
| 2.2781        | 16.0  | 23936 | 2.0908          |
| 2.2447        | 17.0  | 25432 | 2.0792          |
| 2.2589        | 18.0  | 26928 | 2.0695          |
| 2.2274        | 19.0  | 28424 | 2.0611          |
| 2.2311        | 20.0  | 29920 | 2.0538          |
| 2.2263        | 21.0  | 31416 | 2.0482          |
| 2.2066        | 22.0  | 32912 | 2.0443          |
| 2.2042        | 23.0  | 34408 | 2.0413          |
| 2.211         | 24.0  | 35904 | 2.0390          |
| 2.1952        | 25.0  | 37400 | 2.0385          |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.12.1
