---
license: mit
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: bart-large-cnn-finetuned-xsum
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-large-cnn-finetuned-xsum

This model is a fine-tuned version of [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 3.7973
- Rouge1: 24.5661
- Rouge2: 8.6188
- Rougel: 17.1387
- Rougelsum: 18.869
- Gen Len: 73.1667

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-08
- train_batch_size: 3
- eval_batch_size: 3
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 24   | 3.7983          | 24.5842 | 8.6062 | 17.0846 | 18.8412   | 73.3472 |
| No log        | 2.0   | 48   | 3.7973          | 24.5661 | 8.6188 | 17.1387 | 18.869    | 73.1667 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
