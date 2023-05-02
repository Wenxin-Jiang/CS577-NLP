---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: DistilBERTFINAL_ctxSentence_TRAIN_webDiscourse_TEST_NULL_second_train_set_null_False
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DistilBERTFINAL_ctxSentence_TRAIN_webDiscourse_TEST_NULL_second_train_set_null_False

This model is a fine-tuned version of [cardiffnlp/twitter-roberta-base](https://huggingface.co/cardiffnlp/twitter-roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.2555
- Precision: 1.0
- Recall: 0.0200
- F1: 0.0393
- Accuracy: 0.0486

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
| No log        | 1.0   | 95   | 0.5756          | nan       | 0.0    | nan    | 0.715    |
| No log        | 2.0   | 190  | 0.5340          | 0.6429    | 0.1579 | 0.2535 | 0.735    |
| No log        | 3.0   | 285  | 0.5298          | 0.5833    | 0.3684 | 0.4516 | 0.745    |
| No log        | 4.0   | 380  | 0.5325          | 0.5789    | 0.3860 | 0.4632 | 0.745    |
| No log        | 5.0   | 475  | 0.5452          | 0.4815    | 0.4561 | 0.4685 | 0.705    |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
