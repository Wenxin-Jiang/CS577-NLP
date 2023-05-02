---
language:
- pt
license: mit
tags:
- generated_from_trainer
datasets:
- lener_br
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: xlm-roberta-base-finetuned-lener-br
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
      value: 0.844312854675549
    - name: Recall
      type: recall
      value: 0.8844662703540966
    - name: F1
      type: f1
      value: 0.8639232517041151
    - name: Accuracy
      type: accuracy
      value: 0.97516697297055
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-finetuned-lener-br

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the lener_br dataset.
It achieves the following results on the evaluation set:
- Loss: nan
- Precision: 0.8443
- Recall: 0.8845
- F1: 0.8639
- Accuracy: 0.9752

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0832        | 1.0   | 1957  | nan             | 0.6752    | 0.8625 | 0.7575 | 0.9578   |
| 0.0477        | 2.0   | 3914  | nan             | 0.8391    | 0.8839 | 0.8609 | 0.9704   |
| 0.029         | 3.0   | 5871  | nan             | 0.7530    | 0.9059 | 0.8224 | 0.9648   |
| 0.0223        | 4.0   | 7828  | nan             | 0.7488    | 0.8744 | 0.8067 | 0.9659   |
| 0.0234        | 5.0   | 9785  | nan             | 0.7216    | 0.8783 | 0.7923 | 0.9644   |
| 0.0171        | 6.0   | 11742 | nan             | 0.7072    | 0.8969 | 0.7908 | 0.9642   |
| 0.0121        | 7.0   | 13699 | nan             | 0.7769    | 0.8775 | 0.8241 | 0.9681   |
| 0.0093        | 8.0   | 15656 | nan             | 0.7218    | 0.8772 | 0.7920 | 0.9621   |
| 0.0074        | 9.0   | 17613 | nan             | 0.8241    | 0.8767 | 0.8496 | 0.9739   |
| 0.0055        | 10.0  | 19570 | nan             | 0.7369    | 0.8801 | 0.8021 | 0.9638   |
| 0.0055        | 11.0  | 21527 | nan             | 0.8443    | 0.8845 | 0.8639 | 0.9752   |
| 0.0029        | 12.0  | 23484 | nan             | 0.8338    | 0.8935 | 0.8626 | 0.9753   |
| 0.0026        | 13.0  | 25441 | nan             | 0.7721    | 0.8992 | 0.8308 | 0.9694   |
| 0.004         | 14.0  | 27398 | nan             | 0.7466    | 0.8886 | 0.8114 | 0.9672   |
| 0.0006        | 15.0  | 29355 | nan             | 0.7518    | 0.8995 | 0.8190 | 0.9686   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
