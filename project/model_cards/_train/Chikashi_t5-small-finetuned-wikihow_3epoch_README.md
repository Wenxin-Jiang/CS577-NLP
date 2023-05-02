---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wikihow
metrics:
- rouge
model-index:
- name: t5-small-finetuned-wikihow_3epoch
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: wikihow
      type: wikihow
      args: all
    metrics:
    - name: Rouge1
      type: rouge
      value: 25.5784
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-wikihow_3epoch

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the wikihow dataset.
It achieves the following results on the evaluation set:
- Loss: 2.5163
- Rouge1: 25.5784
- Rouge2: 8.9929
- Rougel: 21.5345
- Rougelsum: 24.9382
- Gen Len: 18.384

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
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| 2.9421        | 0.25  | 5000  | 2.6545          | 23.2336 | 7.5502 | 19.5899 | 22.5521   | 18.4076 |
| 2.8411        | 0.51  | 10000 | 2.6103          | 24.3524 | 8.2068 | 20.5238 | 23.6679   | 18.2606 |
| 2.7983        | 0.76  | 15000 | 2.5836          | 24.8169 | 8.4826 | 20.8765 | 24.1686   | 18.3211 |
| 2.7743        | 1.02  | 20000 | 2.5627          | 24.9904 | 8.5625 | 21.0344 | 24.3416   | 18.3786 |
| 2.7452        | 1.27  | 25000 | 2.5508          | 25.1497 | 8.6872 | 21.152  | 24.4751   | 18.3524 |
| 2.7353        | 1.53  | 30000 | 2.5384          | 25.2909 | 8.7408 | 21.2344 | 24.629    | 18.4453 |
| 2.7261        | 1.78  | 35000 | 2.5322          | 25.3748 | 8.7802 | 21.312  | 24.7191   | 18.3754 |
| 2.7266        | 2.03  | 40000 | 2.5265          | 25.4095 | 8.8915 | 21.3871 | 24.7685   | 18.4013 |
| 2.706         | 2.29  | 45000 | 2.5211          | 25.4372 | 8.8926 | 21.4124 | 24.7902   | 18.3776 |
| 2.7073        | 2.54  | 50000 | 2.5176          | 25.4925 | 8.9668 | 21.5103 | 24.8608   | 18.4303 |
| 2.703         | 2.8   | 55000 | 2.5163          | 25.5784 | 8.9929 | 21.5345 | 24.9382   | 18.384  |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
