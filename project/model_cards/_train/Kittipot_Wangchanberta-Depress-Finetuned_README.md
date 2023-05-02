---
tags:
- generated_from_trainer
datasets:
- wisesight_sentiment
model-index:
- name: Wangchanberta-Depress-Finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Wangchanberta-Depress-Finetuned

This model is a fine-tuned version of [airesearch/wangchanberta-base-att-spm-uncased](https://huggingface.co/airesearch/wangchanberta-base-att-spm-uncased) on the wisesight_sentiment dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5910

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 400
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 1.0114        | 0.08  | 200   | 0.9538          |
| 0.8617        | 0.15  | 400   | 0.8280          |
| 0.7882        | 0.23  | 600   | 0.7472          |
| 0.7132        | 0.3   | 800   | 0.7264          |
| 0.7226        | 0.38  | 1000  | 0.7265          |
| 0.6854        | 0.45  | 1200  | 0.6792          |
| 0.621         | 0.53  | 1400  | 0.6451          |
| 0.6093        | 0.61  | 1600  | 0.6364          |
| 0.6099        | 0.68  | 1800  | 0.6128          |
| 0.5766        | 0.76  | 2000  | 0.6388          |
| 0.6033        | 0.83  | 2200  | 0.6148          |
| 0.5966        | 0.91  | 2400  | 0.6440          |
| 0.6208        | 0.98  | 2600  | 0.5910          |
| 0.5178        | 1.06  | 2800  | 0.6340          |
| 0.4863        | 1.13  | 3000  | 0.7177          |
| 0.4852        | 1.21  | 3200  | 0.6766          |
| 0.4711        | 1.29  | 3400  | 0.6739          |
| 0.5203        | 1.36  | 3600  | 0.6429          |
| 0.5167        | 1.44  | 3800  | 0.6539          |
| 0.5053        | 1.51  | 4000  | 0.6172          |
| 0.5076        | 1.59  | 4200  | 0.6053          |
| 0.4704        | 1.66  | 4400  | 0.6474          |
| 0.4807        | 1.74  | 4600  | 0.6225          |
| 0.4792        | 1.82  | 4800  | 0.6282          |
| 0.5177        | 1.89  | 5000  | 0.6011          |
| 0.4839        | 1.97  | 5200  | 0.6231          |
| 0.4155        | 2.04  | 5400  | 0.6668          |
| 0.3923        | 2.12  | 5600  | 0.6886          |
| 0.3713        | 2.19  | 5800  | 0.6895          |
| 0.364         | 2.27  | 6000  | 0.6886          |
| 0.3774        | 2.34  | 6200  | 0.7117          |
| 0.4001        | 2.42  | 6400  | 0.7081          |
| 0.3531        | 2.5   | 6600  | 0.7465          |
| 0.3768        | 2.57  | 6800  | 0.7706          |
| 0.3324        | 2.65  | 7000  | 0.7456          |
| 0.3597        | 2.72  | 7200  | 0.7507          |
| 0.3868        | 2.8   | 7400  | 0.7542          |
| 0.4141        | 2.87  | 7600  | 0.7223          |
| 0.3701        | 2.95  | 7800  | 0.7374          |
| 0.3175        | 3.03  | 8000  | 0.7615          |
| 0.2951        | 3.1   | 8200  | 0.7880          |
| 0.2885        | 3.18  | 8400  | 0.8158          |
| 0.2913        | 3.25  | 8600  | 0.8565          |
| 0.2815        | 3.33  | 8800  | 0.8649          |
| 0.2748        | 3.4   | 9000  | 0.8783          |
| 0.2776        | 3.48  | 9200  | 0.8851          |
| 0.2982        | 3.56  | 9400  | 0.8922          |
| 0.2939        | 3.63  | 9600  | 0.8796          |
| 0.2712        | 3.71  | 9800  | 0.8873          |
| 0.2918        | 3.78  | 10000 | 0.8973          |
| 0.3144        | 3.86  | 10200 | 0.8978          |
| 0.2988        | 3.93  | 10400 | 0.8951          |


### Framework versions

- Transformers 4.11.2
- Pytorch 1.11.0+cu113
- Datasets 2.1.0
- Tokenizers 0.10.3
