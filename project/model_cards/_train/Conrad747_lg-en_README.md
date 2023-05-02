---
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: lg-en
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# lg-en

This model is a fine-tuned version of [AI-Lab-Makerere/lg_en](https://huggingface.co/AI-Lab-Makerere/lg_en) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0047
- Bleu: 31.3411

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| No log        | 1.0   | 178  | 1.0047          | 31.3411 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
