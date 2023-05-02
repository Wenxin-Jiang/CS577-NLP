---
tags:
- generated_from_trainer
model-index:
- name: kobert-finetuned-klue-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# kobert-finetuned-klue-v2

This model is a fine-tuned version of [monologg/kobert](https://huggingface.co/monologg/kobert) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 5.3234

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 5.5898        | 1.08  | 500  | 5.2618          |
| 5.217         | 2.16  | 1000 | 5.1505          |
| 5.1044        | 3.24  | 1500 | 5.0895          |
| 5.0048        | 4.32  | 2000 | 5.0649          |
| 4.8292        | 5.4   | 2500 | 4.9589          |
| 4.5451        | 6.48  | 3000 | 4.8549          |
| 4.2284        | 7.56  | 3500 | 4.8801          |
| 3.9195        | 8.64  | 4000 | 4.8797          |
| 3.6506        | 9.72  | 4500 | 4.8009          |
| 3.4175        | 10.8  | 5000 | 4.8996          |
| 3.1964        | 11.88 | 5500 | 4.9734          |
| 3.0401        | 12.96 | 6000 | 4.9378          |
| 2.8965        | 14.04 | 6500 | 5.3631          |
| 2.7672        | 15.12 | 7000 | 5.3234          |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.2
- Tokenizers 0.12.1
