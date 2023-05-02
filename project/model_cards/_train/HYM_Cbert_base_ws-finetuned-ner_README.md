---
license: gpl-3.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: Cbert_base_ws-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Cbert_base_ws-finetuned-ner

This model is a fine-tuned version of [ckiplab/bert-base-chinese-ws](https://huggingface.co/ckiplab/bert-base-chinese-ws) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0582
- Precision: 0.9602
- Recall: 0.9633
- F1: 0.9617
- Accuracy: 0.9827

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
- train_batch_size: 18
- eval_batch_size: 18
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0482        | 0.64  | 1000  | 0.0509          | 0.9601    | 0.9582 | 0.9592 | 0.9817   |
| 0.0364        | 1.28  | 2000  | 0.0521          | 0.9590    | 0.9615 | 0.9602 | 0.9820   |
| 0.0341        | 1.92  | 3000  | 0.0548          | 0.9546    | 0.9625 | 0.9585 | 0.9812   |
| 0.0264        | 2.56  | 4000  | 0.0550          | 0.9593    | 0.9623 | 0.9608 | 0.9822   |
| 0.0227        | 3.19  | 5000  | 0.0582          | 0.9602    | 0.9633 | 0.9617 | 0.9827   |
| 0.021         | 3.83  | 6000  | 0.0595          | 0.9581    | 0.9624 | 0.9603 | 0.9820   |
| 0.0162        | 4.47  | 7000  | 0.0686          | 0.9574    | 0.9626 | 0.9600 | 0.9819   |
| 0.0159        | 5.11  | 8000  | 0.0719          | 0.9596    | 0.9614 | 0.9605 | 0.9822   |
| 0.0144        | 5.75  | 9000  | 0.0732          | 0.9590    | 0.9620 | 0.9605 | 0.9822   |
| 0.0109        | 6.39  | 10000 | 0.0782          | 0.9599    | 0.9626 | 0.9612 | 0.9824   |
| 0.0122        | 7.03  | 11000 | 0.0803          | 0.9605    | 0.9620 | 0.9612 | 0.9825   |
| 0.0097        | 7.67  | 12000 | 0.0860          | 0.9591    | 0.9620 | 0.9605 | 0.9822   |
| 0.0087        | 8.31  | 13000 | 0.0877          | 0.9591    | 0.9616 | 0.9603 | 0.9821   |
| 0.0087        | 8.95  | 14000 | 0.0902          | 0.9585    | 0.9630 | 0.9607 | 0.9823   |
| 0.0078        | 9.58  | 15000 | 0.0929          | 0.9589    | 0.9621 | 0.9605 | 0.9821   |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.8.0+cu111
- Datasets 2.4.0
- Tokenizers 0.10.3
