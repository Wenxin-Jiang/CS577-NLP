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
- Loss: 0.5602
- Wer: 0.3438

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
| 3.586         | 1.0   | 500   | 2.7824          | 1.0    |
| 1.1036        | 2.01  | 1000  | 0.7074          | 0.5704 |
| 0.4623        | 3.01  | 1500  | 0.4477          | 0.4580 |
| 0.3152        | 4.02  | 2000  | 0.4067          | 0.4235 |
| 0.2596        | 5.02  | 2500  | 0.4183          | 0.4091 |
| 0.2007        | 6.02  | 3000  | 0.4237          | 0.3892 |
| 0.1643        | 7.03  | 3500  | 0.4918          | 0.3898 |
| 0.1436        | 8.03  | 4000  | 0.4023          | 0.3914 |
| 0.121         | 9.04  | 4500  | 0.4674          | 0.3780 |
| 0.112         | 10.04 | 5000  | 0.4919          | 0.3902 |
| 0.0985        | 11.04 | 5500  | 0.5252          | 0.3781 |
| 0.09          | 12.05 | 6000  | 0.5382          | 0.3595 |
| 0.085         | 13.05 | 6500  | 0.5215          | 0.3646 |
| 0.0731        | 14.06 | 7000  | 0.4600          | 0.3673 |
| 0.0645        | 15.06 | 7500  | 0.5151          | 0.3671 |
| 0.0615        | 16.06 | 8000  | 0.5289          | 0.3662 |
| 0.0543        | 17.07 | 8500  | 0.5193          | 0.3752 |
| 0.057         | 18.07 | 9000  | 0.5403          | 0.3734 |
| 0.0466        | 19.08 | 9500  | 0.5607          | 0.3690 |
| 0.0462        | 20.08 | 10000 | 0.5381          | 0.3599 |
| 0.0409        | 21.08 | 10500 | 0.6067          | 0.3681 |
| 0.0373        | 22.09 | 11000 | 0.5607          | 0.3647 |
| 0.0355        | 23.09 | 11500 | 0.5635          | 0.3612 |
| 0.033         | 24.1  | 12000 | 0.5526          | 0.3570 |
| 0.0284        | 25.1  | 12500 | 0.5514          | 0.3484 |
| 0.0272        | 26.1  | 13000 | 0.5378          | 0.3479 |
| 0.0258        | 27.11 | 13500 | 0.5578          | 0.3446 |
| 0.0242        | 28.11 | 14000 | 0.5557          | 0.3442 |
| 0.0235        | 29.12 | 14500 | 0.5602          | 0.3438 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.12.1+cu113
- Datasets 1.18.3
- Tokenizers 0.12.1
