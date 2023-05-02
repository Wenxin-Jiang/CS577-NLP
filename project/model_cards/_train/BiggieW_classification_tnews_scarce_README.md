---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
widget:
- '全国高校科研质量排名，清华北大浙大无缘前五。'
model-index:
- name: classification_tnews_scarce
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# classification_tnews_scarce

This model is a fine-tuned version of [hfl/chinese-roberta-wwm-ext](https://huggingface.co/hfl/chinese-roberta-wwm-ext) on a very small subset of TNEWS dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0516
- Accuracy: 0.56

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
- train_batch_size: 10
- eval_batch_size: 10
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.7816        | 1.0   | 15   | 2.6553          | 0.1467   |
| 2.4088        | 2.0   | 30   | 2.4761          | 0.36     |
| 2.0481        | 3.0   | 45   | 2.2860          | 0.46     |
| 1.833         | 4.0   | 60   | 2.1598          | 0.5      |
| 1.6642        | 5.0   | 75   | 2.0751          | 0.54     |
| 1.5506        | 6.0   | 90   | 2.0516          | 0.56     |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
