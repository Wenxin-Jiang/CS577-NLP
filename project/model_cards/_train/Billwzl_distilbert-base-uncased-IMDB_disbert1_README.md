---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: distilbert-base-uncased-IMDB_disbert1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-IMDB_disbert1

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0461

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 12

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 2.5838        | 1.0   | 10000  | 2.3985          |
| 2.4367        | 2.0   | 20000  | 2.3194          |
| 2.349         | 3.0   | 30000  | 2.2716          |
| 2.2764        | 4.0   | 40000  | 2.2392          |
| 2.2169        | 5.0   | 50000  | 2.1972          |
| 2.1623        | 6.0   | 60000  | 2.1655          |
| 2.122         | 7.0   | 70000  | 2.1277          |
| 2.0728        | 8.0   | 80000  | 2.1221          |
| 2.0348        | 9.0   | 90000  | 2.0928          |
| 1.9918        | 10.0  | 100000 | 2.0739          |
| 1.9621        | 11.0  | 110000 | 2.0536          |
| 1.9394        | 12.0  | 120000 | 2.0461          |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
