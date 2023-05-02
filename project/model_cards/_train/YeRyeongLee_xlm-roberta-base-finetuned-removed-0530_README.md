---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: xlm-roberta-base-finetuned-removed-0530
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-finetuned-removed-0530

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9944
- Accuracy: 0.8717
- F1: 0.8719

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
| No log        | 1.0   | 3180  | 0.6390          | 0.7899   | 0.7852 |
| No log        | 2.0   | 6360  | 0.5597          | 0.8223   | 0.8230 |
| No log        | 3.0   | 9540  | 0.5177          | 0.8462   | 0.8471 |
| No log        | 4.0   | 12720 | 0.5813          | 0.8642   | 0.8647 |
| No log        | 5.0   | 15900 | 0.7324          | 0.8557   | 0.8568 |
| No log        | 6.0   | 19080 | 0.7589          | 0.8626   | 0.8634 |
| No log        | 7.0   | 22260 | 0.7958          | 0.8752   | 0.8751 |
| 0.3923        | 8.0   | 25440 | 0.9177          | 0.8651   | 0.8653 |
| 0.3923        | 9.0   | 28620 | 1.0188          | 0.8673   | 0.8671 |
| 0.3923        | 10.0  | 31800 | 0.9944          | 0.8717   | 0.8719 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.9.0
- Datasets 1.16.1
- Tokenizers 0.12.1
