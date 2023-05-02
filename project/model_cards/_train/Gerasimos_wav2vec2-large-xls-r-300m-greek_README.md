---
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xls-r-300m-greek
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-greek

This model was trained from scratch on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4823
- Wer: 0.3338

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.0106        | 1.72  | 200  | 0.5519          | 0.3537 |
| 0.0249        | 3.45  | 400  | 0.5174          | 0.3465 |
| 0.0206        | 5.17  | 600  | 0.4721          | 0.3323 |
| 0.0221        | 6.89  | 800  | 0.4652          | 0.3373 |
| 0.0204        | 8.62  | 1000 | 0.4883          | 0.3389 |
| 0.0192        | 10.34 | 1200 | 0.4785          | 0.3389 |
| 0.0186        | 12.07 | 1400 | 0.4789          | 0.3378 |
| 0.0172        | 13.79 | 1600 | 0.4915          | 0.3347 |
| 0.0184        | 15.52 | 1800 | 0.4759          | 0.3440 |
| 0.0168        | 17.24 | 2000 | 0.4891          | 0.3371 |
| 0.0155        | 18.96 | 2200 | 0.4928          | 0.3394 |
| 0.0146        | 20.69 | 2400 | 0.4834          | 0.3357 |
| 0.0146        | 22.41 | 2600 | 0.4814          | 0.3362 |
| 0.0151        | 24.14 | 2800 | 0.4791          | 0.3345 |
| 0.0136        | 25.86 | 3000 | 0.4825          | 0.3356 |
| 0.0136        | 27.58 | 3200 | 0.4850          | 0.3351 |
| 0.0127        | 29.31 | 3400 | 0.4823          | 0.3338 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.10.3
