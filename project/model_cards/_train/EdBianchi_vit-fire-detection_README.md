---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
model-index:
- name: vit-fire-detection
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# vit-fire-detection

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0126
- Precision: 0.9960
- Recall: 0.9960

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|
| 0.1018        | 1.0   | 190  | 0.0375          | 0.9934    | 0.9934 |
| 0.0484        | 2.0   | 380  | 0.0167          | 0.9961    | 0.9960 |
| 0.0357        | 3.0   | 570  | 0.0253          | 0.9948    | 0.9947 |
| 0.0133        | 4.0   | 760  | 0.0198          | 0.9961    | 0.9960 |
| 0.012         | 5.0   | 950  | 0.0203          | 0.9947    | 0.9947 |
| 0.0139        | 6.0   | 1140 | 0.0204          | 0.9947    | 0.9947 |
| 0.0076        | 7.0   | 1330 | 0.0175          | 0.9961    | 0.9960 |
| 0.0098        | 8.0   | 1520 | 0.0115          | 0.9974    | 0.9974 |
| 0.0062        | 9.0   | 1710 | 0.0133          | 0.9960    | 0.9960 |
| 0.0012        | 10.0  | 1900 | 0.0126          | 0.9960    | 0.9960 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.14.0.dev20221111
- Datasets 2.8.0
- Tokenizers 0.12.1
