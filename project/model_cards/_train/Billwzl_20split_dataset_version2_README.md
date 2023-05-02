---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: 20split_dataset_version2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 20split_dataset_version2

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0626

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 16

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 2.7621        | 1.0   | 11851  | 2.5216          |
| 2.5466        | 2.0   | 23702  | 2.4157          |
| 2.4505        | 3.0   | 35553  | 2.3592          |
| 2.3798        | 4.0   | 47404  | 2.3028          |
| 2.3178        | 5.0   | 59255  | 2.2768          |
| 2.272         | 6.0   | 71106  | 2.2366          |
| 2.2323        | 7.0   | 82957  | 2.2128          |
| 2.1928        | 8.0   | 94808  | 2.1797          |
| 2.157         | 9.0   | 106659 | 2.1667          |
| 2.1292        | 10.0  | 118510 | 2.1392          |
| 2.0978        | 11.0  | 130361 | 2.1280          |
| 2.0725        | 12.0  | 142212 | 2.1106          |
| 2.052         | 13.0  | 154063 | 2.0944          |
| 2.0268        | 14.0  | 165914 | 2.0804          |
| 2.0121        | 15.0  | 177765 | 2.0698          |
| 1.9997        | 16.0  | 189616 | 2.0626          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
