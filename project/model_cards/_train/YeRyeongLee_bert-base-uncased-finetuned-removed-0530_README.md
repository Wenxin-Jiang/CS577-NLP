---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: bert-base-uncased-finetuned-removed-0530
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-finetuned-removed-0530

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1269
- Accuracy: 0.8745
- F1: 0.8745

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
| No log        | 1.0   | 3180  | 0.5939          | 0.8113   | 0.8113 |
| No log        | 2.0   | 6360  | 0.6459          | 0.8189   | 0.8183 |
| No log        | 3.0   | 9540  | 0.6523          | 0.8597   | 0.8604 |
| No log        | 4.0   | 12720 | 0.8159          | 0.8522   | 0.8521 |
| No log        | 5.0   | 15900 | 0.9294          | 0.8601   | 0.8599 |
| No log        | 6.0   | 19080 | 1.0066          | 0.8594   | 0.8592 |
| No log        | 7.0   | 22260 | 1.0268          | 0.8686   | 0.8689 |
| 0.2451        | 8.0   | 25440 | 1.0274          | 0.8758   | 0.8760 |
| 0.2451        | 9.0   | 28620 | 1.0850          | 0.8726   | 0.8727 |
| 0.2451        | 10.0  | 31800 | 1.1269          | 0.8745   | 0.8745 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.9.0
- Datasets 1.16.1
- Tokenizers 0.12.1
