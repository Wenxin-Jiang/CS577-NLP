---
license: apache-2.0
tags:
- generated_from_trainer
- summarization
datasets:
- mlsum
language: de
metrics:
- rouge
model-index:
- name: t5-seven-epoch-base-german
  results:
  - task:
      name: Summarization
      type: summarization
    dataset:
      name: mlsum de
      type: mlsum
      args: de
    metrics:
    - name: Rouge1
      type: rouge
      value: 42.3787
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-seven-epoch-base-german

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the mlsum de dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5491
- Rouge1: 42.3787
- Rouge2: 32.0253
- Rougel: 38.9529
- Rougelsum: 40.4544
- Gen Len: 47.7873

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
- train_batch_size: 6
- eval_batch_size: 6
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 7.0

### Training results



### Framework versions

- Transformers 4.16.0.dev0
- Pytorch 1.10.0+cu111
- Datasets 1.17.0
- Tokenizers 0.10.3
