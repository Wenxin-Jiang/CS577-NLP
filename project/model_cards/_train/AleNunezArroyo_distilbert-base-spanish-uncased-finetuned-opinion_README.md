---
tags:
- generated_from_trainer
model-index:
- name: distilbert-base-spanish-uncased-finetuned-opinion
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-spanish-uncased-finetuned-opinion

This model was trained from scratch on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 6.2078

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 12.7318       | 1.0   | 899  | 7.5402          |
| 7.8137        | 2.0   | 1798 | 7.0341          |
| 7.2367        | 3.0   | 2697 | 6.7184          |
| 6.9153        | 4.0   | 3596 | 6.5694          |
| 6.7086        | 5.0   | 4495 | 6.4376          |
| 6.5769        | 6.0   | 5394 | 6.3584          |
| 6.4833        | 7.0   | 6293 | 6.2887          |
| 6.4076        | 8.0   | 7192 | 6.2511          |
| 6.362         | 9.0   | 8091 | 6.2257          |
| 6.3296        | 10.0  | 8990 | 6.2064          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
