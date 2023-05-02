---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: deberta-v3-large__sst2__train-8-9
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-v3-large__sst2__train-8-9

This model is a fine-tuned version of [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6013
- Accuracy: 0.7210

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 50
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.6757        | 1.0   | 3    | 0.7810          | 0.25     |
| 0.6506        | 2.0   | 6    | 0.8102          | 0.25     |
| 0.6463        | 3.0   | 9    | 0.8313          | 0.25     |
| 0.5813        | 4.0   | 12   | 0.8858          | 0.25     |
| 0.4635        | 5.0   | 15   | 0.8220          | 0.25     |
| 0.3992        | 6.0   | 18   | 0.7226          | 0.5      |
| 0.3281        | 7.0   | 21   | 0.6707          | 0.75     |
| 0.2276        | 8.0   | 24   | 0.7515          | 0.75     |
| 0.1674        | 9.0   | 27   | 0.6971          | 0.75     |
| 0.0873        | 10.0  | 30   | 0.5419          | 0.75     |
| 0.0525        | 11.0  | 33   | 0.5025          | 0.75     |
| 0.0286        | 12.0  | 36   | 0.5229          | 0.75     |
| 0.0149        | 13.0  | 39   | 0.5660          | 0.75     |
| 0.0082        | 14.0  | 42   | 0.6954          | 0.75     |
| 0.006         | 15.0  | 45   | 0.8649          | 0.75     |
| 0.0043        | 16.0  | 48   | 1.0011          | 0.75     |
| 0.0035        | 17.0  | 51   | 1.0909          | 0.75     |
| 0.0021        | 18.0  | 54   | 1.1615          | 0.75     |
| 0.0017        | 19.0  | 57   | 1.2147          | 0.75     |
| 0.0013        | 20.0  | 60   | 1.2585          | 0.75     |
| 0.0016        | 21.0  | 63   | 1.2917          | 0.75     |


### Framework versions

- Transformers 4.15.0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.10.3
