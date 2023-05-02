---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: mbti-classification-roberta-base-aug
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbti-classification-roberta-base-aug

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1645
- Accuracy: 0.2834

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 2.1201        | 1.0   | 29900 | 2.1415          | 0.2833   |
| 1.8733        | 2.0   | 59800 | 2.1235          | 0.2866   |
| 1.7664        | 3.0   | 89700 | 2.1645          | 0.2834   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu102
- Datasets 2.7.1
- Tokenizers 0.13.2
