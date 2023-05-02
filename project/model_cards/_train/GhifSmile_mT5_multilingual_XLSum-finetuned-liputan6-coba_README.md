---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mT5_multilingual_XLSum-finetuned-liputan6-coba
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mT5_multilingual_XLSum-finetuned-liputan6-coba

This model is a fine-tuned version of [csebuetnlp/mT5_multilingual_XLSum](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2713
- Rouge1: 0.3371
- Rouge2: 0.2029
- Rougel: 0.2927
- Rougelsum: 0.309

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adafactor
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:---------:|
| 1.4304        | 1.0   | 4474  | 1.2713          | 0.3371 | 0.2029 | 0.2927 | 0.309     |
| 1.4286        | 2.0   | 8948  | 1.2713          | 0.3371 | 0.2029 | 0.2927 | 0.309     |
| 1.429         | 3.0   | 13422 | 1.2713          | 0.3371 | 0.2029 | 0.2927 | 0.309     |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.2
