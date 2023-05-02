---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wikihow
metrics:
- rouge
model-index:
- name: t5-small-finetuned-wikihow_3epoch_b8_lr3e-3
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
      value: 27.1711
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-wikihow_3epoch_b8_lr3e-3

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the wikihow dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3163
- Rouge1: 27.1711
- Rouge2: 10.6296
- Rougel: 23.206
- Rougelsum: 26.4801
- Gen Len: 18.5433

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.003
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 3.0734        | 0.25  | 5000  | 2.7884          | 22.4825 | 7.2492  | 19.243  | 21.9167   | 18.0616 |
| 2.9201        | 0.51  | 10000 | 2.7089          | 24.0869 | 8.0348  | 20.4814 | 23.4541   | 18.5994 |
| 2.8403        | 0.76  | 15000 | 2.6390          | 24.62   | 8.3776  | 20.8736 | 23.9784   | 18.4676 |
| 2.7764        | 1.02  | 20000 | 2.5943          | 24.1504 | 8.3933  | 20.8271 | 23.5382   | 18.4078 |
| 2.6641        | 1.27  | 25000 | 2.5428          | 25.6574 | 9.2371  | 21.8576 | 24.9558   | 18.4249 |
| 2.6369        | 1.53  | 30000 | 2.5042          | 25.5208 | 9.254   | 21.6673 | 24.8589   | 18.6467 |
| 2.6           | 1.78  | 35000 | 2.4637          | 26.094  | 9.7003  | 22.3097 | 25.4695   | 18.5065 |
| 2.5562        | 2.03  | 40000 | 2.4285          | 26.5374 | 9.9222  | 22.5291 | 25.8836   | 18.5553 |
| 2.4322        | 2.29  | 45000 | 2.3858          | 26.939  | 10.3555 | 23.0211 | 26.2834   | 18.5614 |
| 2.4106        | 2.54  | 50000 | 2.3537          | 26.7423 | 10.2816 | 22.7986 | 26.083    | 18.5792 |
| 2.3731        | 2.8   | 55000 | 2.3163          | 27.1711 | 10.6296 | 23.206  | 26.4801   | 18.5433 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
