---
tags:
- generated_from_trainer
model-index:
- name: gpt2-gpt2-mc-weight0.25-epoch15-new
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# gpt2-gpt2-mc-weight0.25-epoch15-new

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.7276
- Cls loss: 3.0579
- Lm loss: 3.9626
- Cls Accuracy: 0.6110
- Cls F1: 0.6054
- Cls Precision: 0.6054
- Cls Recall: 0.6110
- Perplexity: 52.59

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Cls loss | Lm loss | Cls Accuracy | Cls F1 | Cls Precision | Cls Recall | Perplexity |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:-------:|:------------:|:------:|:-------------:|:----------:|:----------:|
| 4.674         | 1.0   | 3470  | 4.4372          | 1.5961   | 4.0380  | 0.5487       | 0.5279 | 0.5643        | 0.5487     | 56.71      |
| 4.3809        | 2.0   | 6940  | 4.3629          | 1.4483   | 4.0006  | 0.6023       | 0.5950 | 0.6174        | 0.6023     | 54.63      |
| 4.2522        | 3.0   | 10410 | 4.3721          | 1.5476   | 3.9849  | 0.6012       | 0.5981 | 0.6186        | 0.6012     | 53.78      |
| 4.1478        | 4.0   | 13880 | 4.3892          | 1.6429   | 3.9782  | 0.6081       | 0.6019 | 0.6128        | 0.6081     | 53.42      |
| 4.0491        | 5.0   | 17350 | 4.4182          | 1.8093   | 3.9656  | 0.6156       | 0.6091 | 0.6163        | 0.6156     | 52.75      |
| 3.9624        | 6.0   | 20820 | 4.4757          | 2.0348   | 3.9666  | 0.6121       | 0.6048 | 0.6189        | 0.6121     | 52.81      |
| 3.8954        | 7.0   | 24290 | 4.4969          | 2.1327   | 3.9634  | 0.6092       | 0.6028 | 0.6087        | 0.6092     | 52.64      |
| 3.846         | 8.0   | 27760 | 4.5632          | 2.4063   | 3.9613  | 0.6017       | 0.5972 | 0.6014        | 0.6017     | 52.52      |
| 3.8036        | 9.0   | 31230 | 4.6068          | 2.5888   | 3.9592  | 0.6052       | 0.5988 | 0.6026        | 0.6052     | 52.41      |
| 3.7724        | 10.0  | 34700 | 4.6175          | 2.6197   | 3.9621  | 0.6052       | 0.6006 | 0.6009        | 0.6052     | 52.57      |
| 3.7484        | 11.0  | 38170 | 4.6745          | 2.8470   | 3.9622  | 0.6046       | 0.5996 | 0.6034        | 0.6046     | 52.57      |
| 3.7291        | 12.0  | 41640 | 4.6854          | 2.8950   | 3.9611  | 0.6110       | 0.6056 | 0.6049        | 0.6110     | 52.52      |
| 3.7148        | 13.0  | 45110 | 4.7103          | 2.9919   | 3.9618  | 0.6063       | 0.6002 | 0.6029        | 0.6063     | 52.55      |
| 3.703         | 14.0  | 48580 | 4.7226          | 3.0417   | 3.9616  | 0.6081       | 0.6027 | 0.6021        | 0.6081     | 52.54      |
| 3.6968        | 15.0  | 52050 | 4.7276          | 3.0579   | 3.9626  | 0.6110       | 0.6054 | 0.6054        | 0.6110     | 52.59      |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1