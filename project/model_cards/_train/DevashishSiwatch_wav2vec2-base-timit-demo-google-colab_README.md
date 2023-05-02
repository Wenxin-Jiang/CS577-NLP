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
- Loss: 0.5108
- Wer: 0.3342

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
| 3.6383        | 1.0   | 500   | 2.3747          | 1.0    |
| 0.9624        | 2.01  | 1000  | 0.5724          | 0.5213 |
| 0.4521        | 3.01  | 1500  | 0.4892          | 0.4794 |
| 0.3126        | 4.02  | 2000  | 0.4250          | 0.3991 |
| 0.2299        | 5.02  | 2500  | 0.4288          | 0.3929 |
| 0.195         | 6.02  | 3000  | 0.4707          | 0.3974 |
| 0.1602        | 7.03  | 3500  | 0.4731          | 0.4034 |
| 0.1477        | 8.03  | 4000  | 0.4405          | 0.3896 |
| 0.1284        | 9.04  | 4500  | 0.4663          | 0.3850 |
| 0.1114        | 10.04 | 5000  | 0.4814          | 0.3759 |
| 0.1024        | 11.04 | 5500  | 0.4821          | 0.3701 |
| 0.0973        | 12.05 | 6000  | 0.4718          | 0.3709 |
| 0.0832        | 13.05 | 6500  | 0.5257          | 0.3678 |
| 0.0741        | 14.06 | 7000  | 0.4741          | 0.3621 |
| 0.0696        | 15.06 | 7500  | 0.5073          | 0.3710 |
| 0.0664        | 16.06 | 8000  | 0.4886          | 0.3651 |
| 0.0613        | 17.07 | 8500  | 0.5300          | 0.3588 |
| 0.0612        | 18.07 | 9000  | 0.4983          | 0.3543 |
| 0.049         | 19.08 | 9500  | 0.5158          | 0.3592 |
| 0.0455        | 20.08 | 10000 | 0.5213          | 0.3525 |
| 0.042         | 21.08 | 10500 | 0.4979          | 0.3474 |
| 0.0376        | 22.09 | 11000 | 0.5335          | 0.3493 |
| 0.0331        | 23.09 | 11500 | 0.5276          | 0.3451 |
| 0.0346        | 24.1  | 12000 | 0.5106          | 0.3428 |
| 0.0294        | 25.1  | 12500 | 0.5414          | 0.3426 |
| 0.0265        | 26.1  | 13000 | 0.5234          | 0.3363 |
| 0.0273        | 27.11 | 13500 | 0.5207          | 0.3356 |
| 0.0255        | 28.11 | 14000 | 0.5092          | 0.3354 |
| 0.0248        | 29.12 | 14500 | 0.5108          | 0.3342 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.0+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1
