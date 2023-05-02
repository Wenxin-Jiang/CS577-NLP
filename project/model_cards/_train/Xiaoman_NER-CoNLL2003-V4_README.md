---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: NER-CoNLL2003-V4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# NER-CoNLL2003-V4

This model is a fine-tuned version of [bert-large-uncased](https://huggingface.co/bert-large-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2095

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.961395091713594e-05
- train_batch_size: 6
- eval_batch_size: 6
- seed: 27
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 14   | 0.3630          |
| No log        | 2.0   | 28   | 0.2711          |
| No log        | 3.0   | 42   | 0.2407          |
| No log        | 4.0   | 56   | 0.2057          |
| No log        | 5.0   | 70   | 0.2095          |


### Framework versions

- Transformers 4.19.1
- Pytorch 1.11.0+cu113
- Datasets 2.2.1
- Tokenizers 0.12.1
