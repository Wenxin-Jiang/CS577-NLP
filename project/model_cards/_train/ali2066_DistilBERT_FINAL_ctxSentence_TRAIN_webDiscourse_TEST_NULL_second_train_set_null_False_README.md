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
- name: DistilBERT_FINAL_ctxSentence_TRAIN_webDiscourse_TEST_NULL_second_train_set_null_False
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DistilBERT_FINAL_ctxSentence_TRAIN_webDiscourse_TEST_NULL_second_train_set_null_False

This model is a fine-tuned version of [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0703
- Precision: 0.9667
- Recall: 0.0505
- F1: 0.0961
- Accuracy: 0.0766

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
| No log        | 1.0   | 95   | 0.5442          | 0.6667    | 0.1132 | 0.1935 | 0.75     |
| No log        | 2.0   | 190  | 0.5316          | 0.5385    | 0.1321 | 0.2121 | 0.74     |
| No log        | 3.0   | 285  | 0.5384          | 0.4615    | 0.2264 | 0.3038 | 0.725    |
| No log        | 4.0   | 380  | 0.5503          | 0.4286    | 0.2264 | 0.2963 | 0.715    |
| No log        | 5.0   | 475  | 0.5529          | 0.4286    | 0.2264 | 0.2963 | 0.715    |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.1+cu113
- Datasets 1.18.0
- Tokenizers 0.10.3
