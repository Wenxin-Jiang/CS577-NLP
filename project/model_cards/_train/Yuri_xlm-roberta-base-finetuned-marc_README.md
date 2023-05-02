---
license: mit
tags:
- generated_from_trainer
datasets:
- amazon_reviews_multi
model-index:
- name: xlm-roberta-base-finetuned-marc
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-finetuned-marc

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the amazon_reviews_multi dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9825
- Mae: 0.4956

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
- num_epochs: 2

### Training results

| Training Loss | Epoch | Step | Validation Loss | Mae    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 1.1432        | 1.0   | 308  | 1.0559          | 0.5133 |
| 0.9883        | 2.0   | 616  | 0.9825          | 0.4956 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0+cu111
- Datasets 1.13.3
- Tokenizers 0.10.3
