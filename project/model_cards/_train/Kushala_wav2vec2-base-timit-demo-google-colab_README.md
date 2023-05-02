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
- Loss: 0.5195
- Wer: 0.3386

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
| 3.5345        | 1.0   | 500   | 2.1466          | 1.0010 |
| 0.949         | 2.01  | 1000  | 0.5687          | 0.5492 |
| 0.445         | 3.01  | 1500  | 0.4562          | 0.4717 |
| 0.2998        | 4.02  | 2000  | 0.4154          | 0.4401 |
| 0.2242        | 5.02  | 2500  | 0.3887          | 0.4034 |
| 0.1834        | 6.02  | 3000  | 0.4262          | 0.3905 |
| 0.1573        | 7.03  | 3500  | 0.4200          | 0.3927 |
| 0.1431        | 8.03  | 4000  | 0.4194          | 0.3869 |
| 0.1205        | 9.04  | 4500  | 0.4600          | 0.3912 |
| 0.1082        | 10.04 | 5000  | 0.4613          | 0.3776 |
| 0.0984        | 11.04 | 5500  | 0.4926          | 0.3860 |
| 0.0872        | 12.05 | 6000  | 0.4869          | 0.3780 |
| 0.0826        | 13.05 | 6500  | 0.5033          | 0.3690 |
| 0.0717        | 14.06 | 7000  | 0.4827          | 0.3791 |
| 0.0658        | 15.06 | 7500  | 0.4816          | 0.3650 |
| 0.0579        | 16.06 | 8000  | 0.5433          | 0.3689 |
| 0.056         | 17.07 | 8500  | 0.5513          | 0.3672 |
| 0.0579        | 18.07 | 9000  | 0.4813          | 0.3632 |
| 0.0461        | 19.08 | 9500  | 0.4846          | 0.3501 |
| 0.0431        | 20.08 | 10000 | 0.5449          | 0.3637 |
| 0.043         | 21.08 | 10500 | 0.4906          | 0.3538 |
| 0.0334        | 22.09 | 11000 | 0.5081          | 0.3477 |
| 0.0322        | 23.09 | 11500 | 0.5184          | 0.3439 |
| 0.0316        | 24.1  | 12000 | 0.5412          | 0.3450 |
| 0.0262        | 25.1  | 12500 | 0.5113          | 0.3425 |
| 0.0267        | 26.1  | 13000 | 0.4888          | 0.3414 |
| 0.0258        | 27.11 | 13500 | 0.5071          | 0.3371 |
| 0.0226        | 28.11 | 14000 | 0.5311          | 0.3380 |
| 0.0233        | 29.12 | 14500 | 0.5195          | 0.3386 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.0+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1
