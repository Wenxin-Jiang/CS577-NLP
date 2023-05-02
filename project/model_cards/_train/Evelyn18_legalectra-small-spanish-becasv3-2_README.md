---
tags:
- generated_from_trainer
datasets:
- becasv2
model-index:
- name: legalectra-small-spanish-becasv3-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# legalectra-small-spanish-becasv3-2

This model is a fine-tuned version of [mrm8488/legalectra-small-spanish](https://huggingface.co/mrm8488/legalectra-small-spanish) on the becasv2 dataset.
It achieves the following results on the evaluation set:
- Loss: 4.7145

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
- num_epochs: 30

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 5    | 5.7994          |
| No log        | 2.0   | 10   | 5.6445          |
| No log        | 3.0   | 15   | 5.5595          |
| No log        | 4.0   | 20   | 5.4933          |
| No log        | 5.0   | 25   | 5.4248          |
| No log        | 6.0   | 30   | 5.3547          |
| No log        | 7.0   | 35   | 5.2872          |
| No log        | 8.0   | 40   | 5.2187          |
| No log        | 9.0   | 45   | 5.1585          |
| No log        | 10.0  | 50   | 5.1038          |
| No log        | 11.0  | 55   | 5.0451          |
| No log        | 12.0  | 60   | 5.0015          |
| No log        | 13.0  | 65   | 4.9638          |
| No log        | 14.0  | 70   | 4.9350          |
| No log        | 15.0  | 75   | 4.9034          |
| No log        | 16.0  | 80   | 4.8741          |
| No log        | 17.0  | 85   | 4.8496          |
| No log        | 18.0  | 90   | 4.8275          |
| No log        | 19.0  | 95   | 4.8139          |
| No log        | 20.0  | 100  | 4.7878          |
| No log        | 21.0  | 105  | 4.7672          |
| No log        | 22.0  | 110  | 4.7671          |
| No log        | 23.0  | 115  | 4.7611          |
| No log        | 24.0  | 120  | 4.7412          |
| No log        | 25.0  | 125  | 4.7307          |
| No log        | 26.0  | 130  | 4.7232          |
| No log        | 27.0  | 135  | 4.7208          |
| No log        | 28.0  | 140  | 4.7186          |
| No log        | 29.0  | 145  | 4.7158          |
| No log        | 30.0  | 150  | 4.7145          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
