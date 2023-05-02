---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: sentence_bert-base-uncased-finetuned-SENTENCE
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# sentence_bert-base-uncased-finetuned-SENTENCE

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4834
- Precision: 0.8079
- Recall: 1.0
- F1: 0.8938
- Accuracy: 0.8079

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 13   | 0.3520          | 0.8889    | 1.0    | 0.9412 | 0.8889   |
| No log        | 2.0   | 26   | 0.3761          | 0.8889    | 1.0    | 0.9412 | 0.8889   |
| No log        | 3.0   | 39   | 0.3683          | 0.8889    | 1.0    | 0.9412 | 0.8889   |
| No log        | 4.0   | 52   | 0.3767          | 0.8889    | 1.0    | 0.9412 | 0.8889   |
| No log        | 5.0   | 65   | 0.3834          | 0.8889    | 1.0    | 0.9412 | 0.8889   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
