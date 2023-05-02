---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-base-timit-demo-google-colab
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-timit-demo-google-colab

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5253
- Wer: 0.3406

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 3.4884        | 1.0   | 500   | 1.6139          | 1.0293 |
| 0.8373        | 2.01  | 1000  | 0.5286          | 0.5266 |
| 0.4394        | 3.01  | 1500  | 0.4933          | 0.4678 |
| 0.2974        | 4.02  | 2000  | 0.4159          | 0.4268 |
| 0.2268        | 5.02  | 2500  | 0.4288          | 0.4074 |
| 0.1901        | 6.02  | 3000  | 0.4407          | 0.3852 |
| 0.1627        | 7.03  | 3500  | 0.4599          | 0.3849 |
| 0.1397        | 8.03  | 4000  | 0.4330          | 0.3803 |
| 0.1342        | 9.04  | 4500  | 0.4661          | 0.3785 |
| 0.1165        | 10.04 | 5000  | 0.4518          | 0.3745 |
| 0.1           | 11.04 | 5500  | 0.4714          | 0.3899 |
| 0.0881        | 12.05 | 6000  | 0.4985          | 0.3848 |
| 0.0794        | 13.05 | 6500  | 0.5074          | 0.3672 |
| 0.0707        | 14.06 | 7000  | 0.5692          | 0.3681 |
| 0.0669        | 15.06 | 7500  | 0.4722          | 0.3814 |
| 0.0589        | 16.06 | 8000  | 0.5738          | 0.3784 |
| 0.0562        | 17.07 | 8500  | 0.5183          | 0.3696 |
| 0.0578        | 18.07 | 9000  | 0.5473          | 0.3841 |
| 0.0473        | 19.08 | 9500  | 0.4918          | 0.3655 |
| 0.0411        | 20.08 | 10000 | 0.5258          | 0.3517 |
| 0.0419        | 21.08 | 10500 | 0.5256          | 0.3501 |
| 0.0348        | 22.09 | 11000 | 0.5511          | 0.3597 |
| 0.0328        | 23.09 | 11500 | 0.5054          | 0.3560 |
| 0.0314        | 24.1  | 12000 | 0.5327          | 0.3537 |
| 0.0296        | 25.1  | 12500 | 0.5142          | 0.3446 |
| 0.0251        | 26.1  | 13000 | 0.5155          | 0.3411 |
| 0.0249        | 27.11 | 13500 | 0.5344          | 0.3414 |
| 0.0225        | 28.11 | 14000 | 0.5193          | 0.3408 |
| 0.0226        | 29.12 | 14500 | 0.5253          | 0.3406 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.11.0+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1
