---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-base-uncased-finetuned-filtered-0602
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-filtered-0602

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1959
- Accuracy: 0.9783
- F1: 0.9783

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

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|
| 0.1777        | 1.0   | 3180  | 0.2118          | 0.9563   | 0.9566 |
| 0.1409        | 2.0   | 6360  | 0.1417          | 0.9736   | 0.9736 |
| 0.1035        | 3.0   | 9540  | 0.1454          | 0.9739   | 0.9739 |
| 0.0921        | 4.0   | 12720 | 0.1399          | 0.9755   | 0.9755 |
| 0.0607        | 5.0   | 15900 | 0.1150          | 0.9792   | 0.9792 |
| 0.0331        | 6.0   | 19080 | 0.1770          | 0.9758   | 0.9758 |
| 0.0289        | 7.0   | 22260 | 0.1782          | 0.9767   | 0.9767 |
| 0.0058        | 8.0   | 25440 | 0.1877          | 0.9796   | 0.9796 |
| 0.008         | 9.0   | 28620 | 0.2034          | 0.9764   | 0.9764 |
| 0.0017        | 10.0  | 31800 | 0.1959          | 0.9783   | 0.9783 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.9.0
- Datasets 1.16.1
- Tokenizers 0.12.1
