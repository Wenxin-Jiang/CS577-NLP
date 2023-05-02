---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: results
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# results

This model is a fine-tuned version of [t5-small](https://huggingface.co/t5-small) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2721

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
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step   | Validation Loss |
|:-------------:|:-----:|:------:|:---------------:|
| 0.505         | 1.0   | 26878  | 0.4409          |
| 0.4063        | 2.0   | 53756  | 0.3390          |
| 0.358         | 3.0   | 80634  | 0.2967          |
| 0.3383        | 4.0   | 107512 | 0.2777          |
| 0.3289        | 5.0   | 134390 | 0.2721          |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0
- Datasets 2.1.0
- Tokenizers 0.12.1
