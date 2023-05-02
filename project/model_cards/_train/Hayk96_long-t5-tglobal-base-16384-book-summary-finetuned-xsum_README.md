---
license: bsd-3-clause
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: long-t5-tglobal-base-16384-book-summary-finetuned-xsum
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# long-t5-tglobal-base-16384-book-summary-finetuned-xsum

This model is a fine-tuned version of [pszemraj/long-t5-tglobal-base-16384-book-summary](https://huggingface.co/pszemraj/long-t5-tglobal-base-16384-book-summary) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.7110
- Rouge1: 19.379
- Rouge2: 2.0125
- Rougel: 12.4318
- Rougelsum: 12.4432
- Gen Len: 72.3611

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.002
- train_batch_size: 3
- eval_batch_size: 3
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 24   | 3.7825          | 18.6153 | 1.7298 | 12.0792 | 12.0714   | 82.3611 |
| No log        | 2.0   | 48   | 3.7110          | 19.379  | 2.0125 | 12.4318 | 12.4432   | 72.3611 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
