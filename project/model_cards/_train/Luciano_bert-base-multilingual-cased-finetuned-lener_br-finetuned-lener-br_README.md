---
language:
- pt
license: mit
tags:
- generated_from_trainer
datasets:
- brazilian_court_decisions
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-base-multilingual-cased-finetuned-lener_br-finetuned-lener-br
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: lener_br
      type: lener_br
      config: lener_br
      split: train
      args: lener_br
    metrics:
    - name: Precision
      type: precision
      value: 0
    - name: Recall
      type: recall
      value: 0
    - name: F1
      type: f1
      value: 0
    - name: Accuracy
      type: accuracy
      value: 0
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-multilingual-cased-finetuned-lener_br-finetuned-lener-br

This model is a fine-tuned version of [bert-base-multilingual-cased](https://huggingface.co/bert-base-multilingual-cased) on the lener_br dataset.
It achieves the following results on the evaluation set:
- Loss: nan  (To update)
- Precision: 0.9122  (To update)
- Recall: 0.9163  (To update)
- F1: 0.9142  (To update)
- Accuracy: 0.9826  (To update)

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters (To update) 

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15
- mixed_precision_training: Native AMP

### Training results (To update)

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.068         | 1.0   | 3914  | nan             | 0.6196    | 0.8604 | 0.7204 | 0.9568   |
| 0.0767        | 2.0   | 7828  | nan             | 0.8270    | 0.8710 | 0.8484 | 0.9693   |
| 0.0257        | 3.0   | 11742 | nan             | 0.7243    | 0.9005 | 0.8029 | 0.9639   |
| 0.0193        | 4.0   | 15656 | nan             | 0.9010    | 0.8984 | 0.8997 | 0.9821   |
| 0.0156        | 5.0   | 19570 | nan             | 0.7150    | 0.9121 | 0.8016 | 0.9641   |
| 0.0165        | 6.0   | 23484 | nan             | 0.7640    | 0.8796 | 0.8177 | 0.9691   |
| 0.0225        | 7.0   | 27398 | nan             | 0.8851    | 0.9098 | 0.8973 | 0.9803   |
| 0.016         | 8.0   | 31312 | nan             | 0.9081    | 0.9015 | 0.9048 | 0.9792   |
| 0.0078        | 9.0   | 35226 | nan             | 0.8941    | 0.8863 | 0.8902 | 0.9788   |
| 0.0061        | 10.0  | 39140 | nan             | 0.9026    | 0.9002 | 0.9014 | 0.9804   |
| 0.0057        | 11.0  | 43054 | nan             | 0.8793    | 0.9018 | 0.8904 | 0.9769   |
| 0.0044        | 12.0  | 46968 | nan             | 0.8790    | 0.9033 | 0.8910 | 0.9785   |
| 0.0043        | 13.0  | 50882 | nan             | 0.9122    | 0.9163 | 0.9142 | 0.9826   |
| 0.0003        | 14.0  | 54796 | nan             | 0.9032    | 0.9070 | 0.9051 | 0.9807   |
| 0.0025        | 15.0  | 58710 | nan             | 0.8903    | 0.9085 | 0.8993 | 0.9798   |


### Framework versions (To update)

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
