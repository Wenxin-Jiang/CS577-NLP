---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- cnn_dailymail
metrics:
- rouge
model-index:
- name: t5-small-finetuned-cnndm1
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: cnn_dailymail
      type: cnn_dailymail
      args: 3.0.0
    metrics:
    - name: Rouge1
      type: rouge
      value: 24.4246
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-cnndm1

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the cnn_dailymail dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6853
- Rouge1: 24.4246
- Rouge2: 11.6944
- Rougel: 20.1717
- Rougelsum: 23.0424
- Gen Len: 18.9996

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
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 1.912         | 0.14  | 5000  | 1.7167          | 24.4232 | 11.7049 | 20.1758 | 23.0345   | 18.9997 |
| 1.8784        | 0.28  | 10000 | 1.7018          | 24.4009 | 11.6918 | 20.1561 | 23.0073   | 18.9997 |
| 1.8628        | 0.42  | 15000 | 1.6934          | 24.385  | 11.683  | 20.1285 | 22.9823   | 18.9997 |
| 1.8594        | 0.56  | 20000 | 1.6902          | 24.4407 | 11.6835 | 20.1734 | 23.0369   | 18.9996 |
| 1.8537        | 0.7   | 25000 | 1.6864          | 24.3635 | 11.658  | 20.1318 | 22.9782   | 18.9993 |
| 1.8505        | 0.84  | 30000 | 1.6856          | 24.4267 | 11.6991 | 20.1629 | 23.0361   | 18.9994 |
| 1.8505        | 0.98  | 35000 | 1.6853          | 24.4246 | 11.6944 | 20.1717 | 23.0424   | 18.9996 |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
