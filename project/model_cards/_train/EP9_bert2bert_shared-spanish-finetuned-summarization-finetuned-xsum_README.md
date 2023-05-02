---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bert2bert_shared-spanish-finetuned-summarization-finetuned-xsum
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert2bert_shared-spanish-finetuned-summarization-finetuned-xsum

This model is a fine-tuned version of [mrm8488/bert2bert_shared-spanish-finetuned-summarization](https://huggingface.co/mrm8488/bert2bert_shared-spanish-finetuned-summarization) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3690
- Rouge1: 50.02
- Rouge2: 35.706
- Rougel: 46.6253
- Rougelsum: 46.6412
- Gen Len: 22.1176

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
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 2.5969        | 1.0   | 3090 | 2.4559          | 49.4282 | 35.2705 | 46.095  | 46.0994   | 22.5422 |
| 2.3318        | 2.0   | 6180 | 2.3690          | 50.02   | 35.706  | 46.6253 | 46.6412   | 22.1176 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.0
- Tokenizers 0.13.2
