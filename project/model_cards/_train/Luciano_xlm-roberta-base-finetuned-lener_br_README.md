---
language:
- pt
license: mit
tags:
- generated_from_trainer
model-index:
- name: xlm-roberta-base-finetuned-lener_br
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-finetuned-lener_br

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9094

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 1.545         | 1.0   | 2079  | 1.4107          |
| 1.4708        | 2.0   | 4158  | 1.3126          |
| 1.322         | 3.0   | 6237  | 1.1943          |
| 1.1986        | 4.0   | 8316  | 1.1581          |
| 1.1316        | 5.0   | 10395 | 1.1156          |
| 1.0824        | 6.0   | 12474 | 1.0400          |
| 1.0435        | 7.0   | 14553 | 1.0276          |
| 0.9824        | 8.0   | 16632 | 1.0119          |
| 0.9289        | 9.0   | 18711 | nan             |
| 0.9123        | 10.0  | 20790 | 0.9945          |
| 0.8591        | 11.0  | 22869 | nan             |
| 0.8411        | 12.0  | 24948 | 0.9413          |
| 0.8376        | 13.0  | 27027 | 0.9411          |
| 0.7868        | 14.0  | 29106 | 0.9228          |
| 0.8012        | 15.0  | 31185 | 0.9449          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
