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
- name: DistilBERT_FINAL_ctxSentence_TRAIN_editorials_TEST_NULL_second_train_set_null_False
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DistilBERT_FINAL_ctxSentence_TRAIN_editorials_TEST_NULL_second_train_set_null_False

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.8119
- Precision: 0.2752
- Recall: 0.9522
- F1: 0.4270
- Accuracy: 0.2849

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
| No log        | 1.0   | 166  | 0.0726          | 0.9827    | 1.0    | 0.9913 | 0.9828   |
| No log        | 2.0   | 332  | 0.0569          | 0.9827    | 1.0    | 0.9913 | 0.9828   |
| No log        | 3.0   | 498  | 0.0434          | 0.9884    | 1.0    | 0.9942 | 0.9885   |
| 0.1021        | 4.0   | 664  | 0.0505          | 0.9884    | 1.0    | 0.9942 | 0.9885   |
| 0.1021        | 5.0   | 830  | 0.0472          | 0.9884    | 1.0    | 0.9942 | 0.9885   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
