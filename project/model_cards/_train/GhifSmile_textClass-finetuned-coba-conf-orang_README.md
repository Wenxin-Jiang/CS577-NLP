---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: textClass-finetuned-coba-conf-orang
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# textClass-finetuned-coba-conf-orang

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4868
- Accuracy: 0.7856

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.5108        | 1.0   | 2757  | 0.4652          | 0.7761   |
| 0.4484        | 2.0   | 5514  | 0.4447          | 0.7881   |
| 0.4031        | 3.0   | 8271  | 0.4552          | 0.7891   |
| 0.3646        | 4.0   | 11028 | 0.4720          | 0.7911   |
| 0.3372        | 5.0   | 13785 | 0.4868          | 0.7856   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
