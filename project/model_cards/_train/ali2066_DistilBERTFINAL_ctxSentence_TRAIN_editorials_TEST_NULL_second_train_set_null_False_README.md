---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: DistilBERTFINAL_ctxSentence_TRAIN_editorials_TEST_NULL_second_train_set_null_False
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DistilBERTFINAL_ctxSentence_TRAIN_editorials_TEST_NULL_second_train_set_null_False

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base](https://huggingface.co/cardiffnlp/twitter-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.4527
- Precision: 0.2844
- Recall: 0.9676
- F1: 0.4395
- Accuracy: 0.2991

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
| No log        | 1.0   | 166  | 0.1044          | 0.9742    | 1.0    | 0.9869 | 0.9742   |
| No log        | 2.0   | 332  | 0.1269          | 0.9742    | 1.0    | 0.9869 | 0.9742   |
| No log        | 3.0   | 498  | 0.1028          | 0.9742    | 1.0    | 0.9869 | 0.9742   |
| 0.0947        | 4.0   | 664  | 0.0836          | 0.9826    | 0.9971 | 0.9898 | 0.9799   |
| 0.0947        | 5.0   | 830  | 0.0884          | 0.9854    | 0.9912 | 0.9883 | 0.9771   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
