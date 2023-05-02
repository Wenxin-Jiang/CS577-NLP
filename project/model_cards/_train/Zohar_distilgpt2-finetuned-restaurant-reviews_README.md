---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: distilgpt2-finetuned-restaurant-reviews
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilgpt2-finetuned-restaurant-reviews

This model is a fine-tuned version of [distilgpt2](https://huggingface.co/distilgpt2) on a subset of the Yelp restaurant reviews dataset.
It achieves the following results on the evaluation set:
- Loss: 3.4668

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 3.6331        | 1.0   | 2536 | 3.5280          |
| 3.5676        | 2.0   | 5072 | 3.4793          |
| 3.5438        | 3.0   | 7608 | 3.4668          |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.2+cu102
- Datasets 1.18.2
- Tokenizers 0.11.0
