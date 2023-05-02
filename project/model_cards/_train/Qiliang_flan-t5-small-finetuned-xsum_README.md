---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- xsum
metrics:
- rouge
model-index:
- name: flan-t5-small-finetuned-xsum
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: xsum
      type: xsum
      config: default
      split: train
      args: default
    metrics:
    - name: Rouge1
      type: rouge
      value: 26.422
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# flan-t5-small-finetuned-xsum

This model is a fine-tuned version of [google/flan-t5-small](https://huggingface.co/google/flan-t5-small) on the xsum dataset.
It achieves the following results on the evaluation set:
- Loss: nan
- Rouge1: 26.422
- Rouge2: 7.2028
- Rougel: 21.006
- Rougelsum: 21.0068
- Gen Len: 18.5694

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
- train_batch_size: 12
- eval_batch_size: 12
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:---------:|:-------:|
| 0.0           | 1.0   | 17004 | nan             | 26.422 | 7.2028 | 21.006 | 21.0068   | 18.5694 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1
- Datasets 2.6.1
- Tokenizers 0.13.1
