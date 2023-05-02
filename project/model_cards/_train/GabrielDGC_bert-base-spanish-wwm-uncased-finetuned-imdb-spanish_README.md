---
tags:
- generated_from_trainer
datasets:
- tesis
model-index:
- name: bert-base-spanish-wwm-uncased-finetuned-imdb-spanish
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-spanish-wwm-uncased-finetuned-imdb-spanish

This model is a fine-tuned version of [dccuchile/bert-base-spanish-wwm-uncased](https://huggingface.co/dccuchile/bert-base-spanish-wwm-uncased) on the tesis dataset.
It achieves the following results on the evaluation set:
- Loss: 5.0087

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
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 1    | 4.7540          |
| No log        | 2.0   | 2    | 4.7894          |
| No log        | 3.0   | 3    | 4.4417          |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
