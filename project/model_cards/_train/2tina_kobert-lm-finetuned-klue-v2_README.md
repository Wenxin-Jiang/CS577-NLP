---
tags:
- generated_from_trainer
model-index:
- name: kobert-lm-finetuned-klue-v2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# kobert-lm-finetuned-klue-v2

This model is a fine-tuned version of [monologg/kobert-lm](https://huggingface.co/monologg/kobert-lm) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 4.9679

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 5.7641        | 0.52  | 500  | 5.6079          |
| 5.5176        | 1.04  | 1000 | 5.4635          |
| 5.4401        | 1.57  | 1500 | 5.3370          |
| 5.2919        | 2.09  | 2000 | 5.2396          |
| 5.1756        | 2.61  | 2500 | 5.2675          |
| 5.0793        | 3.13  | 3000 | 5.1546          |
| 4.8933        | 3.66  | 3500 | 5.0728          |
| 4.7273        | 4.18  | 4000 | 5.0165          |
| 4.5473        | 4.7   | 4500 | 4.9679          |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu113
- Datasets 2.5.2
- Tokenizers 0.12.1
