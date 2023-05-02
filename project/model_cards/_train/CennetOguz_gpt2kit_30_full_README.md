---
license: mit
tags:
- generated_from_trainer
model-index:
- name: gpt2kit_30_full
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2kit_30_full

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4313

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
- distributed_type: multi-GPU
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 10   | 3.1822          |
| No log        | 2.0   | 20   | 2.4642          |
| No log        | 3.0   | 30   | 2.1652          |
| No log        | 4.0   | 40   | 2.0160          |
| No log        | 5.0   | 50   | 1.9149          |
| No log        | 6.0   | 60   | 1.8388          |
| No log        | 7.0   | 70   | 1.7793          |
| No log        | 8.0   | 80   | 1.7282          |
| No log        | 9.0   | 90   | 1.6850          |
| No log        | 10.0  | 100  | 1.6501          |
| No log        | 11.0  | 110  | 1.6215          |
| No log        | 12.0  | 120  | 1.5943          |
| No log        | 13.0  | 130  | 1.5780          |
| No log        | 14.0  | 140  | 1.5573          |
| No log        | 15.0  | 150  | 1.5417          |
| No log        | 16.0  | 160  | 1.5227          |
| No log        | 17.0  | 170  | 1.5106          |
| No log        | 18.0  | 180  | 1.4948          |
| No log        | 19.0  | 190  | 1.4818          |
| No log        | 20.0  | 200  | 1.4692          |
| No log        | 21.0  | 210  | 1.4602          |
| No log        | 22.0  | 220  | 1.4516          |
| No log        | 23.0  | 230  | 1.4497          |
| No log        | 24.0  | 240  | 1.4488          |
| No log        | 25.0  | 250  | 1.4437          |
| No log        | 26.0  | 260  | 1.4385          |
| No log        | 27.0  | 270  | 1.4363          |
| No log        | 28.0  | 280  | 1.4338          |
| No log        | 29.0  | 290  | 1.4316          |
| No log        | 30.0  | 300  | 1.4313          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0
- Datasets 2.4.0
- Tokenizers 0.12.1
