---
tags:
- generated_from_trainer
datasets:
- xsum
metrics:
- rouge
model-index:
- name: fine-tune-Pegasus
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
      value: 17.993
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# fine-tune-Pegasus

This model is a fine-tuned version of [google/pegasus-large](https://huggingface.co/google/pegasus-large) on the xsum dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3242
- Rouge1: 17.993
- Rouge2: 2.9392
- Rougel: 12.313
- Rougelsum: 13.3091
- Gen Len: 67.0552

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6.35e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 500
- num_epochs: 1.0
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.1
- Datasets 1.17.0
- Tokenizers 0.10.3
