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
- name: bert-base-chinese-ws-finetuned-ner
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-chinese-ws-finetuned-ner

This model is a fine-tuned version of [ckiplab/bert-base-chinese-ws](https://huggingface.co/ckiplab/bert-base-chinese-ws) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0567
- Precision: 0.9615
- Recall: 0.9630
- F1: 0.9623
- Accuracy: 0.9829

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
- num_epochs: 7

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0475        | 0.64  | 1000  | 0.0506          | 0.9607    | 0.9594 | 0.9600 | 0.9821   |
| 0.0359        | 1.28  | 2000  | 0.0517          | 0.9596    | 0.9615 | 0.9605 | 0.9822   |
| 0.0335        | 1.92  | 3000  | 0.0534          | 0.9550    | 0.9625 | 0.9587 | 0.9814   |
| 0.0258        | 2.56  | 4000  | 0.0547          | 0.9605    | 0.9628 | 0.9616 | 0.9826   |
| 0.0226        | 3.19  | 5000  | 0.0567          | 0.9615    | 0.9630 | 0.9623 | 0.9829   |
| 0.0207        | 3.83  | 6000  | 0.0585          | 0.9594    | 0.9630 | 0.9612 | 0.9824   |
| 0.0161        | 4.47  | 7000  | 0.0663          | 0.9595    | 0.9634 | 0.9615 | 0.9825   |
| 0.0158        | 5.11  | 8000  | 0.0716          | 0.9600    | 0.9625 | 0.9613 | 0.9825   |
| 0.0141        | 5.75  | 9000  | 0.0709          | 0.9597    | 0.9627 | 0.9612 | 0.9824   |
| 0.0117        | 6.39  | 10000 | 0.0744          | 0.9605    | 0.9633 | 0.9619 | 0.9827   |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.8.0+cu111
- Datasets 2.4.0
- Tokenizers 0.10.3
