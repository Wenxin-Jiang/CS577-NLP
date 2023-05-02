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
- name: xlm-roberta-base-es-base-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-es-base-ner

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2887
- Precision: 0.5703
- Recall: 0.6028
- F1: 0.5861
- Accuracy: 0.9216

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.7989        | 1.0   | 515  | 0.4610          | 0.4365    | 0.3851 | 0.4091 | 0.8867   |
| 0.4088        | 2.0   | 1030 | 0.3468          | 0.5133    | 0.5175 | 0.5154 | 0.9067   |
| 0.3144        | 3.0   | 1545 | 0.3082          | 0.5492    | 0.5532 | 0.5512 | 0.9158   |
| 0.2675        | 4.0   | 2060 | 0.2913          | 0.5627    | 0.5865 | 0.5744 | 0.9216   |
| 0.239         | 5.0   | 2575 | 0.2887          | 0.5703    | 0.6028 | 0.5861 | 0.9216   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
