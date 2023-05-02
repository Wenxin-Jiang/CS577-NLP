---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: t5-small-finetuned-xsum-finetuned-billsum
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-xsum-finetuned-billsum

This model is a fine-tuned version of [Frederick0291/t5-small-finetuned-xsum](https://huggingface.co/Frederick0291/t5-small-finetuned-xsum) on an unknown dataset.

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

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| No log        | 1.0   | 330  | 1.8540          | 32.9258 | 14.9104 | 27.1067 | 27.208    | 18.8437 |


### Framework versions

- Transformers 4.10.2
- Pytorch 1.9.0+cu102
- Datasets 1.12.1
- Tokenizers 0.10.3
