---
license: apache-2.0
tags:
- translation
- generated_from_trainer
metrics:
- bleu
model-index:
- name: model-translate-en-to-ar-from-320k-dataset-ar-en-th2301191458
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# model-translate-en-to-ar-from-320k-dataset-ar-en-th2301191458

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-en-ar](https://huggingface.co/Helsinki-NLP/opus-mt-en-ar) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8107
- Bleu: 21.4462

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
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Bleu    |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|
| 2.0862        | 1.0   | 18750 | 1.8506          | 20.8253 |
| 1.9858        | 2.0   | 37500 | 1.8207          | 21.2835 |
| 1.9098        | 3.0   | 56250 | 1.8107          | 21.4462 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
