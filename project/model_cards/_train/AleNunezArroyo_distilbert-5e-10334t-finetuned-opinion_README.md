---
tags:
- generated_from_trainer
model-index:
- name: distilbert-5e-10334t-finetuned-opinion
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-5e-10334t-finetuned-opinion

This model is a fine-tuned version of [CenIA/distilbert-base-spanish-uncased](https://huggingface.co/CenIA/distilbert-base-spanish-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 4.6764

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
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 6.1394        | 1.0   | 898  | 5.4374          |
| 5.312         | 2.0   | 1796 | 5.0640          |
| 5.0305        | 3.0   | 2694 | 4.8486          |
| 4.8765        | 4.0   | 3592 | 4.7270          |
| 4.7992        | 5.0   | 4490 | 4.6803          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
