---
license: mit
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: camembert-base-finetuned-mixte-symbole-dd
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# camembert-base-finetuned-mixte-symbole-dd

This model is a fine-tuned version of [camembert-base](https://huggingface.co/camembert-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3576
- Precision: 0.8788
- Recall: 0.8986
- F1: 0.8886
- Accuracy: 0.9230

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
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1977        | 1.0   | 4322  | 0.2256          | 0.8388    | 0.8980 | 0.8674 | 0.9240   |
| 0.1498        | 2.0   | 8644  | 0.2765          | 0.8666    | 0.8916 | 0.8789 | 0.9235   |
| 0.1085        | 3.0   | 12966 | 0.2945          | 0.8666    | 0.9028 | 0.8844 | 0.9211   |
| 0.0775        | 4.0   | 17288 | 0.3181          | 0.8735    | 0.9015 | 0.8873 | 0.9226   |
| 0.0605        | 5.0   | 21610 | 0.3576          | 0.8788    | 0.8986 | 0.8886 | 0.9230   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
