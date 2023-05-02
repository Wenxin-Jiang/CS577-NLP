---
tags:
- generated_from_trainer
datasets:
- becasv2
model-index:
- name: legalectra-small-spanish-becasv3-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# legalectra-small-spanish-becasv3-5

This model is a fine-tuned version of [mrm8488/legalectra-small-spanish](https://huggingface.co/mrm8488/legalectra-small-spanish) on the becasv2 dataset.
It achieves the following results on the evaluation set:
- Loss: 4.7020

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
- num_epochs: 50

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 5    | 5.7715          |
| No log        | 2.0   | 10   | 5.7001          |
| No log        | 3.0   | 15   | 5.6206          |
| No log        | 4.0   | 20   | 5.5463          |
| No log        | 5.0   | 25   | 5.4866          |
| No log        | 6.0   | 30   | 5.4369          |
| No log        | 7.0   | 35   | 5.3939          |
| No log        | 8.0   | 40   | 5.3545          |
| No log        | 9.0   | 45   | 5.3168          |
| No log        | 10.0  | 50   | 5.2824          |
| No log        | 11.0  | 55   | 5.2504          |
| No log        | 12.0  | 60   | 5.2193          |
| No log        | 13.0  | 65   | 5.1864          |
| No log        | 14.0  | 70   | 5.1515          |
| No log        | 15.0  | 75   | 5.1174          |
| No log        | 16.0  | 80   | 5.0839          |
| No log        | 17.0  | 85   | 5.0497          |
| No log        | 18.0  | 90   | 5.0188          |
| No log        | 19.0  | 95   | 4.9937          |
| No log        | 20.0  | 100  | 4.9726          |
| No log        | 21.0  | 105  | 4.9483          |
| No log        | 22.0  | 110  | 4.9205          |
| No log        | 23.0  | 115  | 4.8993          |
| No log        | 24.0  | 120  | 4.8802          |
| No log        | 25.0  | 125  | 4.8612          |
| No log        | 26.0  | 130  | 4.8498          |
| No log        | 27.0  | 135  | 4.8294          |
| No log        | 28.0  | 140  | 4.8176          |
| No log        | 29.0  | 145  | 4.8144          |
| No log        | 30.0  | 150  | 4.8012          |
| No log        | 31.0  | 155  | 4.7890          |
| No log        | 32.0  | 160  | 4.7745          |
| No log        | 33.0  | 165  | 4.7641          |
| No log        | 34.0  | 170  | 4.7558          |
| No log        | 35.0  | 175  | 4.7474          |
| No log        | 36.0  | 180  | 4.7384          |
| No log        | 37.0  | 185  | 4.7319          |
| No log        | 38.0  | 190  | 4.7262          |
| No log        | 39.0  | 195  | 4.7225          |
| No log        | 40.0  | 200  | 4.7201          |
| No log        | 41.0  | 205  | 4.7165          |
| No log        | 42.0  | 210  | 4.7129          |
| No log        | 43.0  | 215  | 4.7111          |
| No log        | 44.0  | 220  | 4.7086          |
| No log        | 45.0  | 225  | 4.7060          |
| No log        | 46.0  | 230  | 4.7049          |
| No log        | 47.0  | 235  | 4.7036          |
| No log        | 48.0  | 240  | 4.7028          |
| No log        | 49.0  | 245  | 4.7023          |
| No log        | 50.0  | 250  | 4.7020          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
