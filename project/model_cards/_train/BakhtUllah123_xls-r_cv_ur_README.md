---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: xls-r_cv_ur
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xls-r_cv_ur

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4888
- Wer: 1.0

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
- lr_scheduler_warmup_steps: 100
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer |
|:-------------:|:-----:|:----:|:---------------:|:---:|
| 8.4361        | 1.14  | 100  | 2.3733          | 1.0 |
| 1.9609        | 2.27  | 200  | 1.8280          | 1.0 |
| 1.8191        | 3.41  | 300  | 1.8259          | 1.0 |
| 1.8359        | 4.55  | 400  | 1.8069          | 1.0 |
| 1.7667        | 5.68  | 500  | 1.8038          | 1.0 |
| 1.7751        | 6.82  | 600  | 1.7473          | 1.0 |
| 1.7428        | 7.95  | 700  | 1.6996          | 1.0 |
| 1.697         | 9.09  | 800  | 1.6364          | 1.0 |
| 1.6532        | 10.23 | 900  | 1.4985          | 1.0 |
| 1.5217        | 11.36 | 1000 | 1.2836          | 1.0 |
| 1.3385        | 12.5  | 1100 | 1.0293          | 1.0 |
| 1.1596        | 13.64 | 1200 | 0.8294          | 1.0 |
| 1.0655        | 14.77 | 1300 | 0.7150          | 1.0 |
| 0.9951        | 15.91 | 1400 | 0.6364          | 1.0 |
| 0.9013        | 17.05 | 1500 | 0.5548          | 1.0 |
| 0.8276        | 18.18 | 1600 | 0.5200          | 1.0 |
| 0.8129        | 19.32 | 1700 | 0.4888          | 1.0 |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.11.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
