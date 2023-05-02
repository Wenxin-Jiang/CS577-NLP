---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- samsum
metrics:
- rouge
model-index:
- name: dialogue-summarizationv1
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: samsum
      type: samsum
      args: samsum
    metrics:
    - name: Rouge1
      type: rouge
      value: 47.3665
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dialogue-summarizationv1

This model is a fine-tuned version of [facebook/bart-base](https://huggingface.co/facebook/bart-base) on the samsum dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5298
- Rouge1: 47.3665
- Rouge2: 23.9331
- Rougel: 39.9646
- Rougelsum: 43.594
- Gen Len: 17.8264

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 1.5818        | 1.0   | 1841 | 1.5298          | 47.3665 | 23.9331 | 39.9646 | 43.594    | 17.8264 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
