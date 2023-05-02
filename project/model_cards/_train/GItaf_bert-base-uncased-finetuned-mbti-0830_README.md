---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: bert-base-uncased-finetuned-mbti-0830
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-mbti-0830

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.1613

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 4.4259        | 1.0   | 9720  | 4.3466          |
| 4.2788        | 2.0   | 19440 | 4.2536          |
| 4.1928        | 3.0   | 29160 | 4.2074          |
| 4.1062        | 4.0   | 38880 | 4.1839          |
| 4.0502        | 5.0   | 48600 | 4.1715          |
| 4.0037        | 6.0   | 58320 | 4.1637          |
| 3.9575        | 7.0   | 68040 | 4.1603          |
| 3.9169        | 8.0   | 77760 | 4.1591          |
| 3.8915        | 9.0   | 87480 | 4.1602          |
| 3.8741        | 10.0  | 97200 | 4.1613          |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
