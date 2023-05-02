---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: _ctxSentence_TRAIN_all_TEST_french_second_train_set_french_False
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# _ctxSentence_TRAIN_all_TEST_french_second_train_set_french_False

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base](https://huggingface.co/cardiffnlp/twitter-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4936
- Precision: 0.8189
- Recall: 0.9811
- F1: 0.8927
- Accuracy: 0.8120

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 13   | 0.5150          | 0.7447    | 1.0    | 0.8537 | 0.7447   |
| No log        | 2.0   | 26   | 0.5565          | 0.7447    | 1.0    | 0.8537 | 0.7447   |
| No log        | 3.0   | 39   | 0.5438          | 0.7778    | 1.0    | 0.8750 | 0.7872   |
| No log        | 4.0   | 52   | 0.5495          | 0.7778    | 1.0    | 0.8750 | 0.7872   |
| No log        | 5.0   | 65   | 0.5936          | 0.7778    | 1.0    | 0.8750 | 0.7872   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
