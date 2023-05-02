---
tags:
- generated_from_trainer
model-index:
- name: dna_3-Pretrained
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dna_3-Pretrained

This model is a fine-tuned version of [](https://huggingface.co/) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6003

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.6057        | 1.0   | 62   | 0.6032          |
| 0.5983        | 2.0   | 124  | 0.6002          |
| 0.5934        | 3.0   | 186  | 0.5992          |
| 0.5853        | 4.0   | 248  | 0.5979          |
| 0.5799        | 5.0   | 310  | 0.5982          |
| 0.5769        | 6.0   | 372  | 0.5999          |
| 0.5754        | 7.0   | 434  | 0.5996          |
| 0.5713        | 8.0   | 496  | 0.6000          |
| 0.5687        | 9.0   | 558  | 0.5988          |
| 0.5666        | 10.0  | 620  | 0.6003          |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
