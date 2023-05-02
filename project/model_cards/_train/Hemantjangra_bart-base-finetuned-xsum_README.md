---
license: apache-2.0
tags:
- summarization_t5_xsum
- generated_from_trainer
datasets:
- xsum
metrics:
- rouge
model-index:
- name: bart-base-finetuned-xsum
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
      value: 34.6293
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bart-base-finetuned-xsum

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on the xsum dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1755
- Rouge1: 34.6293
- Rouge2: 13.4749
- Rougel: 28.2616
- Rougelsum: 28.2553

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
- train_batch_size: 10
- eval_batch_size: 10
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| 2.4765        | 1.0   | 1000 | 2.0873          | 33.9596 | 12.722  | 27.4135 | 27.4062   |
| 1.9854        | 2.0   | 2000 | 2.0802          | 33.6802 | 12.8965 | 27.4061 | 27.4064   |
| 1.6677        | 3.0   | 3000 | 2.0998          | 34.2038 | 13.1362 | 27.8808 | 27.8806   |
| 1.4313        | 4.0   | 4000 | 2.1404          | 34.8491 | 13.4154 | 28.2768 | 28.2702   |
| 1.275         | 5.0   | 5000 | 2.1755          | 34.6293 | 13.4749 | 28.2616 | 28.2553   |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
