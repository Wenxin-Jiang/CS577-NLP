---
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: mental-bert-base-uncased-masked_finetuned-0517
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mental-bert-base-uncased-masked_finetuned-0517

This model is a fine-tuned version of [mental/mental-bert-base-uncased](https://huggingface.co/mental/mental-bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5217
- Accuracy: 0.917
- F1: 0.9171

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

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|
| No log        | 1.0   | 3000  | 0.2922          | 0.8993   | 0.8997 |
| No log        | 2.0   | 6000  | 0.3964          | 0.9063   | 0.9069 |
| No log        | 3.0   | 9000  | 0.4456          | 0.9197   | 0.9197 |
| No log        | 4.0   | 12000 | 0.5217          | 0.917    | 0.9171 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0
- Datasets 1.16.1
- Tokenizers 0.10.3
