---
tags:
- generated_from_trainer
model-index:
- name: kobigbird-bert-base-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# kobigbird-bert-base-finetuned

This model is a fine-tuned version of [monologg/kobigbird-bert-base](https://huggingface.co/monologg/kobigbird-bert-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8070

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
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 3.5433        | 0.52  | 500  | 1.7958          |
| 1.5093        | 1.03  | 1000 | 1.1129          |
| 1.1411        | 1.55  | 1500 | 1.0226          |
| 0.9785        | 2.07  | 2000 | 0.8868          |
| 0.8037        | 2.58  | 2500 | 0.8301          |
| 0.7273        | 3.1   | 3000 | 0.8552          |
| 0.6034        | 3.62  | 3500 | 0.8070          |


### Framework versions

- Transformers 4.23.0
- Pytorch 1.12.1+cu113
- Datasets 2.5.2
- Tokenizers 0.13.1
