---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: AgitationTextV1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# AgitationTextV1

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5634
- Accuracy: 0.84
- Precision: 0.9054
- Recall: 0.8816
- F1: 0.8933

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.558         | 1.0   | 50   | 0.5387          | 0.75     | 0.9048    | 0.75   | 0.8201 |
| 0.4431        | 2.0   | 100  | 0.4989          | 0.75     | 0.9474    | 0.7105 | 0.8120 |
| 0.3334        | 3.0   | 150  | 0.4703          | 0.79     | 0.9661    | 0.75   | 0.8444 |
| 0.2601        | 4.0   | 200  | 0.4391          | 0.85     | 0.9420    | 0.8553 | 0.8966 |
| 0.2081        | 5.0   | 250  | 0.4560          | 0.84     | 0.9167    | 0.8684 | 0.8919 |
| 0.1655        | 6.0   | 300  | 0.5424          | 0.84     | 0.8947    | 0.8947 | 0.8947 |
| 0.1427        | 7.0   | 350  | 0.4977          | 0.84     | 0.9286    | 0.8553 | 0.8904 |
| 0.1237        | 8.0   | 400  | 0.5642          | 0.85     | 0.9067    | 0.8947 | 0.9007 |
| 0.1122        | 9.0   | 450  | 0.6052          | 0.85     | 0.9067    | 0.8947 | 0.9007 |
| 0.0962        | 10.0  | 500  | 0.5634          | 0.84     | 0.9054    | 0.8816 | 0.8933 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
