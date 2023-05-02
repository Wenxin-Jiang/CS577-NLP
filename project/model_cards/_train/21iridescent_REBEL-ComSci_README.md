---
license: cc-by-nc-sa-4.0
tags:
- generated_from_trainer
model-index:
- name: REBEL-ComSci
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# REBEL-ComSci

This model is a fine-tuned version of [Babelscape/rebel-large](https://huggingface.co/Babelscape/rebel-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 5.0770

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.002
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 210  | 5.2197          |
| No log        | 2.0   | 420  | 5.0887          |
| 5.8771        | 3.0   | 630  | 5.1124          |
| 5.8771        | 4.0   | 840  | 5.0977          |
| 4.5631        | 5.0   | 1050 | 5.0572          |
| 4.5631        | 6.0   | 1260 | 5.0645          |
| 4.5631        | 7.0   | 1470 | 5.0819          |
| 4.5209        | 8.0   | 1680 | 5.0690          |
| 4.5209        | 9.0   | 1890 | 5.0819          |
| 4.4896        | 10.0  | 2100 | 5.0770          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Tokenizers 0.13.1
