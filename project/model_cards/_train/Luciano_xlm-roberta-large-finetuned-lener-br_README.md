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
- name: xlm-roberta-large-finetuned-lener-br
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
      value: 0.8762313715584744
    - name: Recall
      type: recall
      value: 0.8966141121736882
    - name: F1
      type: f1
      value: 0.8863055697496168
    - name: Accuracy
      type: accuracy
      value: 0.979500052295785
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-large-finetuned-lener-br

This model is a fine-tuned version of [xlm-roberta-large](https://huggingface.co/xlm-roberta-large) on the lener_br dataset.
It achieves the following results on the evaluation set:
- Loss: nan
- Precision: 0.8762
- Recall: 0.8966
- F1: 0.8863
- Accuracy: 0.9795

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0785        | 1.0   | 3914  | nan             | 0.7119    | 0.8410 | 0.7711 | 0.9658   |
| 0.076         | 2.0   | 7828  | nan             | 0.8397    | 0.8679 | 0.8536 | 0.9740   |
| 0.0434        | 3.0   | 11742 | nan             | 0.8545    | 0.8666 | 0.8605 | 0.9693   |
| 0.022         | 4.0   | 15656 | nan             | 0.8293    | 0.8573 | 0.8431 | 0.9652   |
| 0.0284        | 5.0   | 19570 | nan             | 0.8789    | 0.8571 | 0.8678 | 0.9776   |
| 0.029         | 6.0   | 23484 | nan             | 0.8521    | 0.8788 | 0.8653 | 0.9771   |
| 0.0227        | 7.0   | 27398 | nan             | 0.7648    | 0.8873 | 0.8215 | 0.9686   |
| 0.0219        | 8.0   | 31312 | nan             | 0.8609    | 0.9026 | 0.8813 | 0.9780   |
| 0.0121        | 9.0   | 35226 | nan             | 0.8746    | 0.8979 | 0.8861 | 0.9812   |
| 0.0087        | 10.0  | 39140 | nan             | 0.8829    | 0.8827 | 0.8828 | 0.9808   |
| 0.0081        | 11.0  | 43054 | nan             | 0.8740    | 0.8749 | 0.8745 | 0.9765   |
| 0.0058        | 12.0  | 46968 | nan             | 0.8838    | 0.8842 | 0.8840 | 0.9788   |
| 0.0044        | 13.0  | 50882 | nan             | 0.869     | 0.8984 | 0.8835 | 0.9788   |
| 0.002         | 14.0  | 54796 | nan             | 0.8762    | 0.8966 | 0.8863 | 0.9795   |
| 0.0017        | 15.0  | 58710 | nan             | 0.8729    | 0.8982 | 0.8854 | 0.9791   |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
