---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- pub_med_summarization_dataset
metrics:
- rouge
model-index:
- name: t5-base-finetuned-pubmed
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: pub_med_summarization_dataset
      type: pub_med_summarization_dataset
      args: document
    metrics:
    - name: Rouge1
      type: rouge
      value: 9.3771
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-finetuned-pubmed

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on the pub_med_summarization_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 2.6311
- Rouge1: 9.3771
- Rouge2: 3.7042
- Rougel: 8.4912
- Rougelsum: 9.0013
- Gen Len: 19.0

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Rouge1 | Rouge2 | Rougel | Rougelsum | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:---------:|:-------:|
| 2.0957        | 1.0   | 4000  | 1.9006          | 8.6968 | 3.2473 | 7.9565 | 8.3224    | 19.0    |
| 2.0489        | 2.0   | 8000  | 1.8571          | 8.6877 | 3.2461 | 7.9311 | 8.2991    | 19.0    |
| 2.7345        | 3.0   | 12000 | 2.6112          | 9.585  | 3.0129 | 8.4729 | 9.1109    | 19.0    |
| 3.0585        | 4.0   | 16000 | 2.7222          | 9.7011 | 3.3549 | 8.6588 | 9.2646    | 19.0    |
| 2.9437        | 5.0   | 20000 | 2.6311          | 9.3771 | 3.7042 | 8.4912 | 9.0013    | 19.0    |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.6
