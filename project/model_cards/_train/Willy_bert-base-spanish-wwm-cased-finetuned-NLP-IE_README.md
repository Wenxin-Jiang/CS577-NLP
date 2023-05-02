---
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-base-spanish-wwm-cased-finetuned-NLP-IE
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-spanish-wwm-cased-finetuned-NLP-IE

This model is a fine-tuned version of [dccuchile/bert-base-spanish-wwm-cased](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6260
- Accuracy: 0.7015

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.6052        | 1.0   | 9    | 0.6370          | 0.7015   |
| 0.5501        | 2.0   | 18   | 0.6260          | 0.7015   |


### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
