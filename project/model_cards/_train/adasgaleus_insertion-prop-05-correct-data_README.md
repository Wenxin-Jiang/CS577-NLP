---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: insertion-prop-05-correct-data
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# insertion-prop-05-correct-data

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0794
- Precision: 0.9284
- Recall: 0.9056
- F1: 0.9169
- Accuracy: 0.9689

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
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1815        | 0.32  | 500  | 0.0982          | 0.9159    | 0.8802 | 0.8977 | 0.9619   |
| 0.1113        | 0.64  | 1000 | 0.0833          | 0.9257    | 0.9018 | 0.9136 | 0.9676   |
| 0.1018        | 0.96  | 1500 | 0.0794          | 0.9284    | 0.9056 | 0.9169 | 0.9689   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
