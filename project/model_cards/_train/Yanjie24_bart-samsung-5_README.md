---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- samsum
metrics:
- rouge
model-index:
- name: bart-samsung-5
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
      value: 48.4734
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-samsung-5

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on the samsum dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4959
- Rouge1: 48.4734
- Rouge2: 25.3475
- Rougel: 40.9144
- Rougelsum: 44.7797
- Gen Len: 18.22

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
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 1.6107        | 1.0   | 1841 | 1.5390          | 47.1407 | 24.384  | 40.4826 | 43.4437   | 17.5513 |
| 1.5528        | 2.0   | 3682 | 1.4971          | 48.5483 | 25.1562 | 41.1806 | 44.7254   | 18.3521 |
| 1.4225        | 3.0   | 5523 | 1.5013          | 48.2461 | 25.2181 | 40.9022 | 44.4942   | 18.0844 |
| 1.3266        | 4.0   | 7364 | 1.4976          | 48.8949 | 25.4367 | 41.2355 | 45.0961   | 18.2359 |
| 1.2635        | 5.0   | 9205 | 1.4959          | 48.4734 | 25.3475 | 40.9144 | 44.7797   | 18.22   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.7.1
- Tokenizers 0.13.2
