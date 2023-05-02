---
tags:
- generated_from_trainer
model-index:
- name: bert-base-parsbert-uncased-finetuned
  results:
  - task:
      name: Masked Language Modeling
      type: fill-mask
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-parsbert-uncased-finetuned

This model is a fine-tuned version of [HooshvareLab/bert-base-parsbert-uncased](https://huggingface.co/HooshvareLab/bert-base-parsbert-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.2045

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
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 3.5596        | 1.0   | 515  | 3.2097          |


### Framework versions

- Transformers 4.10.0
- Pytorch 1.9.0+cu102
- Datasets 1.11.0
- Tokenizers 0.10.3
