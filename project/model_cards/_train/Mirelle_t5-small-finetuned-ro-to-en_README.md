---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wmt16
metrics:
- bleu
model-index:
- name: t5-small-finetuned-ro-to-en
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: wmt16
      type: wmt16
      args: ro-en
    metrics:
    - name: Bleu
      type: bleu
      value: 13.4499
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-ro-to-en

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the wmt16 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5877
- Bleu: 13.4499
- Gen Len: 17.5073

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|
| 1.6167        | 0.05  | 2000  | 1.8649          | 9.7029  | 17.5753 |
| 1.4551        | 0.1   | 4000  | 1.7810          | 10.6382 | 17.5358 |
| 1.3723        | 0.16  | 6000  | 1.7369          | 11.1285 | 17.5158 |
| 1.3373        | 0.21  | 8000  | 1.7086          | 11.6173 | 17.5013 |
| 1.2935        | 0.26  | 10000 | 1.6890          | 12.0641 | 17.5038 |
| 1.2632        | 0.31  | 12000 | 1.6670          | 12.3012 | 17.5253 |
| 1.2463        | 0.37  | 14000 | 1.6556          | 12.3991 | 17.5153 |
| 1.2272        | 0.42  | 16000 | 1.6442          | 12.7392 | 17.4732 |
| 1.2052        | 0.47  | 18000 | 1.6328          | 12.8446 | 17.5143 |
| 1.1985        | 0.52  | 20000 | 1.6233          | 13.0892 | 17.4807 |
| 1.1821        | 0.58  | 22000 | 1.6153          | 13.1529 | 17.4952 |
| 1.1791        | 0.63  | 24000 | 1.6079          | 13.2964 | 17.5088 |
| 1.1698        | 0.68  | 26000 | 1.6038          | 13.3548 | 17.4842 |
| 1.154         | 0.73  | 28000 | 1.5957          | 13.3012 | 17.5053 |
| 1.1634        | 0.79  | 30000 | 1.5931          | 13.4203 | 17.5083 |
| 1.1487        | 0.84  | 32000 | 1.5893          | 13.3959 | 17.5123 |
| 1.1495        | 0.89  | 34000 | 1.5875          | 13.3745 | 17.4902 |
| 1.1458        | 0.94  | 36000 | 1.5877          | 13.4129 | 17.5043 |
| 1.1465        | 1.0   | 38000 | 1.5877          | 13.4499 | 17.5073 |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.10.0+cu111
- Datasets 1.16.1
- Tokenizers 0.10.3
