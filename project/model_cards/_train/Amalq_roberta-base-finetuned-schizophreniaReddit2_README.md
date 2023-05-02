---
license: mit
tags:
- generated_from_trainer
model-index:
- name: roberta-base-finetuned-schizophreniaReddit2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-finetuned-schizophreniaReddit2

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7785

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 490  | 1.8093          |
| 1.9343        | 2.0   | 980  | 1.7996          |
| 1.8856        | 3.0   | 1470 | 1.7966          |
| 1.8552        | 4.0   | 1960 | 1.7844          |
| 1.8267        | 5.0   | 2450 | 1.7839          |


### Framework versions

- Transformers 4.14.1
- Pytorch 1.10.0+cu111
- Datasets 1.16.1
- Tokenizers 0.10.3
