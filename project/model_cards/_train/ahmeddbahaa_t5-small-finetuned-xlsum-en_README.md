---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
datasets:
- xlsum
metrics:
- rouge
model-index:
- name: t5-small-finetuned-xlsum-en
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: xlsum
      type: xlsum
      args: english
    metrics:
    - name: Rouge1
      type: rouge
      value: 23.7508
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-xlsum-en

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the xlsum dataset.
It achieves the following results on the evaluation set:
- Loss: 2.6629
- Rouge1: 23.7508
- Rouge2: 5.5427
- Rougel: 18.6777
- Rougelsum: 18.652

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 3
- eval_batch_size: 3
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|
| 3.0789        | 1.0   | 1010 | 2.6881          | 22.6824 | 4.4735 | 17.6707 | 17.5485   |
| 2.9223        | 2.0   | 2020 | 2.6629          | 23.7508 | 5.5427 | 18.6777 | 18.652    |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6
