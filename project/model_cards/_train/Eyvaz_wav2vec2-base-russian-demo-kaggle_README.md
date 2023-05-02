---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-base-russian-demo-kaggle
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-russian-demo-kaggle

This model is a fine-tuned version of [facebook/wav2vec2-base](https://huggingface.co/facebook/wav2vec2-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: inf
- Wer: 0.9997

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
- train_batch_size: 12
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 24
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 0.0102        | 1.03  | 500   | inf             | 0.9997 |
| 0.0068        | 2.06  | 1000  | inf             | 0.9997 |
| 0.0           | 3.09  | 1500  | inf             | 0.9997 |
| 0.0313        | 4.12  | 2000  | inf             | 0.9997 |
| 0.0           | 5.15  | 2500  | inf             | 0.9997 |
| 0.0052        | 6.19  | 3000  | inf             | 0.9997 |
| 0.0287        | 7.22  | 3500  | inf             | 0.9997 |
| 0.0           | 8.25  | 4000  | inf             | 0.9997 |
| 0.01          | 9.28  | 4500  | inf             | 0.9997 |
| 0.0           | 10.31 | 5000  | inf             | 0.9997 |
| 0.3919        | 11.34 | 5500  | inf             | 0.9997 |
| 0.0           | 12.37 | 6000  | inf             | 0.9997 |
| 0.0           | 13.4  | 6500  | inf             | 0.9997 |
| 0.0           | 14.43 | 7000  | inf             | 0.9997 |
| 0.6422        | 15.46 | 7500  | inf             | 0.9997 |
| 0.0           | 16.49 | 8000  | inf             | 0.9997 |
| 0.0           | 17.53 | 8500  | inf             | 0.9997 |
| 0.0           | 18.56 | 9000  | inf             | 0.9997 |
| 0.0           | 19.59 | 9500  | inf             | 0.9997 |
| 0.0           | 20.62 | 10000 | inf             | 0.9997 |
| 0.0427        | 21.65 | 10500 | inf             | 0.9997 |
| 0.0           | 22.68 | 11000 | inf             | 0.9997 |
| 0.0           | 23.71 | 11500 | inf             | 0.9997 |
| 0.0           | 24.74 | 12000 | inf             | 0.9997 |
| 0.0091        | 25.77 | 12500 | inf             | 0.9997 |
| 0.1243        | 26.8  | 13000 | inf             | 0.9997 |
| 0.0           | 27.83 | 13500 | inf             | 0.9997 |
| 0.0           | 28.87 | 14000 | inf             | 0.9997 |
| 0.0           | 29.9  | 14500 | inf             | 0.9997 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.1
- Datasets 1.13.3
- Tokenizers 0.10.3
