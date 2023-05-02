---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
  name: bert-base-uncased-finetuned-semeval2020-task4b-append-e3-b32-l4e5
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-semeval2020-task4b-append-e3-b32-l4e5

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5121
- Accuracy: 0.8700

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 344  | 0.3603          | 0.8550   |
| 0.3894        | 2.0   | 688  | 0.4011          | 0.8630   |
| 0.1088        | 3.0   | 1032 | 0.5121          | 0.8700   |


### Framework versions

- Transformers 4.12.3
- Pytorch 1.9.1
- Datasets 1.12.1
- Tokenizers 0.10.3
