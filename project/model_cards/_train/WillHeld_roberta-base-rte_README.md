---
language:
- en
license: mit
tags:
- generated_from_trainer
datasets:
- glue
metrics:
- accuracy
model-index:
- name: roberta-base-rte
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
      value: 0.7581227436823105
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-rte

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the GLUE RTE dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7660
- Accuracy: 0.7581

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
| 0.551         | 3.21  | 500  | 0.7660          | 0.7581   |
| 0.1665        | 6.41  | 1000 | 1.5218          | 0.7690   |
| 0.0463        | 9.62  | 1500 | 1.6747          | 0.7653   |


### Framework versions

- Transformers 4.21.3
- Pytorch 1.7.1
- Datasets 1.18.3
- Tokenizers 0.11.6
