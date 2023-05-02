---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- crd3
metrics:
- rouge
model-index:
- name: primer-crd3
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: crd3
      type: crd3
      config: default
      split: train[:500]
      args: default
    metrics:
    - name: Rouge1
      type: rouge
      value: 0.1510358452879352
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# primer-crd3

This model is a fine-tuned version of [allenai/PRIMERA](https://huggingface.co/allenai/PRIMERA) on the crd3 dataset.
It achieves the following results on the evaluation set:
- Loss: 3.8193
- Rouge1: 0.1510
- Rouge2: 0.0279
- Rougel: 0.1251
- Rougelsum: 0.1355

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|:------:|:---------:|
| No log        | 1.0   | 250  | 2.9569          | 0.1762 | 0.0485 | 0.1525 | 0.1605    |
| 1.7993        | 2.0   | 500  | 3.4079          | 0.1612 | 0.0286 | 0.1367 | 0.1444    |
| 1.7993        | 3.0   | 750  | 3.8193          | 0.1510 | 0.0279 | 0.1251 | 0.1355    |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.8.0
- Datasets 2.7.0
- Tokenizers 0.13.2
