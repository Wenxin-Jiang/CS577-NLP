---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- yelp_review_full
metrics:
- accuracy
model-index:
- name: test-electra-small-yelp
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
      value: 0.5677007577622891
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# test-electra-small-yelp

This model is a fine-tuned version of [google/electra-small-discriminator](https://huggingface.co/google/electra-small-discriminator) on the yelp_review_full yelp_review_full dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2601
- Accuracy: 0.5677

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
- train_batch_size: 8
- eval_batch_size: 8
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
