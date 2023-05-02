---
license: mit
tags:
- generated_from_trainer
model-index:
- name: roberta-base-IMDB_roberta
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-IMDB_roberta

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1897

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
- num_epochs: 16

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 2.7882        | 1.0   | 1250  | 2.4751          |
| 2.5749        | 2.0   | 2500  | 2.4183          |
| 2.4501        | 3.0   | 3750  | 2.3799          |
| 2.3697        | 4.0   | 5000  | 2.3792          |
| 2.3187        | 5.0   | 6250  | 2.3622          |
| 2.24          | 6.0   | 7500  | 2.3491          |
| 2.164         | 7.0   | 8750  | 2.3146          |
| 2.1187        | 8.0   | 10000 | 2.2804          |
| 2.0552        | 9.0   | 11250 | 2.2629          |
| 2.0285        | 10.0  | 12500 | 2.2088          |
| 1.9807        | 11.0  | 13750 | 2.2061          |
| 1.9597        | 12.0  | 15000 | 2.2094          |
| 1.9062        | 13.0  | 16250 | 2.1486          |
| 1.8766        | 14.0  | 17500 | 2.1348          |
| 1.8528        | 15.0  | 18750 | 2.1665          |
| 1.8425        | 16.0  | 20000 | 2.1897          |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
