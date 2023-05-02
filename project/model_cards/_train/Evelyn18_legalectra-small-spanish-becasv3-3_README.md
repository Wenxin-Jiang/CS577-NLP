---
tags:
- generated_from_trainer
datasets:
- becasv2
model-index:
- name: legalectra-small-spanish-becasv3-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# legalectra-small-spanish-becasv3-3

This model is a fine-tuned version of [mrm8488/legalectra-small-spanish](https://huggingface.co/mrm8488/legalectra-small-spanish) on the becasv2 dataset.
It achieves the following results on the evaluation set:
- Loss: 4.4873

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 5    | 5.7608          |
| No log        | 2.0   | 10   | 5.5991          |
| No log        | 3.0   | 15   | 5.5162          |
| No log        | 4.0   | 20   | 5.4370          |
| No log        | 5.0   | 25   | 5.3521          |
| No log        | 6.0   | 30   | 5.2657          |
| No log        | 7.0   | 35   | 5.1771          |
| No log        | 8.0   | 40   | 5.1024          |
| No log        | 9.0   | 45   | 5.0248          |
| No log        | 10.0  | 50   | 4.9609          |
| No log        | 11.0  | 55   | 4.9167          |
| No log        | 12.0  | 60   | 4.8487          |
| No log        | 13.0  | 65   | 4.8175          |
| No log        | 14.0  | 70   | 4.7646          |
| No log        | 15.0  | 75   | 4.7276          |
| No log        | 16.0  | 80   | 4.7003          |
| No log        | 17.0  | 85   | 4.6518          |
| No log        | 18.0  | 90   | 4.6240          |
| No log        | 19.0  | 95   | 4.6033          |
| No log        | 20.0  | 100  | 4.5601          |
| No log        | 21.0  | 105  | 4.5433          |
| No log        | 22.0  | 110  | 4.5279          |
| No log        | 23.0  | 115  | 4.4981          |
| No log        | 24.0  | 120  | 4.4831          |
| No log        | 25.0  | 125  | 4.4745          |
| No log        | 26.0  | 130  | 4.4607          |
| No log        | 27.0  | 135  | 4.4528          |
| No log        | 28.0  | 140  | 4.4348          |
| No log        | 29.0  | 145  | 4.4418          |
| No log        | 30.0  | 150  | 4.4380          |
| No log        | 31.0  | 155  | 4.4205          |
| No log        | 32.0  | 160  | 4.4373          |
| No log        | 33.0  | 165  | 4.4302          |
| No log        | 34.0  | 170  | 4.4468          |
| No log        | 35.0  | 175  | 4.4512          |
| No log        | 36.0  | 180  | 4.4225          |
| No log        | 37.0  | 185  | 4.4303          |
| No log        | 38.0  | 190  | 4.4562          |
| No log        | 39.0  | 195  | 4.4671          |
| No log        | 40.0  | 200  | 4.4869          |
| No log        | 41.0  | 205  | 4.5046          |
| No log        | 42.0  | 210  | 4.4990          |
| No log        | 43.0  | 215  | 4.4847          |
| No log        | 44.0  | 220  | 4.4770          |
| No log        | 45.0  | 225  | 4.4786          |
| No log        | 46.0  | 230  | 4.4741          |
| No log        | 47.0  | 235  | 4.4797          |
| No log        | 48.0  | 240  | 4.4830          |
| No log        | 49.0  | 245  | 4.4845          |
| No log        | 50.0  | 250  | 4.4873          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
