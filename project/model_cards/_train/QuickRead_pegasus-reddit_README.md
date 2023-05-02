---
tags:
- generated_from_trainer
datasets:
- reddit
metrics:
- rouge
model-index:
- name: pegasus-reddit
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: reddit
      type: reddit
      args: default
    metrics:
    - name: Rouge1
      type: rouge
      value: 23.967
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pegasus-reddit

This model is a fine-tuned version of [google/pegasus-large](https://huggingface.co/google/pegasus-large) on the reddit dataset.
It achieves the following results on the evaluation set:
- Loss: 3.3329
- Rouge1: 23.967
- Rouge2: 5.0032
- Rougel: 15.3267
- Rougelsum: 18.5905
- Gen Len: 69.2193

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
