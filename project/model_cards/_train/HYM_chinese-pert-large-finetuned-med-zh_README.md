---
tags:
- generated_from_trainer
model-index:
- name: chinese-pert-large-finetuned-med-zh
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# chinese-pert-large-finetuned-med-zh

This model is a fine-tuned version of [](https://huggingface.co/) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4370

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 0.9428        | 1.0   | 14081 | 10.3783         |
| 0.8847        | 2.0   | 28162 | 6.8072          |
| 0.8689        | 3.0   | 42243 | 1.3781          |
| 0.8592        | 4.0   | 56324 | 5.5274          |
| 0.8734        | 5.0   | 70405 | 1.4370          |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.8.0+cu111
- Datasets 2.4.0
- Tokenizers 0.10.3
