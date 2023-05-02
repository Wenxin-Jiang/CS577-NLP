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
- name: bert-finetuned-ner2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner2

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0015
- Precision: 0.9709
- Recall: 0.9904
- F1: 0.9806
- Accuracy: 0.9995

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
| No log        | 1.0   | 108  | 0.0035          | 0.9565    | 0.9876 | 0.9718 | 0.9990   |
| No log        | 2.0   | 216  | 0.0019          | 0.9628    | 0.9904 | 0.9764 | 0.9994   |
| No log        | 3.0   | 324  | 0.0016          | 0.9764    | 0.9904 | 0.9834 | 0.9995   |
| No log        | 4.0   | 432  | 0.0017          | 0.9736    | 0.9866 | 0.9801 | 0.9995   |
| 0.0166        | 5.0   | 540  | 0.0015          | 0.9709    | 0.9904 | 0.9806 | 0.9995   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.2
