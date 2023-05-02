---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: DistilBERTFINAL_ctxSentence_TRAIN_all_TEST_french_second_train_set_NULL_True
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DistilBERTFINAL_ctxSentence_TRAIN_all_TEST_french_second_train_set_NULL_True

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base](https://huggingface.co/cardiffnlp/twitter-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4024
- Precision: 0.8643
- Recall: 0.9769
- F1: 0.9171
- Accuracy: 0.8594

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
| No log        | 1.0   | 130  | 0.4920          | 0.7766    | 1.0    | 0.8742 | 0.7766   |
| No log        | 2.0   | 260  | 0.4469          | 0.7885    | 1.0    | 0.8818 | 0.7918   |
| No log        | 3.0   | 390  | 0.3860          | 0.8248    | 0.9860 | 0.8982 | 0.8265   |
| 0.462         | 4.0   | 520  | 0.3948          | 0.8441    | 0.9832 | 0.9084 | 0.8460   |
| 0.462         | 5.0   | 650  | 0.3694          | 0.8632    | 0.9693 | 0.9132 | 0.8568   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
