---
license: cc-by-nc-sa-4.0
tags:
- generated_from_trainer
model-index:
- name: chinese-pert-large-finetuned-product
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# chinese-pert-large-finetuned-product

This model is a fine-tuned version of [hfl/chinese-pert-large](https://huggingface.co/hfl/chinese-pert-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0208

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 128
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.0545        | 1.0   | 3237  | 0.0532          |
| 0.0451        | 2.0   | 6474  | 0.0465          |
| 0.0414        | 3.0   | 9711  | 0.0439          |
| 0.0198        | 4.0   | 12948 | 0.0220          |
| 0.0191        | 5.0   | 16185 | 0.0217          |
| 0.0188        | 6.0   | 19422 | 0.0215          |
| 0.0185        | 7.0   | 22659 | 0.0212          |
| 0.0183        | 8.0   | 25896 | 0.0209          |
| 0.0181        | 9.0   | 29133 | 0.0208          |
| 0.018         | 10.0  | 32370 | 0.0208          |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.6.0
- Datasets 2.0.0
- Tokenizers 0.11.6
