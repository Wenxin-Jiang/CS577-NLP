---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- matthews_correlation
model-index:
- name: pft-clf-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pft-clf-finetuned

This model is a fine-tuned version of [HooshvareLab/bert-fa-zwnj-base](https://huggingface.co/HooshvareLab/bert-fa-zwnj-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0987
- Matthews Correlation: 0.9737

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 6
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Matthews Correlation |
|:-------------:|:-----:|:----:|:---------------:|:--------------------:|
| 0.1299        | 1.0   | 1268 | 0.0987          | 0.9737               |


### Framework versions

- Transformers 4.26.0
- Pytorch 1.13.1+cu116
- Datasets 2.9.0
- Tokenizers 0.13.2
