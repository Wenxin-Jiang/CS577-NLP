---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- wikihow
metrics:
- rouge
model-index:
- name: t5-small-finetuned-cnndm3-wikihow3
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: wikihow
      type: wikihow
      args: all
    metrics:
    - name: Rouge1
      type: rouge
      value: 27.2654
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-cnndm3-wikihow3

This model is a fine-tuned version of [Chikashi/t5-small-finetuned-cnndm3-wikihow2](https://huggingface.co/Chikashi/t5-small-finetuned-cnndm3-wikihow2) on the wikihow dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3138
- Rouge1: 27.2654
- Rouge2: 10.5461
- Rougel: 23.2451
- Rougelsum: 26.6151
- Gen Len: 18.5263

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 2.5019        | 1.0   | 39313 | 2.3138          | 27.2654 | 10.5461 | 23.2451 | 26.6151   | 18.5263 |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.0+cu111
- Datasets 2.1.0
- Tokenizers 0.12.1
