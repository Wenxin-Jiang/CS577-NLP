---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: xlm-roberta-base-finetuned-combined-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-finetuned-combined-DS

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0232
- Accuracy: 0.6362
- Precision: 0.6193
- Recall: 0.6204
- F1: 0.6160

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4.1187640010910775e-05
- train_batch_size: 16
- eval_batch_size: 32
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0408        | 1.0   | 711  | 1.0206          | 0.5723   | 0.5597    | 0.5122 | 0.4897 |
| 0.9224        | 2.0   | 1422 | 0.9092          | 0.5695   | 0.5745    | 0.5610 | 0.5572 |
| 0.8395        | 3.0   | 2133 | 0.8878          | 0.6088   | 0.6083    | 0.6071 | 0.5981 |
| 0.7418        | 3.99  | 2844 | 0.8828          | 0.6088   | 0.6009    | 0.6068 | 0.5936 |
| 0.6484        | 4.99  | 3555 | 0.9636          | 0.6355   | 0.6235    | 0.6252 | 0.6184 |
| 0.5644        | 5.99  | 4266 | 1.0232          | 0.6362   | 0.6193    | 0.6204 | 0.6160 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
