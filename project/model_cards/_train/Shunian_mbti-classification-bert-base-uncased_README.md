---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: mbti-classification-bert-base-uncased
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mbti-classification-bert-base-uncased

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3272
- Accuracy: 0.2924

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
- train_batch_size: 24
- eval_batch_size: 24
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Accuracy | Validation Loss |
|:-------------:|:-----:|:-----:|:--------:|:---------------:|
| 2.0851        | 1.0   | 13660 | 0.3052   | 2.0650          |
| 1.9902        | 2.0   | 27320 | 0.3105   | 2.0524          |
| 1.8139        | 3.0   | 40980 | 0.3029   | 2.1081          |
| 1.6191        | 4.0   | 54640 | 2.2604   | 0.2964          |
| 1.4893        | 5.0   | 68300 | 2.3272   | 0.2924          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu102
- Datasets 2.7.1
- Tokenizers 0.13.2
