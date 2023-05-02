---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- accuracy
- f1
model-index:
- name: DistilRoberta
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DistilRoberta

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1246
- Precision: 0.9633
- Accuracy: 0.9697
- F1: 0.9705

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:--------:|:------:|
| 0.5894        | 0.4   | 500  | 0.4710          | 0.8381    | 0.7747   | 0.7584 |
| 0.3863        | 0.8   | 1000 | 0.3000          | 0.8226    | 0.8737   | 0.8858 |
| 0.2272        | 1.2   | 1500 | 0.1973          | 0.9593    | 0.9333   | 0.9329 |
| 0.1639        | 1.6   | 2000 | 0.1694          | 0.9067    | 0.9367   | 0.9403 |
| 0.1263        | 2.0   | 2500 | 0.1128          | 0.9657    | 0.9597   | 0.9603 |
| 0.0753        | 2.4   | 3000 | 0.1305          | 0.9614    | 0.967    | 0.9679 |
| 0.0619        | 2.8   | 3500 | 0.1246          | 0.9633    | 0.9697   | 0.9705 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
