---
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: lg-en-v3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# lg-en-v3

This model is a fine-tuned version of [AI-Lab-Makerere/lg_en](https://huggingface.co/AI-Lab-Makerere/lg_en) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9289
- Bleu: 32.5138

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4.4271483249908667e-05
- train_batch_size: 14
- eval_batch_size: 6
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 2
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| No log        | 1.0   | 26   | 1.0323          | 32.6278 |
| No log        | 2.0   | 52   | 0.9289          | 32.5138 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
