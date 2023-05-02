---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- samsum
metrics:
- rouge
model-index:
- name: t5-samsung
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: samsum
      type: samsum
      config: samsum
      split: train
      args: samsum
    metrics:
    - name: Rouge1
      type: rouge
      value: 42.2345
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-samsung

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the samsum dataset.
It achieves the following results on the evaluation set:
- Loss: 1.8153
- Rouge1: 42.2345
- Rouge2: 18.983
- Rougel: 33.0073
- Rougelsum: 38.8755
- Gen Len: 36.4242

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| 2.0028        | 1.0   | 1841 | 1.8153          | 42.2345 | 18.983 | 33.0073 | 38.8755   | 36.4242 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
