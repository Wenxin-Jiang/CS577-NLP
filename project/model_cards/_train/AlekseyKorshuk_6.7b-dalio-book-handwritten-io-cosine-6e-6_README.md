---
license: other
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: 6.7b-dalio-book-handwritten-io-cosine-6e-6
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 6.7b-dalio-book-handwritten-io-cosine-6e-6

This model is a fine-tuned version of [facebook/opt-6.7b](https://huggingface.co/facebook/opt-6.7b) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 2.0586
- Accuracy: 0.3412

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 6e-06
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 8
- total_eval_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: constant
- num_epochs: 1.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.6377        | 0.11  | 6    | 2.4688          | 0.3016   |
| 2.5046        | 0.21  | 12   | 2.3848          | 0.3096   |
| 2.4755        | 0.32  | 18   | 2.3223          | 0.3156   |
| 2.459         | 0.43  | 24   | 2.2715          | 0.3201   |
| 2.3602        | 0.54  | 30   | 2.2246          | 0.3243   |
| 2.3829        | 0.64  | 36   | 2.1895          | 0.3275   |
| 2.3188        | 0.75  | 42   | 2.1465          | 0.3315   |
| 2.2895        | 0.86  | 48   | 2.1035          | 0.3365   |
| 2.3062        | 0.96  | 54   | 2.0586          | 0.3412   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.12.1
