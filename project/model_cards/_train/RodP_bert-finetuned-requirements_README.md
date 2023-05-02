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
- name: bert-finetuned-requirements
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-requirements

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0538
- Precision: 0.9609
- Recall: 0.9609
- F1: 0.9609
- Accuracy: 0.9822

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 33   | 0.1992          | 0.8903    | 0.8880 | 0.8892 | 0.9476   |
| No log        | 2.0   | 66   | 0.1351          | 0.9039    | 0.9062 | 0.9051 | 0.9554   |
| No log        | 3.0   | 99   | 0.0949          | 0.9368    | 0.9271 | 0.9319 | 0.9677   |
| No log        | 4.0   | 132  | 0.0613          | 0.9556    | 0.9531 | 0.9544 | 0.9788   |
| No log        | 5.0   | 165  | 0.0538          | 0.9609    | 0.9609 | 0.9609 | 0.9822   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
