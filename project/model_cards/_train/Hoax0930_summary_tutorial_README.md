---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
datasets:
- amazon_reviews_multi
metrics:
- rouge
model-index:
- name: summary_tutorial
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: amazon_reviews_multi
      type: amazon_reviews_multi
      config: en
      split: train
      args: en
    metrics:
    - name: Rouge1
      type: rouge
      value: 19.4358
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# summary_tutorial

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on the amazon_reviews_multi dataset.
It achieves the following results on the evaluation set:
- Loss: 2.8504
- Rouge1: 19.4358
- Rouge2: 10.0475
- Rougel: 18.6327
- Rougelsum: 18.648

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| 2.867         | 1.0   | 771  | 2.7687          | 18.7278 | 10.8323 | 17.9617 | 17.8262   |
| 2.5363        | 2.0   | 1542 | 2.7741          | 18.4642 | 10.2431 | 17.8719 | 17.7799   |
| 2.3516        | 3.0   | 2313 | 2.7578          | 18.4591 | 9.5235  | 18.0114 | 17.8761   |
| 2.216         | 4.0   | 3084 | 2.7938          | 20.2372 | 10.7222 | 19.5686 | 19.5045   |
| 2.0929        | 5.0   | 3855 | 2.7981          | 19.536  | 10.0232 | 18.7119 | 18.7774   |
| 2.0           | 6.0   | 4626 | 2.8229          | 18.5138 | 9.6349  | 17.7119 | 17.782    |
| 1.9479        | 7.0   | 5397 | 2.8397          | 19.3795 | 10.0475 | 18.5904 | 18.532    |
| 1.9031        | 8.0   | 6168 | 2.8504          | 19.4358 | 10.0475 | 18.6327 | 18.648    |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
