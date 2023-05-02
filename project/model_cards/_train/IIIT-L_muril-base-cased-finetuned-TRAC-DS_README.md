---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: muril-base-cased-finetuned-TRAC-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# muril-base-cased-finetuned-TRAC-DS

This model is a fine-tuned version of [google/muril-base-cased](https://huggingface.co/google/muril-base-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1894
- Accuracy: 0.6838
- Precision: 0.6534
- Recall: 0.6513
- F1: 0.6522

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 25

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0109        | 1.99  | 612  | 0.9284          | 0.5948   | 0.4327    | 0.5193 | 0.4509 |
| 0.8635        | 3.99  | 1224 | 0.8556          | 0.6291   | 0.6012    | 0.5865 | 0.5888 |
| 0.764         | 5.98  | 1836 | 0.8585          | 0.6609   | 0.6249    | 0.6275 | 0.6260 |
| 0.6744        | 7.97  | 2448 | 0.8469          | 0.6732   | 0.6391    | 0.6408 | 0.6398 |
| 0.5865        | 9.97  | 3060 | 0.8438          | 0.6667   | 0.6424    | 0.6395 | 0.6395 |
| 0.4978        | 11.96 | 3672 | 0.9269          | 0.6855   | 0.6532    | 0.6582 | 0.6542 |
| 0.4245        | 13.95 | 4284 | 0.9934          | 0.6699   | 0.6397    | 0.6482 | 0.6396 |
| 0.378         | 15.95 | 4896 | 1.0488          | 0.6830   | 0.6530    | 0.6446 | 0.6474 |
| 0.3349        | 17.94 | 5508 | 1.0548          | 0.6806   | 0.6505    | 0.6536 | 0.6518 |
| 0.3019        | 19.93 | 6120 | 1.1092          | 0.6757   | 0.6476    | 0.6497 | 0.6482 |
| 0.2869        | 21.93 | 6732 | 1.1515          | 0.6814   | 0.6507    | 0.6514 | 0.6510 |
| 0.2575        | 23.92 | 7344 | 1.1894          | 0.6838   | 0.6534    | 0.6513 | 0.6522 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
