---
license: mit
tags:
- generated_from_trainer
model-index:
- name: Romance-baseline
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Romance-baseline

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 6.5909

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 256
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 1000
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 0.94  | 15   | 10.7009         |
| No log        | 1.94  | 30   | 10.0799         |
| No log        | 2.94  | 45   | 9.6627          |
| No log        | 3.94  | 60   | 9.4619          |
| No log        | 4.94  | 75   | 9.2970          |
| No log        | 5.94  | 90   | 9.0919          |
| No log        | 6.94  | 105  | 8.9071          |
| No log        | 7.94  | 120  | 8.7240          |
| No log        | 8.94  | 135  | 8.5485          |
| No log        | 9.94  | 150  | 8.3952          |
| No log        | 10.94 | 165  | 8.2469          |
| No log        | 11.94 | 180  | 8.1193          |
| No log        | 12.94 | 195  | 7.9918          |
| No log        | 13.94 | 210  | 7.8662          |
| No log        | 14.94 | 225  | 7.7394          |
| No log        | 15.94 | 240  | 7.6219          |
| No log        | 16.94 | 255  | 7.5135          |
| No log        | 17.94 | 270  | 7.4110          |
| No log        | 18.94 | 285  | 7.3021          |
| No log        | 19.94 | 300  | 7.2021          |
| No log        | 20.94 | 315  | 7.1276          |
| No log        | 21.94 | 330  | 7.0278          |
| No log        | 22.94 | 345  | 6.9627          |
| No log        | 23.94 | 360  | 6.8806          |
| No log        | 24.94 | 375  | 6.8214          |
| No log        | 25.94 | 390  | 6.7725          |
| No log        | 26.94 | 405  | 6.7101          |
| No log        | 27.94 | 420  | 6.6792          |
| No log        | 28.94 | 435  | 6.6361          |
| No log        | 29.94 | 450  | 6.5950          |
| No log        | 30.94 | 465  | 6.5745          |
| No log        | 31.94 | 480  | 6.5469          |
| No log        | 32.94 | 495  | 6.5520          |
| No log        | 33.94 | 510  | 6.5121          |
| No log        | 34.94 | 525  | 6.5255          |
| No log        | 35.94 | 540  | 6.5179          |
| No log        | 36.94 | 555  | 6.5079          |
| No log        | 37.94 | 570  | 6.5138          |
| No log        | 38.94 | 585  | 6.5170          |
| No log        | 39.94 | 600  | 6.4807          |
| No log        | 40.94 | 615  | 6.5338          |
| No log        | 41.94 | 630  | 6.4960          |
| No log        | 42.94 | 645  | 6.5342          |
| No log        | 43.94 | 660  | 6.5119          |
| No log        | 44.94 | 675  | 6.5614          |
| No log        | 45.94 | 690  | 6.5235          |
| No log        | 46.94 | 705  | 6.5388          |
| No log        | 47.94 | 720  | 6.5574          |
| No log        | 48.94 | 735  | 6.5581          |
| No log        | 49.94 | 750  | 6.5909          |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
