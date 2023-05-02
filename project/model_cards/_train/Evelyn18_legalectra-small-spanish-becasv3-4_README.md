---
tags:
- generated_from_trainer
datasets:
- becasv2
model-index:
- name: legalectra-small-spanish-becasv3-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# legalectra-small-spanish-becasv3-4

This model is a fine-tuned version of [mrm8488/legalectra-small-spanish](https://huggingface.co/mrm8488/legalectra-small-spanish) on the becasv2 dataset.
It achieves the following results on the evaluation set:
- Loss: 4.1290

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
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 5    | 5.6625          |
| No log        | 2.0   | 10   | 5.4940          |
| No log        | 3.0   | 15   | 5.3886          |
| No log        | 4.0   | 20   | 5.3004          |
| No log        | 5.0   | 25   | 5.2210          |
| No log        | 6.0   | 30   | 5.1434          |
| No log        | 7.0   | 35   | 5.0546          |
| No log        | 8.0   | 40   | 4.9726          |
| No log        | 9.0   | 45   | 4.9227          |
| No log        | 10.0  | 50   | 4.8344          |
| No log        | 11.0  | 55   | 4.7749          |
| No log        | 12.0  | 60   | 4.7381          |
| No log        | 13.0  | 65   | 4.7016          |
| No log        | 14.0  | 70   | 4.6581          |
| No log        | 15.0  | 75   | 4.6231          |
| No log        | 16.0  | 80   | 4.5900          |
| No log        | 17.0  | 85   | 4.5446          |
| No log        | 18.0  | 90   | 4.5041          |
| No log        | 19.0  | 95   | 4.4635          |
| No log        | 20.0  | 100  | 4.4356          |
| No log        | 21.0  | 105  | 4.3985          |
| No log        | 22.0  | 110  | 4.3650          |
| No log        | 23.0  | 115  | 4.3540          |
| No log        | 24.0  | 120  | 4.3270          |
| No log        | 25.0  | 125  | 4.2873          |
| No log        | 26.0  | 130  | 4.2808          |
| No log        | 27.0  | 135  | 4.2623          |
| No log        | 28.0  | 140  | 4.2466          |
| No log        | 29.0  | 145  | 4.2488          |
| No log        | 30.0  | 150  | 4.2410          |
| No log        | 31.0  | 155  | 4.2187          |
| No log        | 32.0  | 160  | 4.2000          |
| No log        | 33.0  | 165  | 4.1883          |
| No log        | 34.0  | 170  | 4.1803          |
| No log        | 35.0  | 175  | 4.1773          |
| No log        | 36.0  | 180  | 4.1652          |
| No log        | 37.0  | 185  | 4.1614          |
| No log        | 38.0  | 190  | 4.1609          |
| No log        | 39.0  | 195  | 4.1652          |
| No log        | 40.0  | 200  | 4.1560          |
| No log        | 41.0  | 205  | 4.1435          |
| No log        | 42.0  | 210  | 4.1463          |
| No log        | 43.0  | 215  | 4.1434          |
| No log        | 44.0  | 220  | 4.1340          |
| No log        | 45.0  | 225  | 4.1259          |
| No log        | 46.0  | 230  | 4.1212          |
| No log        | 47.0  | 235  | 4.1224          |
| No log        | 48.0  | 240  | 4.1257          |
| No log        | 49.0  | 245  | 4.1284          |
| No log        | 50.0  | 250  | 4.1290          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
