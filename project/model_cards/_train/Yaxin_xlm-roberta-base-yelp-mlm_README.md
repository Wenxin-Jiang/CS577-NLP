---
license: mit
tags:
- generated_from_trainer
datasets:
- yelp_review_full
metrics:
- accuracy
model-index:
- name: xlm-roberta-base-yelp-mlm
  results:
  - task:
      name: Masked Language Modeling
      type: fill-mask
    dataset:
      name: yelp_review_full yelp_review_full
      type: yelp_review_full
      args: yelp_review_full
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.7356223359340127
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# xlm-roberta-base-yelp-mlm

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) on the yelp_review_full yelp_review_full dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1743
- Accuracy: 0.7356

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results



### Framework versions

- Transformers 4.18.0.dev0
- Pytorch 1.10.0
- Datasets 1.18.3
- Tokenizers 0.11.0
