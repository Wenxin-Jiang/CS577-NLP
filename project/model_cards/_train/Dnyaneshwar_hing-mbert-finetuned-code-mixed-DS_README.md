---
license: cc-by-4.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: hing-mbert-finetuned-code-mixed-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hing-mbert-finetuned-code-mixed-DS

This model is a fine-tuned version of [l3cube-pune/hing-mbert](https://huggingface.co/l3cube-pune/hing-mbert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0518
- Accuracy: 0.7545
- Precision: 0.7041
- Recall: 0.7076
- F1: 0.7053

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2.7277800745684633e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.8338        | 1.0   | 497  | 0.6922          | 0.7163   | 0.6697    | 0.6930 | 0.6686 |
| 0.5744        | 2.0   | 994  | 0.7872          | 0.7324   | 0.6786    | 0.6967 | 0.6845 |
| 0.36          | 3.0   | 1491 | 1.0518          | 0.7545   | 0.7041    | 0.7076 | 0.7053 |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
