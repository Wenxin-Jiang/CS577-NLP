---
language:
- en
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: bert-base-cased-rte
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: GLUE RTE
      type: glue
      args: rte
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.6534296028880866
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-cased-rte

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the GLUE RTE dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9753
- Accuracy: 0.6534

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
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.4837        | 3.21  | 500  | 0.9753          | 0.6534   |
| 0.0827        | 6.41  | 1000 | 1.6693          | 0.6715   |
| 0.0253        | 9.62  | 1500 | 1.7777          | 0.6643   |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.7.1
- Datasets 1.18.3
- Tokenizers 0.11.6
