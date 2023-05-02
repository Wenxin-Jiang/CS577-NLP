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
- name: hasoc19-bert-base-multilingual-cased-sentiment-new
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hasoc19-bert-base-multilingual-cased-sentiment-new

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4758
- Accuracy: 0.8501
- Precision: 0.8524
- Recall: 0.8501
- F1: 0.8507

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
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.4987        | 1.0   | 537  | 0.3931          | 0.8249   | 0.8304    | 0.8249 | 0.8208 |
| 0.3676        | 2.0   | 1074 | 0.3513          | 0.8417   | 0.8487    | 0.8417 | 0.8427 |
| 0.2883        | 3.0   | 1611 | 0.3604          | 0.8475   | 0.8484    | 0.8475 | 0.8478 |
| 0.235         | 4.0   | 2148 | 0.3929          | 0.8501   | 0.8509    | 0.8501 | 0.8504 |
| 0.1859        | 5.0   | 2685 | 0.4413          | 0.8449   | 0.8451    | 0.8449 | 0.8450 |
| 0.1563        | 6.0   | 3222 | 0.4758          | 0.8501   | 0.8524    | 0.8501 | 0.8507 |


### Framework versions

- Transformers 4.24.0.dev0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.13.1
