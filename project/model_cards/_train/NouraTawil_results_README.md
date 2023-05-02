---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- rouge
model-index:
- name: results
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# results

This model is a fine-tuned version of [sshleifer/distilbart-xsum-12-3](https://huggingface.co/sshleifer/distilbart-xsum-12-3) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 4.8564
- Rouge1: 12.9538
- Rouge2: 3.654
- Rougel: 12.3643
- Rougelsum: 12.521
- Gen Len: 13.14

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 1
- label_smoothing_factor: 0.1

### Training results



### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.2
