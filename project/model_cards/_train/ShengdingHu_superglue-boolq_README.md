---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: superglue-boolq
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# superglue-boolq

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2098
- Accuracy: 76.7584
- Average Metrics: 76.7584

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Average Metrics |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------------:|
| No log        | 0.34  | 100  | 0.2293          | 73.2722  | 73.2722         |
| No log        | 0.68  | 200  | 0.2098          | 76.7584  | 76.7584         |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.10.2+cu111
- Datasets 1.17.0
- Tokenizers 0.12.1
