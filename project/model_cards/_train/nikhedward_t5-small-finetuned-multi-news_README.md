---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- multi_news
metrics:
- rouge
model-index:
- name: t5-small-finetuned-multi-news
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: multi_news
      type: multi_news
      args: default
    metrics:
    - name: Rouge1
      type: rouge
      value: 14.5549
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-multi-news

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the multi_news dataset.
It achieves the following results on the evaluation set:
- Loss: 2.7775
- Rouge1: 14.5549
- Rouge2: 4.5934
- Rougel: 11.1178
- Rougelsum: 12.8964
- Gen Len: 19.0

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
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| 3.0211        | 1.0   | 1405 | 2.7775          | 14.5549 | 4.5934 | 11.1178 | 12.8964   | 19.0    |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
