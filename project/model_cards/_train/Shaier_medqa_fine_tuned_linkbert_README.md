---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: medqa_fine_tuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# medqa_fine_tuned

This model is a fine-tuned version of [michiyasunaga/BioLinkBERT-base](https://huggingface.co/michiyasunaga/BioLinkBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4462
- Accuracy: 0.4002

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 100
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| No log        | 1.0   | 318  | 1.3208          | 0.3553   |
| 1.2802        | 2.0   | 636  | 1.3428          | 0.3703   |
| 1.2802        | 3.0   | 954  | 1.3780          | 0.3892   |
| 1.1466        | 4.0   | 1272 | 1.4234          | 0.3978   |
| 1.052         | 5.0   | 1590 | 1.4462          | 0.4002   |


### Framework versions

- Transformers 4.18.0
- Pytorch 1.11.0
- Datasets 2.3.2
- Tokenizers 0.11.0
