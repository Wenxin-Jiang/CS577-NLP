---
tags:
- xsum_v1_last
- generated_from_trainer
datasets:
- xsum
metrics:
- rouge
model-index:
- name: pegasus-large-finetune-xsum
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: xsum
      type: xsum
      args: default
    metrics:
    - name: Rouge1
      type: rouge
      value: 5.0462
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pegasus-large-finetune-xsum

This model is a fine-tuned version of [google/pegasus-large](https://huggingface.co/google/pegasus-large) on the xsum dataset.
It achieves the following results on the evaluation set:
- Loss: 10.0826
- Rouge1: 5.0462
- Rouge2: 0.6914
- Rougel: 3.5071
- Rougelsum: 3.9548

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
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| 11.4044       | 1.0   | 13   | 10.7501         | 5.5154 | 0.5561 | 3.8425 | 4.2435    |
| 10.5741       | 2.0   | 26   | 10.2309         | 5.4282 | 0.7228 | 3.5759 | 4.0538    |
| 10.0146       | 3.0   | 39   | 10.0826         | 5.0462 | 0.6914 | 3.5071 | 3.9548    |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.13.0
- Datasets 2.6.1
- Tokenizers 0.11.0
