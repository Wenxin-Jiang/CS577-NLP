---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wsj0-full-supervised
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wsj0-full-supervised

This model is a fine-tuned version of [facebook/wav2vec2-large-lv60](https://huggingface.co/facebook/wav2vec2-large-lv60) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0623
- Wer: 0.0343

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 5.517         | 0.86  | 500   | 2.9475          | 1.0    |
| 2.2387        | 1.72  | 1000  | 0.4004          | 0.3498 |
| 0.3081        | 2.57  | 1500  | 0.1362          | 0.1159 |
| 0.1744        | 3.43  | 2000  | 0.1125          | 0.0929 |
| 0.1285        | 4.29  | 2500  | 0.0894          | 0.0727 |
| 0.1015        | 5.15  | 3000  | 0.0852          | 0.0642 |
| 0.0811        | 6.0   | 3500  | 0.0789          | 0.0614 |
| 0.0748        | 6.86  | 4000  | 0.0746          | 0.0529 |
| 0.0639        | 7.72  | 4500  | 0.0714          | 0.0481 |
| 0.0606        | 8.58  | 5000  | 0.0698          | 0.0489 |
| 0.0525        | 9.43  | 5500  | 0.0747          | 0.0464 |
| 0.0489        | 10.29 | 6000  | 0.0594          | 0.0396 |
| 0.0419        | 11.15 | 6500  | 0.0600          | 0.0359 |
| 0.0414        | 12.01 | 7000  | 0.0612          | 0.0412 |
| 0.0383        | 12.86 | 7500  | 0.0676          | 0.0392 |
| 0.0352        | 13.72 | 8000  | 0.0626          | 0.0388 |
| 0.034         | 14.58 | 8500  | 0.0699          | 0.0372 |
| 0.0309        | 15.44 | 9000  | 0.0807          | 0.0420 |
| 0.0295        | 16.3  | 9500  | 0.0796          | 0.0396 |
| 0.0273        | 17.15 | 10000 | 0.0716          | 0.0376 |
| 0.0271        | 18.01 | 10500 | 0.0657          | 0.0384 |
| 0.0251        | 18.87 | 11000 | 0.0585          | 0.0351 |
| 0.024         | 19.73 | 11500 | 0.0557          | 0.0347 |
| 0.0252        | 20.58 | 12000 | 0.0609          | 0.0327 |
| 0.0231        | 21.44 | 12500 | 0.0720          | 0.0368 |
| 0.0202        | 22.3  | 13000 | 0.0625          | 0.0343 |
| 0.0195        | 23.16 | 13500 | 0.0635          | 0.0372 |
| 0.0201        | 24.01 | 14000 | 0.0582          | 0.0335 |
| 0.0183        | 24.87 | 14500 | 0.0562          | 0.0343 |
| 0.0183        | 25.73 | 15000 | 0.0629          | 0.0335 |
| 0.0175        | 26.59 | 15500 | 0.0593          | 0.0323 |
| 0.017         | 27.44 | 16000 | 0.0631          | 0.0339 |
| 0.0162        | 28.3  | 16500 | 0.0597          | 0.0335 |
| 0.0169        | 29.16 | 17000 | 0.0623          | 0.0343 |


### Framework versions

- Transformers 4.14.1
- Pytorch 1.10.2
- Datasets 1.18.2
- Tokenizers 0.10.3
