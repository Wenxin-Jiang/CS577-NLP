---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: DistilBERTFINAL_ctxSentence_TRAIN_all_TEST_NULL_second_train_set_null_False
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DistilBERTFINAL_ctxSentence_TRAIN_all_TEST_NULL_second_train_set_null_False

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base](https://huggingface.co/cardiffnlp/twitter-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0557
- Precision: 0.9930
- Recall: 0.9878
- F1: 0.9904
- Accuracy: 0.9814

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
| No log        | 1.0   | 479  | 0.3334          | 0.9041    | 0.9041 | 0.9041 | 0.8550   |
| 0.3756        | 2.0   | 958  | 0.3095          | 0.8991    | 0.9251 | 0.9119 | 0.8649   |
| 0.2653        | 3.0   | 1437 | 0.3603          | 0.8929    | 0.9527 | 0.9218 | 0.8779   |
| 0.1991        | 4.0   | 1916 | 0.3907          | 0.8919    | 0.9540 | 0.9219 | 0.8779   |
| 0.1586        | 5.0   | 2395 | 0.3642          | 0.9070    | 0.9356 | 0.9211 | 0.8788   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
