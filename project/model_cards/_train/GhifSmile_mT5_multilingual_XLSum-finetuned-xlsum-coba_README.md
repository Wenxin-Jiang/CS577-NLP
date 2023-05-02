---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mT5_multilingual_XLSum-finetuned-xlsum-coba
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mT5_multilingual_XLSum-finetuned-xlsum-coba

This model is a fine-tuned version of [csebuetnlp/mT5_multilingual_XLSum](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2369
- Rouge1: 0.3744
- Rouge2: 0.1718
- Rougel: 0.3092
- Rougelsum: 0.3106

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.00056
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:---------:|
| 1.6963        | 1.0   | 7648  | 1.2369          | 0.3744 | 0.1718 | 0.3092 | 0.3106    |
| 1.6975        | 2.0   | 15296 | 1.2369          | 0.3744 | 0.1718 | 0.3092 | 0.3106    |
| 1.6969        | 3.0   | 22944 | 1.2369          | 0.3744 | 0.1718 | 0.3092 | 0.3106    |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
