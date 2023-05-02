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
- name: bert-base-chinese-ws-finetuned-ner_all
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-chinese-ws-finetuned-ner_all

This model is a fine-tuned version of [ckiplab/bert-base-chinese-ws](https://huggingface.co/ckiplab/bert-base-chinese-ws) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0330
- Precision: 0.9723
- Recall: 0.9734
- F1: 0.9728
- Accuracy: 0.9879

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
- train_batch_size: 18
- eval_batch_size: 18
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0648        | 0.29  | 500  | 0.0524          | 0.9586    | 0.9572 | 0.9579 | 0.9813   |
| 0.0509        | 0.59  | 1000 | 0.0460          | 0.9615    | 0.9628 | 0.9622 | 0.9832   |
| 0.0478        | 0.88  | 1500 | 0.0429          | 0.9624    | 0.9660 | 0.9642 | 0.9840   |
| 0.0417        | 1.17  | 2000 | 0.0409          | 0.9650    | 0.9680 | 0.9665 | 0.9851   |
| 0.0402        | 1.47  | 2500 | 0.0387          | 0.9662    | 0.9693 | 0.9677 | 0.9856   |
| 0.0378        | 1.76  | 3000 | 0.0359          | 0.9699    | 0.9717 | 0.9708 | 0.9869   |
| 0.0385        | 2.05  | 3500 | 0.0353          | 0.9703    | 0.9718 | 0.9710 | 0.9871   |
| 0.0337        | 2.34  | 4000 | 0.0341          | 0.9709    | 0.9731 | 0.9720 | 0.9875   |
| 0.0348        | 2.64  | 4500 | 0.0333          | 0.9721    | 0.9733 | 0.9727 | 0.9878   |
| 0.0346        | 2.93  | 5000 | 0.0331          | 0.9722    | 0.9735 | 0.9729 | 0.9879   |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.8.0+cu111
- Datasets 2.4.0
- Tokenizers 0.10.3
