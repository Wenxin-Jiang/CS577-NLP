---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: bert-base-uncased-finetuned-filtered-0609
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-filtered-0609

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1749
- Accuracy: 0.9789
- Precision: 0.9790
- Recall: 0.9789
- F1: 0.9789

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.1671        | 1.0   | 3180  | 0.1735          | 0.9632   | 0.9648    | 0.9632 | 0.9635 |
| 0.1384        | 2.0   | 6360  | 0.1120          | 0.9736   | 0.9738    | 0.9736 | 0.9736 |
| 0.1064        | 3.0   | 9540  | 0.1880          | 0.9635   | 0.9647    | 0.9635 | 0.9635 |
| 0.0823        | 4.0   | 12720 | 0.1495          | 0.9758   | 0.9759    | 0.9758 | 0.9757 |
| 0.0426        | 5.0   | 15900 | 0.1766          | 0.9742   | 0.9746    | 0.9742 | 0.9743 |
| 0.0254        | 6.0   | 19080 | 0.1724          | 0.9777   | 0.9778    | 0.9777 | 0.9777 |
| 0.0257        | 7.0   | 22260 | 0.1760          | 0.9764   | 0.9767    | 0.9764 | 0.9764 |
| 0.0017        | 8.0   | 25440 | 0.1672          | 0.9786   | 0.9787    | 0.9786 | 0.9786 |
| 0.0077        | 9.0   | 28620 | 0.1894          | 0.9789   | 0.9791    | 0.9789 | 0.9789 |
| 0.0014        | 10.0  | 31800 | 0.1749          | 0.9789   | 0.9790    | 0.9789 | 0.9789 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.9.1+cu111
- Datasets 1.16.1
- Tokenizers 0.12.1
