---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- eli5
metrics:
- rouge
model-index:
- name: t5-small-finetuned-eli5
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: eli5
      type: eli5
      config: LFQA_reddit
      split: train_eli5
      args: LFQA_reddit
    metrics:
    - name: Rouge1
      type: rouge
      value: 11.8922
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-small-finetuned-eli5

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the eli5 dataset.
It achieves the following results on the evaluation set:
- Loss: 3.7555
- Rouge1: 11.8922
- Rouge2: 1.88
- Rougel: 9.6595
- Rougelsum: 10.8308
- Gen Len: 18.9911

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
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1  | Rouge2 | Rougel | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:------:|:------:|:---------:|:-------:|
| 3.9546        | 1.0   | 34080 | 3.7555          | 11.8922 | 1.88   | 9.6595 | 10.8308   | 18.9911 |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
