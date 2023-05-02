---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-nlp-project-ft-news-ds-google
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-nlp-project-ft-news-ds-google

This model is a fine-tuned version of [jestemleon/bert-nlp-project-news](https://huggingface.co/jestemleon/bert-nlp-project-news) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3238
- Accuracy: 0.9038
- F1: 0.9107

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.3415        | 0.37  | 196  | 0.2452          | 0.9048   | 0.9136 |
| 0.2747        | 0.75  | 392  | 0.2425          | 0.9076   | 0.9136 |
| 0.2309        | 1.12  | 588  | 0.2658          | 0.9114   | 0.9179 |
| 0.1964        | 1.49  | 784  | 0.2916          | 0.9010   | 0.9055 |
| 0.1812        | 1.86  | 980  | 0.2950          | 0.9019   | 0.9091 |
| 0.1569        | 2.24  | 1176 | 0.2926          | 0.9095   | 0.9164 |
| 0.1173        | 2.61  | 1372 | 0.3188          | 0.9076   | 0.9145 |
| 0.1145        | 2.98  | 1568 | 0.3238          | 0.9038   | 0.9107 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
