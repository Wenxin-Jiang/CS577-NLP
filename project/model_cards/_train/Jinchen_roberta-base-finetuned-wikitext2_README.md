---
license: mit
tags:
- generated_from_trainer
model-index:
- name: roberta-base-finetuned-wikitext2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-base-finetuned-wikitext2

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5020

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: IPU
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- total_eval_batch_size: 20
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0
- training precision: Mixed Precision

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.6689        | 1.0   | 300  | 1.5518          |
| 1.7525        | 2.0   | 600  | 1.5078          |
| 1.5267        | 3.0   | 900  | 1.4971          |


### Framework versions

- Transformers 4.20.0
- Pytorch 1.10.0+cpu
- Datasets 2.4.0
- Tokenizers 0.12.1
