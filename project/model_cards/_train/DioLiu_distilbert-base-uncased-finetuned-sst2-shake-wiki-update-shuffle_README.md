---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased-finetuned-sst2-shake-wiki-update-shuffle
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-finetuned-sst2-shake-wiki-update-shuffle

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0284
- Accuracy: 0.9971

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

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.0166        | 1.0   | 7783  | 0.0135          | 0.9965   |
| 0.0091        | 2.0   | 15566 | 0.0172          | 0.9968   |
| 0.0059        | 3.0   | 23349 | 0.0223          | 0.9968   |
| 0.0           | 4.0   | 31132 | 0.0332          | 0.9962   |
| 0.0001        | 5.0   | 38915 | 0.0284          | 0.9971   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0+cu113
- Datasets 2.2.1
- Tokenizers 0.12.1
