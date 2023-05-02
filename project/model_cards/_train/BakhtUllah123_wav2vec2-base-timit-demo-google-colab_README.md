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
- Loss: 0.5282
- Wer: 0.3302

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
| 3.5185        | 1.0   | 500   | 1.5798          | 0.9593 |
| 0.8096        | 2.01  | 1000  | 0.5024          | 0.5082 |
| 0.4196        | 3.01  | 1500  | 0.4594          | 0.4489 |
| 0.2936        | 4.02  | 2000  | 0.4104          | 0.4131 |
| 0.2215        | 5.02  | 2500  | 0.4308          | 0.4062 |
| 0.1891        | 6.02  | 3000  | 0.4242          | 0.3825 |
| 0.1626        | 7.03  | 3500  | 0.4187          | 0.3792 |
| 0.136         | 8.03  | 4000  | 0.4387          | 0.3766 |
| 0.1221        | 9.04  | 4500  | 0.4634          | 0.3832 |
| 0.1119        | 10.04 | 5000  | 0.4271          | 0.3640 |
| 0.0976        | 11.04 | 5500  | 0.4379          | 0.3701 |
| 0.0846        | 12.05 | 6000  | 0.4686          | 0.3648 |
| 0.0792        | 13.05 | 6500  | 0.4502          | 0.3595 |
| 0.0709        | 14.06 | 7000  | 0.4723          | 0.3634 |
| 0.0671        | 15.06 | 7500  | 0.4601          | 0.3577 |
| 0.058         | 16.06 | 8000  | 0.5146          | 0.3535 |
| 0.055         | 17.07 | 8500  | 0.5352          | 0.3540 |
| 0.0576        | 18.07 | 9000  | 0.5102          | 0.3469 |
| 0.0448        | 19.08 | 9500  | 0.5159          | 0.3527 |
| 0.0429        | 20.08 | 10000 | 0.5085          | 0.3538 |
| 0.0384        | 21.08 | 10500 | 0.5001          | 0.3453 |
| 0.0339        | 22.09 | 11000 | 0.5322          | 0.3460 |
| 0.032         | 23.09 | 11500 | 0.5295          | 0.3459 |
| 0.0306        | 24.1  | 12000 | 0.5285          | 0.3434 |
| 0.0268        | 25.1  | 12500 | 0.5280          | 0.3382 |
| 0.0231        | 26.1  | 13000 | 0.5259          | 0.3363 |
| 0.0242        | 27.11 | 13500 | 0.5298          | 0.3325 |
| 0.0215        | 28.11 | 14000 | 0.5350          | 0.3306 |
| 0.0226        | 29.12 | 14500 | 0.5282          | 0.3302 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1
