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
- name: DistilBERT_FINAL_ctxSentence_TRAIN_essays_TEST_NULL_second_train_set_null_False
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DistilBERT_FINAL_ctxSentence_TRAIN_essays_TEST_NULL_second_train_set_null_False

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7321
- Precision: 0.9795
- Recall: 0.7277
- F1: 0.835
- Accuracy: 0.7208

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
| No log        | 1.0   | 130  | 0.3755          | 0.8521    | 0.9910 | 0.9163 | 0.8529   |
| No log        | 2.0   | 260  | 0.3352          | 0.8875    | 0.9638 | 0.9241 | 0.8713   |
| No log        | 3.0   | 390  | 0.3370          | 0.8918    | 0.9321 | 0.9115 | 0.8529   |
| 0.4338        | 4.0   | 520  | 0.3415          | 0.8957    | 0.9321 | 0.9135 | 0.8566   |
| 0.4338        | 5.0   | 650  | 0.3416          | 0.8918    | 0.9321 | 0.9115 | 0.8529   |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
