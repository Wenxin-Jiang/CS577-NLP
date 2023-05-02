---
license: mit
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
model-index:
- name: roberta-base-finetuned-ner-agglo-twitter
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-finetuned-ner-agglo-twitter

This model is a fine-tuned version of [ArBert/roberta-base-finetuned-ner](https://huggingface.co/ArBert/roberta-base-finetuned-ner) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6645
- Precision: 0.6885
- Recall: 0.7665
- F1: 0.7254

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|
| No log        | 1.0   | 245  | 0.2820          | 0.6027    | 0.7543 | 0.6700 |
| No log        | 2.0   | 490  | 0.2744          | 0.6308    | 0.7864 | 0.7000 |
| 0.2301        | 3.0   | 735  | 0.2788          | 0.6433    | 0.7637 | 0.6984 |
| 0.2301        | 4.0   | 980  | 0.3255          | 0.6834    | 0.7221 | 0.7022 |
| 0.1153        | 5.0   | 1225 | 0.3453          | 0.6686    | 0.7439 | 0.7043 |
| 0.1153        | 6.0   | 1470 | 0.3988          | 0.6797    | 0.7420 | 0.7094 |
| 0.0617        | 7.0   | 1715 | 0.4711          | 0.6702    | 0.7259 | 0.6969 |
| 0.0617        | 8.0   | 1960 | 0.4904          | 0.6904    | 0.7505 | 0.7192 |
| 0.0328        | 9.0   | 2205 | 0.5088          | 0.6591    | 0.7713 | 0.7108 |
| 0.0328        | 10.0  | 2450 | 0.5709          | 0.6468    | 0.7788 | 0.7067 |
| 0.019         | 11.0  | 2695 | 0.5570          | 0.6642    | 0.7533 | 0.7059 |
| 0.019         | 12.0  | 2940 | 0.5574          | 0.6899    | 0.7656 | 0.7258 |
| 0.0131        | 13.0  | 3185 | 0.5858          | 0.6952    | 0.7609 | 0.7265 |
| 0.0131        | 14.0  | 3430 | 0.6239          | 0.6556    | 0.7826 | 0.7135 |
| 0.0074        | 15.0  | 3675 | 0.5931          | 0.6825    | 0.7599 | 0.7191 |
| 0.0074        | 16.0  | 3920 | 0.6364          | 0.6785    | 0.7580 | 0.7161 |
| 0.005         | 17.0  | 4165 | 0.6437          | 0.6855    | 0.7580 | 0.7199 |
| 0.005         | 18.0  | 4410 | 0.6610          | 0.6779    | 0.7599 | 0.7166 |
| 0.0029        | 19.0  | 4655 | 0.6625          | 0.6853    | 0.7656 | 0.7232 |
| 0.0029        | 20.0  | 4900 | 0.6645          | 0.6885    | 0.7665 | 0.7254 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
