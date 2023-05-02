---
tags:
- generated_from_trainer
model_index:
- name: bert-base-dutch-cased-finetuned-gv
  results:
  - task:
      name: Masked Language Modeling
      type: fill-mask
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-dutch-cased-finetuned-gv

This model is a fine-tuned version of [GroNLP/bert-base-dutch-cased](https://huggingface.co/GroNLP/bert-base-dutch-cased) on an unkown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7837

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
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.4741        | 1.0   | 2603 | 1.8404          |
| 1.2384        | 2.0   | 5206 | 1.8457          |
| 1.2121        | 3.0   | 7809 | 1.7837          |


### Framework versions

- Transformers 4.9.0
- Pytorch 1.9.0+cu102
- Datasets 1.10.2
- Tokenizers 0.10.3
