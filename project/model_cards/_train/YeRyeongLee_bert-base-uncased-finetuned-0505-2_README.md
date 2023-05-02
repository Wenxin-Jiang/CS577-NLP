---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-base-uncased-finetuned-0505-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-0505-2

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4277
- Accuracy: 0.9206
- F1: 0.9205

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
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| No log        | 1.0   | 1373 | 0.3634          | 0.9025   | 0.9012 |
| No log        | 2.0   | 2746 | 0.3648          | 0.9066   | 0.9060 |
| No log        | 3.0   | 4119 | 0.3978          | 0.9189   | 0.9183 |
| No log        | 4.0   | 5492 | 0.4277          | 0.9206   | 0.9205 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0
- Datasets 1.16.1
- Tokenizers 0.10.3
