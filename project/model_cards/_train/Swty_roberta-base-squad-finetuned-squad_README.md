---
license: cc-by-4.0
tags:
- generated_from_trainer
model-index:
- name: roberta-base-squad-finetuned-squad
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-squad-finetuned-squad

This model is a fine-tuned version of [deepset/roberta-base-squad2](https://huggingface.co/deepset/roberta-base-squad2) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 6.7060

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 17   | 5.9055          |
| No log        | 2.0   | 34   | 6.2285          |
| No log        | 3.0   | 51   | 6.8639          |
| No log        | 4.0   | 68   | 6.3238          |
| No log        | 5.0   | 85   | 7.0916          |
| No log        | 6.0   | 102  | 6.7791          |
| No log        | 7.0   | 119  | 6.8093          |
| No log        | 8.0   | 136  | 6.7029          |
| No log        | 9.0   | 153  | 6.7142          |
| No log        | 10.0  | 170  | 6.7060          |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.11.0+cu102
- Datasets 2.6.1
- Tokenizers 0.12.1
