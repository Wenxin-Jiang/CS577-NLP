---
license: mit
tags:
- generated_from_trainer
datasets:
- Yaxin/amazon_reviews_multi
metrics:
- accuracy
model-index:
- name: xlm-roberta-base-amazon-en-es-fr-mlm
  results:
  - task:
      name: Masked Language Modeling
      type: fill-mask
    dataset:
      name: Yaxin/amazon_reviews_multi
      type: Yaxin/amazon_reviews_multi
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.6951035447140035
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-amazon-en-es-fr-mlm

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the Yaxin/amazon_reviews_multi dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3936
- Accuracy: 0.6951

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
- train_batch_size: 6
- eval_batch_size: 6
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5.0

### Training results



### Framework versions

- Transformers 4.18.0.dev0
- Pytorch 1.11.0
- Datasets 2.0.0
- Tokenizers 0.11.6
