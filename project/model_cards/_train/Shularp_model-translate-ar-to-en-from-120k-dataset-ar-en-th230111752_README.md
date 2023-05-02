---
license: apache-2.0
tags:
- translation
- generated_from_trainer
metrics:
- bleu
model-index:
- name: model-translate-ar-to-en-from-120k-dataset-ar-en-th230111752
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# model-translate-ar-to-en-from-120k-dataset-ar-en-th230111752

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-ar-en](https://huggingface.co/Helsinki-NLP/opus-mt-ar-en) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2879
- Bleu: 36.3711

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Bleu    |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|
| 1.3225        | 1.0   | 12500 | 1.3048          | 35.6396 |
| 1.0963        | 2.0   | 25000 | 1.2906          | 36.2535 |
| 1.1074        | 3.0   | 37500 | 1.2879          | 36.3711 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
