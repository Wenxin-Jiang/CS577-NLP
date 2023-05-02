---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: distilroberta-base-testingSB
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilroberta-base-testingSB

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on a company specific, Danish dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0403

## Model description

Customer-specific model used to embed asset management work orders in Danish

## Intended uses & limitations

Customer-specific and trained for unsupervised categorization tasks

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results
Epoch	Training Loss	Validation Loss
1	0.988500	1.056376
2	0.996300	1.027803
3	0.990300	1.040270

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.98850        | 1.0   | 1461 | 1.5211          |
| 1.3179        | 2.0   | 2922 | 1.3314          |
| 1.1931        | 3.0   | 4383 | 1.2530          |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.10.0+cu111
- Datasets 1.15.1
- Tokenizers 0.10.3
