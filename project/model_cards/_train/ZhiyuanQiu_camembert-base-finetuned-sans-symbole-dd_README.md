---
license: mit
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: camembert-base-finetuned-sans-symbole-dd
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# camembert-base-finetuned-sans-symbole-dd

This model is a fine-tuned version of [camembert-base](https://huggingface.co/camembert-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2642
- Precision: 0.8856
- Recall: 0.9176
- F1: 0.9013
- Accuracy: 0.9364

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
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1961        | 1.0   | 4317  | 0.2216          | 0.8675    | 0.9039 | 0.8853 | 0.9319   |
| 0.161         | 2.0   | 8634  | 0.2243          | 0.8614    | 0.9158 | 0.8878 | 0.9237   |
| 0.1169        | 3.0   | 12951 | 0.2507          | 0.8752    | 0.9154 | 0.8949 | 0.9329   |
| 0.0875        | 4.0   | 17268 | 0.2642          | 0.8856    | 0.9176 | 0.9013 | 0.9364   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
