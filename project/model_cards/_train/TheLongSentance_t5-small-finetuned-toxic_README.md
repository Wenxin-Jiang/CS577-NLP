---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model_index:
- name: t5-small-finetuned-toxic
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    metric:
      name: Rouge1
      type: rouge
      value: 93.7659
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-toxic

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on an unkown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1295
- Rouge1: 93.7659
- Rouge2: 3.6618
- Rougel: 93.7652
- Rougelsum: 93.7757
- Gen Len: 2.5481

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
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| 0.1595        | 1.0   | 7979 | 0.1295          | 93.7659 | 3.6618 | 93.7652 | 93.7757   | 2.5481  |


### Framework versions

- Transformers 4.9.1
- Pytorch 1.9.0+cu102
- Datasets 1.11.0
- Tokenizers 0.10.3
