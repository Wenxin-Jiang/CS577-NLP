---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: codet5-base-masked-buggy-code-repair
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# codet5-base-masked-buggy-code-repair

This model is a fine-tuned version of [Salesforce/codet5-base](https://huggingface.co/Salesforce/codet5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2876
- Precision: 0.1990
- Recall: 0.3
- F1: 0.2320
- Accuracy: 0.3

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
- num_epochs: 10

### Training results



### Framework versions

- Transformers 4.16.2
- Pytorch 1.9.1
- Datasets 1.18.4
- Tokenizers 0.11.6
