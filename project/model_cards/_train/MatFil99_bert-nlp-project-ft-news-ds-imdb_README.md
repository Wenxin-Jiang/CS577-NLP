---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-nlp-project-ft-news-ds-imdb
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-nlp-project-ft-news-ds-imdb

This model is a fine-tuned version of [jestemleon/bert-nlp-project-news](https://huggingface.co/jestemleon/bert-nlp-project-news) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2678
- Accuracy: 0.944
- F1: 0.9433

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
| 0.2722        | 0.38  | 750  | 0.1888          | 0.9283   | 0.9262 |
| 0.2133        | 0.75  | 1500 | 0.1709          | 0.939    | 0.9363 |
| 0.1752        | 1.12  | 2250 | 0.2139          | 0.9395   | 0.9397 |
| 0.1234        | 1.5   | 3000 | 0.2063          | 0.944    | 0.9428 |
| 0.117         | 1.88  | 3750 | 0.2787          | 0.9327   | 0.9336 |
| 0.0766        | 2.25  | 4500 | 0.2711          | 0.9417   | 0.9412 |
| 0.0603        | 2.62  | 5250 | 0.2659          | 0.9423   | 0.9406 |
| 0.0563        | 3.0   | 6000 | 0.2678          | 0.944    | 0.9433 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
