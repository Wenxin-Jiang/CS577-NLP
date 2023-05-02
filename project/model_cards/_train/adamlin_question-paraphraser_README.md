---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- adamlin/question_augmentation
metrics:
- rouge
model-index:
- name: question-paraphraser
  results:
  - task:
      name: Summarization
      type: summarization
    dataset:
      name: adamlin/question_augmentation
      type: adamlin/question_augmentation
    metrics:
    - name: Rouge1
      type: rouge
      value: 0.5385
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# question-paraphraser

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the adamlin/question_augmentation dataset.
It achieves the following results on the evaluation set:
- Loss: 3.5901
- Rouge1: 0.5385
- Rouge2: 0.0769
- Rougel: 0.5586
- Rougelsum: 0.5586
- Gen Len: 7.6712

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
- num_epochs: 3.0

### Training results



### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0
- Datasets 2.3.2
- Tokenizers 0.12.1
