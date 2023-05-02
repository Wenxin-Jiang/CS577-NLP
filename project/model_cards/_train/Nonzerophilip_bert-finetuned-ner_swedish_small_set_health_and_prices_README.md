---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-finetuned-ner_swedish_small_set_health_and_prices
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-ner_swedish_small_set_health_and_prices

This model is a fine-tuned version of [KBLab/bert-base-swedish-cased-ner](https://huggingface.co/KBLab/bert-base-swedish-cased-ner) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0942
- Precision: 0.7709
- Recall: 0.8118
- F1: 0.7908
- Accuracy: 0.9741

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 250  | 0.1310          | 0.6116    | 0.7471 | 0.6726 | 0.9578   |
| 0.1583        | 2.0   | 500  | 0.0939          | 0.7560    | 0.8020 | 0.7783 | 0.9737   |
| 0.1583        | 3.0   | 750  | 0.0942          | 0.7709    | 0.8118 | 0.7908 | 0.9741   |


### Framework versions

- Transformers 4.19.3
- Pytorch 1.7.1
- Datasets 2.2.2
- Tokenizers 0.12.1
