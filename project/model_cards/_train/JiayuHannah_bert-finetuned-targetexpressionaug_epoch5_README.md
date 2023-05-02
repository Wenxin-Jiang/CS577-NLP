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
- name: bert-finetuned-targetexpressionaug_epoch5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-targetexpressionaug_epoch5

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2460
- Precision: 0.6388
- Recall: 0.6574
- F1: 0.6480
- Accuracy: 0.7685

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
| No log        | 1.0   | 424  | 0.9757          | 0.5661    | 0.6406 | 0.6010 | 0.7455   |
| 0.2463        | 2.0   | 848  | 1.0356          | 0.6151    | 0.6350 | 0.6249 | 0.7656   |
| 0.1394        | 3.0   | 1272 | 1.0995          | 0.6246    | 0.6406 | 0.6325 | 0.7634   |
| 0.1155        | 4.0   | 1696 | 1.1802          | 0.6331    | 0.6529 | 0.6429 | 0.7673   |
| 0.0768        | 5.0   | 2120 | 1.2460          | 0.6388    | 0.6574 | 0.6480 | 0.7685   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.0
- Tokenizers 0.13.2
