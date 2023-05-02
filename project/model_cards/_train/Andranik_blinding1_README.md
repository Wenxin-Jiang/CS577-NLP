---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: blinding
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# blinding

This model is a fine-tuned version of [michiyasunaga/BioLinkBERT-base](https://huggingface.co/michiyasunaga/BioLinkBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7158
- Accuracy: 0.6842

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 6.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.9949        | 2.0   | 20   | 0.9573          | 0.4737   |
| 0.5907        | 4.0   | 40   | 0.9047          | 0.5789   |
| 0.2675        | 6.0   | 60   | 0.7158          | 0.6842   |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
