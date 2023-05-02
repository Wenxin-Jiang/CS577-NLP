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
- name: DistilBERT_FINAL_ctxSentence_TRAIN_all_TEST_NULL_second_train_set_null_False
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DistilBERT_FINAL_ctxSentence_TRAIN_all_TEST_NULL_second_train_set_null_False

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0699
- Precision: 0.9942
- Recall: 0.9773
- F1: 0.9857
- Accuracy: 0.9725

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
| No log        | 1.0   | 479  | 0.4036          | 0.8333    | 0.9326 | 0.8802 | 0.8054   |
| 0.5047        | 2.0   | 958  | 0.3749          | 0.8635    | 0.9339 | 0.8973 | 0.8361   |
| 0.3336        | 3.0   | 1437 | 0.3789          | 0.8862    | 0.9184 | 0.9020 | 0.8471   |
| 0.2644        | 4.0   | 1916 | 0.4024          | 0.8762    | 0.9171 | 0.8962 | 0.8371   |
| 0.2233        | 5.0   | 2395 | 0.4195          | 0.8784    | 0.9171 | 0.8973 | 0.8391   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
