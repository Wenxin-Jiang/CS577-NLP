---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- samsum
metrics:
- rouge
model-index:
- name: tst-summarization
  results:
  - task:
      name: Summarization
      type: summarization
    dataset:
      name: samsum
      type: samsum
      config: samsum
      split: train
      args: samsum
    metrics:
    - name: Rouge1
      type: rouge
      value: 44.9509
---


# tst-summarization

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the samsum dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6972
- Rouge1: 44.9509
- Rouge2: 21.7162
- Rougel: 37.7582
- Rougelsum: 41.7239
- Gen Len: 22.7714

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results



### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cpu
- Datasets 2.8.0
- Tokenizers 0.13.2
