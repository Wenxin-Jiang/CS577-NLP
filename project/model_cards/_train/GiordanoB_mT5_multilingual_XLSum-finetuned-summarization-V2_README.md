---
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: mT5_multilingual_XLSum-finetuned-summarization-V2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mT5_multilingual_XLSum-finetuned-summarization-V2

This model is a fine-tuned version of [csebuetnlp/mT5_multilingual_XLSum](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5523
- Rouge1: 25.8727
- Rouge2: 16.1688
- Rougel: 19.8093
- Rougelsum: 23.4429
- Gen Len: 34.4286

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

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 13   | 1.8850          | 23.9901 | 12.4882 | 17.2823 | 20.8977   | 31.2857 |
| No log        | 2.0   | 26   | 1.5894          | 25.1547 | 14.8857 | 19.2203 | 22.9079   | 31.8571 |
| No log        | 3.0   | 39   | 1.5523          | 25.8727 | 16.1688 | 19.8093 | 23.4429   | 34.4286 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
