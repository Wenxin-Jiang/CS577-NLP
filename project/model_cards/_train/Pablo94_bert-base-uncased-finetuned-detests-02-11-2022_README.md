---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: bert-base-uncased-finetuned-detests-02-11-2022
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-detests-02-11-2022

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0794
- F1: 0.5455

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.014         | 0.64  | 25   | 0.6229          | 0.5536 |
| 0.0698        | 1.28  | 50   | 0.6996          | 0.5907 |
| 0.0173        | 1.92  | 75   | 0.7531          | 0.5882 |
| 0.0032        | 2.56  | 100  | 0.8054          | 0.4928 |
| 0.0087        | 3.21  | 125  | 0.9557          | 0.5735 |
| 0.0028        | 3.85  | 150  | 0.8859          | 0.5352 |
| 0.013         | 4.49  | 175  | 0.9674          | 0.5536 |
| 0.0031        | 5.13  | 200  | 0.9073          | 0.5691 |
| 0.0032        | 5.77  | 225  | 0.9253          | 0.5439 |
| 0.0483        | 6.41  | 250  | 0.9705          | 0.5837 |
| 0.0323        | 7.05  | 275  | 1.0368          | 0.5824 |
| 0.0019        | 7.69  | 300  | 1.0221          | 0.5520 |
| 0.0256        | 8.33  | 325  | 1.0419          | 0.5523 |
| 0.0319        | 8.97  | 350  | 1.0764          | 0.5425 |
| 0.0125        | 9.62  | 375  | 1.0794          | 0.5455 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
