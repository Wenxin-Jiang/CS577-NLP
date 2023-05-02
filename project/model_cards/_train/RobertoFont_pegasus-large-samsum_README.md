---
tags:
- generated_from_trainer
datasets:
- samsum
metrics:
- rouge
model-index:
- name: pegasus-large-samsum
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: samsum
      type: samsum
      args: samsum
    metrics:
    - name: Rouge1
      type: rouge
      value: 48.0968
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pegasus-large-samsum

This model is a fine-tuned version of [google/pegasus-large](https://huggingface.co/google/pegasus-large) on the samsum dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4109
- Rouge1: 48.0968
- Rouge2: 24.6663
- Rougel: 40.2569
- Rougelsum: 44.0137

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 64
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| No log        | 1.0   | 230  | 1.4646          | 45.0631 | 22.5567 | 38.0518 | 41.2694   |
| No log        | 2.0   | 460  | 1.4203          | 47.4122 | 24.158  | 39.7414 | 43.3485   |
| 1.699         | 3.0   | 690  | 1.4109          | 48.0968 | 24.6663 | 40.2569 | 44.0137   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
