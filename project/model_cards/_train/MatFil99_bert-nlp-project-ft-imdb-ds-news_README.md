---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-nlp-project-ft-imdb-ds-news
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-nlp-project-ft-imdb-ds-news

This model is a fine-tuned version of [jestemleon/bert-nlp-project-imdb](https://huggingface.co/jestemleon/bert-nlp-project-imdb) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4268
- Accuracy: 0.8984
- F1: 0.8780

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
| 0.4318        | 0.37  | 120  | 0.3162          | 0.8828   | 0.8598 |
| 0.3094        | 0.75  | 240  | 0.2958          | 0.8891   | 0.8678 |
| 0.2667        | 1.12  | 360  | 0.3354          | 0.8984   | 0.8776 |
| 0.2074        | 1.5   | 480  | 0.3459          | 0.8922   | 0.8691 |
| 0.1805        | 1.87  | 600  | 0.3802          | 0.8969   | 0.8769 |
| 0.132         | 2.24  | 720  | 0.3858          | 0.9      | 0.8779 |
| 0.1051        | 2.62  | 840  | 0.4174          | 0.8969   | 0.8755 |
| 0.1074        | 2.99  | 960  | 0.4268          | 0.8984   | 0.8780 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
