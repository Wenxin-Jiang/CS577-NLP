---
tags:
- generated_from_trainer
model-index:
- name: kobigbird-bert-base-finetuned-klue-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# kobigbird-bert-base-finetuned-klue-v2

This model is a fine-tuned version of [monologg/kobigbird-bert-base](https://huggingface.co/monologg/kobigbird-bert-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9250

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 4.5274        | 0.35  | 500  | 2.7400          |
| 1.9296        | 0.69  | 1000 | 1.4055          |
| 1.3583        | 1.04  | 1500 | 1.1407          |
| 1.1119        | 1.38  | 2000 | 1.0246          |
| 1.017         | 1.73  | 2500 | 0.9231          |
| 0.8637        | 2.07  | 3000 | 0.9507          |
| 0.6573        | 2.42  | 3500 | 0.9678          |
| 0.6916        | 2.76  | 4000 | 0.9250          |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.2
- Tokenizers 0.12.1
